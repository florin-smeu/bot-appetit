from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from typing import Dict, Text, Any, List

import requests
from operator import itemgetter

from rasa_sdk import Action
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.forms import FormAction


API_KEY = 'AIzaSyAu-uc1As4xBhfge4l_9Aj4qZ-Vh6IJYWg'

ENDPOINTS = {
    "base": "https://maps.googleapis.com/maps/api/place/textsearch/json?",
    "query": "query={}",
    "key": "&key={}"
}

FACILITY_TYPES = {
    "restaurant": {
        "name": "restaurant"
    },
    "bar": {
        "name": "bar"
    },
    "cafe": {
        "name": "cafe"
    }
}

def _create_path(query: Text) -> Text:
    """Creates a path to find provider using the endpoints."""
    return ENDPOINTS["base"] + ENDPOINTS["query"].format(query) + ENDPOINTS["key"].format(API_KEY)

def _find_facilities(location: Text, facility_type: Text) -> List[Dict]:
    """Returns json of facilities matching the search criteria."""

    full_path = _create_path(facility_type + " " + location + " Romania")

    print("Full path:")
    print(full_path)

    results = requests.get(full_path).json()
    return results['results']


def _resolve_name(facility_types, resource) -> Text:
    for key, value in facility_types.items():
        if value.get("name") == resource:
            return value.get("name")
    return ""


class FindFacilityTypes(Action):
    """This action class allows to display buttons for each facility type
    for the user to chose from to fill the facility_type entity slot."""

    def name(self) -> Text:
        """Unique identifier of the action"""

        return "find_facility_types"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        buttons = []
        for t in FACILITY_TYPES:
            facility_type = FACILITY_TYPES[t]
            payload = "/inform{\"facility_type\": \"" + facility_type.get(
                "name") + "\"}"

            buttons.append(
                {"title": "{}".format(facility_type.get("name").title()),
                 "payload": payload})

        dispatcher.utter_message(template="utter_greet", buttons=buttons)
        return []


class FacilityForm(FormAction):
    """Custom form action to fill all slots required to find specific type
    of eating facilities in a certain city or zip code."""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "facility_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["facility_type", "location"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"facility_type": self.from_entity(entity="facility_type",
                                                  intent=["inform",
                                                          "search_provider"]),
                "location": self.from_entity(entity="location",
                                             intent=["inform",
                                                     "search_provider"])}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:
        """Once required slots are filled, print a message"""

        location = tracker.get_slot('location')
        facility_type = tracker.get_slot('facility_type')

        message = "I am now searching for {}s in {}".format(facility_type, location)
        dispatcher.utter_message(message)
        return []

class FacilityAction(Action):

    def name(self) -> Text:
        return "facility_action"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        location = tracker.get_slot('location')
        facility_type = tracker.get_slot('facility_type')

        results = _find_facilities(location, facility_type)
        button_name = _resolve_name(FACILITY_TYPES, facility_type)
        if len(results) == 0:
            dispatcher.utter_message(
                "Sorry, we could not find a {} in {}.".format(button_name,
                                                              location.title()))
            return []

        buttons = []

        # limit number of results to 3 for clear presentation purposes
        rating_sorted_results = sorted(results, key=itemgetter('rating'), reverse=True)


        for r in rating_sorted_results[:3]:
            name = r["name"]
            facility_address = r["formatted_address"]

            payload = "/inform{\"facility_name\":\"" + name + "\"}"
            buttons.append(
                {"title": "{}".format(name), "payload": payload})

        if len(buttons) == 1:
            message = "Here is a {} near you:".format(button_name)
        else:
            message = "Here are {} {}s near you:".format(len(buttons),
                                                         button_name)

        # TODO: update rasa core version for configurable `button_type`
        dispatcher.utter_button_message(message, buttons)
        return []


class DetailsForm(FormAction):
    """This form class retrieves the address of the user's
    eating facility choice to display it to the user."""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "details_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
            """A list of required slots that the form has to fill"""

            return ["facility_type", "facility_name"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"facility_type": self.from_entity(entity="facility_type",
                                                  intent=["inform",
                                                          "search_provider"]),
                "facility_name": self.from_entity(entity="facility_name",
                                             intent=["inform",
                                                     "search_provider"])}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:

        facility_type = tracker.get_slot("facility_type")
        facility_name = tracker.get_slot("facility_name")

        message = "I am now searching for details for the {} {}".format(facility_name, facility_type)
        dispatcher.utter_message(message)
        return []

class DetailsAction(Action):
    def name(self) -> Text:
        return "details_action"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        facility_type = tracker.get_slot("facility_type")
        facility_name = tracker.get_slot("facility_name")
        location = tracker.get_slot("location")

        full_path = _create_path(facility_type + " " + facility_name + " " + location + " Romania")
        print(full_path)
        results = requests.get(full_path).json()
        results = results["results"]
        if results:
            print(results)
            selected = results[0]
            address = selected["formatted_address"]

            #dispatcher.utter_message("The address of {} is {}".format(facility_name, address))
            return [SlotSet("facility_address", address)]
        else:
            print("No address found. Most likely this action was executed "
                  "before the user choose a eating facility from the "
                  "provided list. "
                  "If this is a common problem in your dialogue flow,"
                  "using a form instead for this action might be appropriate.")

            #dispatcher.utter_message("Sorry I couldn't find the address for {}".format(facility_name))
            return [SlotSet("facility_address", "No address")]
