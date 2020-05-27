from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from typing import Dict, Text, Any, List

import requests
from operator import itemgetter

from rasa_sdk import Action
from rasa_sdk.events import SlotSet, FollowupAction, Restarted, AllSlotsReset
from rasa_sdk.forms import FormAction

from places_util import *




TEXTSEARCH_ENDPOINTS = {
    "base": "https://maps.googleapis.com/maps/api/place/textsearch/json?",
    "query": "query={}", # custom query
    "key": "&key={}", # api key
    "type": "&type={}", # same as in nearbysearch
    "region": "&region=ro",
    # minprice maxprice
    # opennow
    # #location
}

NEARBY_ENDPOINTS = {
    "base": "https://maps.googleapis.com/maps/api/place/nearbysearch/json?",
    "location": "&location={}", #latitude,longitude
    "key": "&key={}", # api key
    "type": "&type={}", # restaurant / bar / cafe
    "rankby": "&rankby={}", # distance / prominence
    "keyword": "&keyword={}", # custom term
    # opennow
    # minprice maxprice
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

def _create_path(query: Text, type: Text) -> Text:
    """Creates a path to find provider using the endpoints."""
    return TEXTSEARCH_ENDPOINTS["base"] + \
           TEXTSEARCH_ENDPOINTS["query"].format(query) + \
           TEXTSEARCH_ENDPOINTS["key"].format(API_KEY) + \
           TEXTSEARCH_ENDPOINTS["type"].format(type)


def _find_facilities(query: Text, type: Text) -> List[Dict]:
    """Returns json of facilities matching the search criteria."""

    full_path = _create_path(query, type)

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

        rating_sorted_results = sorted(results, key=itemgetter('rating'), reverse=True)

        # limit number of results to 3 for clear presentation purposes
        for r in rating_sorted_results[:3]:
            name = r["name"]
            place_id = r["place_id"]

            payload = "/inform{\"place_id\":\"" + place_id + "\"}"
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

            return ["facility_type", "place_id", "location"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"facility_type": self.from_entity(entity="facility_type",
                                                  intent=["inform",
                                                          "search_provider"]),
                "place_id": self.from_entity(entity="place_id",
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

        facility_type = tracker.get_slot("facility_type")
        place_id = tracker.get_slot("place_id")
        location = tracker.get_slot("location")

        message = "I am now searching for details for the {} {}".format(place_id, facility_type)
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
        place_id = tracker.get_slot("place_id")
        location = tracker.get_slot("location")

        details = Details(place_id)
        details_path = details.create_details_path()
        print(details_path)
        success = details.retrieve()

        if success is True:
            return [SlotSet("facility_details", details.__dict__)]
        else:
            print("No address found. Most likely this action was executed "
                  "before the user choose a eating facility from the "
                  "provided list. "
                  "If this is a common problem in your dialogue flow,"
                  "using a form instead for this action might be appropriate.")

            dispatcher.utter_message("Sorry I couldn't find details for {}".format(place_id))
            return [SlotSet("facility_details", "No details")]


class PhotosAction(Action):
    def name(self) -> Text:
        return "photos_action"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        facility_details = tracker.get_slot("facility_details")
        place_id = tracker.get_slot("place_id")
        location = tracker.get_slot("location")

        photo_paths = []
        for photo in facility_details["photos"][:2]:
            photo_obj = Photo(height=photo["height"],
                              width=photo["width"],
                              photo_reference=photo["photo_reference"],
                              html_attributions=photo["html_attributions"])
            photo_paths.append(photo_obj.create_photo_path())

        message = "Here are some photos for {} in {}".format(place_id, location)
        dispatcher.utter_message(message)

        gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": facility_details["name"],
                            "image_url": photo_paths[0],
                            "subtitle": "We have the right hat for everyone.",
                            "default_action": {
                                "type": "web_url",
                                "url": "https://tithal.life",
                                "webview_height_ratio": "tall",
                            },
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "url": "https://tithal.life",
                                    "title": "View Website"
                                },
                                {
                                    "type": "postback",
                                    "title": "Start Chatting",
                                    "payload": "DEVELOPER_DEFINED_PAYLOAD"
                                }
                            ]
                        },
                        {
                            "title": facility_details["name"],
                            "image_url": photo_paths[1],
                            "subtitle": "We have the right hat for everyone.",
                            "default_action": {
                                "type": "web_url",
                                "url": "https://tithal.life",
                                "webview_height_ratio": "tall",
                            },
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "url": "https://tithal.life",
                                    "title": "View Website"
                                },
                                {
                                    "type": "postback",
                                    "title": "Start Chatting",
                                    "payload": "DEVELOPER_DEFINED_PAYLOAD"
                                }
                            ]
                        }
                    ]
                }
            }
        }
        dispatcher.utter_custom_json(gt)
        return []


class ActionRestarted(Action):
    def name(self):
        return 'action_restarted'
    def run(self, dispatcher, tracker, domain):
        return[Restarted()]

class ActionSlotReset(Action):
    def name(self):
        return 'action_slot_reset'
    def run(self, dispatcher, tracker, domain):
        return[AllSlotsReset()]
