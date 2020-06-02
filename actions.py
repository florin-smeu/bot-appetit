from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from typing import Dict, Text, Any, List

import requests
import math
import random
from operator import itemgetter

from rasa_sdk import Action
from rasa_sdk.events import SlotSet, FollowupAction, Restarted, AllSlotsReset
from rasa_sdk.forms import FormAction

API_KEY = 'AIzaSyAu-uc1As4xBhfge4l_9Aj4qZ-Vh6IJYWg'
DEFAULT_WEBSITE = "https://bot-appetit.com"
DEFAULT_PROTOCOL = "https"
NO_PHOTO = "no_photo"
EMOJIES = {
    "smirking_face": u'\U0001F4B8',
    "thinking_face": u'\U0001F914',
    "sweat_smile": u'\U0001F605',
    "laughing_face": u'\U0001F602',
    "burger": u'\U0001F354',
    "coffee": u'\U00002615',
    "cocktail": u'\U0001F379',
    "star": u'\U00002B50',
    "money": u'\U0001F4B8',
    "pin": u'\U0001F4CC',
    "phone": u'\U0000260E',
    "calendar": u'\U0001F4C6',
    "world": u'\U0001F30D',
}
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
        "name": "restaurant",
        "emoji": EMOJIES["burger"],
    },
    "bar": {
        "name": "bar",
        "emoji": EMOJIES["cocktail"],
    },
    "cafe": {
        "name": "cafe",
        "emoji": EMOJIES["coffee"],
    }
}

class Details:
    """Class that stores all the details a facility can offer"""
    ENDPOINTS = {
        "base": "https://maps.googleapis.com/maps/api/place/details/json?",
        "place_id": "place_id={}",
        "fields": "&fields=photo",
        "key": "&key={}",
    }

    def __init__(self, place_id):
        self.place_id = place_id
        self.create_details_path()

    def create_details_path(self):
        """Creates a path to find provider using the endpoints."""
        self.path = Details.ENDPOINTS["base"] + \
                    Details.ENDPOINTS["place_id"].format(self.place_id) + \
                    Details.ENDPOINTS["key"].format(API_KEY)

        return self.path

    def retrieve(self):
        path = self.create_details_path()

        if self.path is None:
            print("[ERROR] Path is None for", self.place_id)
            return False

        result = requests.get(self.path).json()
        if result["status"] != "OK":
            print("[ERROR] The status is not OK for", self.place_id, result["status"])
            return False

        result = result["result"]

        #with open("details" + result["name"].replace(" ", "") + ".json", "w") as f:
        #    json.dump(result, f, ensure_ascii=False, indent=4)

        if "opening_hours" in result:
            self.opening_hours = result["opening_hours"]

        if "photos" in result:
            self.photos = result["photos"]

        if "international_phone_number" in result:
            self.international_phone_number = result["international_phone_number"]

        if "name" in result:
            self.name = result["name"]

        if "formatted_address" in result:
            self.address = result["formatted_address"]

        if "price_level" in result:
            self.price_level = result["price_level"]

        if "rating" in result:
            self.rating = result["rating"]

        if "reviews" in result:
            self.reviews = result["reviews"]

        if "user_ratings_total" in result:
            self.user_ratings_total = result["user_ratings_total"]

        if "website" in result:
            self.website = result["website"]
        else:
            self.website = DEFAULT_WEBSITE

        return True

class Photo:
    """Class that stores all the information about a photo of a facility"""
    #MAX_WIDTH = 764
    MAX_WIDTH = 700

    ENDPOINTS = {
        "base": "https://maps.googleapis.com/maps/api/place/photo?",
        "maxwidth": "maxwidth={}",
        "photoreference": "&photoreference={}",
        "key": "&key={}"
    }

    def __init__(self, height, width, photo_reference, html_attributions):
        self.maxwidth = min(min(height, width), Photo.MAX_WIDTH)
        self.photo_reference = photo_reference
        self.html_attributions = html_attributions
        self.create_photo_path()
        self.parse_attribution()

    def create_photo_path(self):
        self.path = Photo.ENDPOINTS["base"] + \
                    Photo.ENDPOINTS["maxwidth"].format(self.maxwidth) + \
                    Photo.ENDPOINTS["photoreference"].format(self.photo_reference) + \
                    Photo.ENDPOINTS["key"].format(API_KEY)

        return self.path

    def parse_attribution(self):
        self.authors = []
        self.url = "https://bot-appetit.com"
        if len(self.html_attributions) == 0:
            self.authors.append("unknown")
            return
        for attrib in self.html_attributions:
            url_tokens = attrib.split("\"")
            self.url = url_tokens[1]
            name_tokens = attrib.split(">")
            name_tokens = name_tokens[1].split("<")
            self.authors.append(name_tokens[0])


    def retrieve(self):
        return requests.get(self.path)

class MessengerUtil:
    """Class that stores util fields and methods for posting messages to
    Facebook Messenger"""

    MAX_PHOTOS = 10
    MAPS_ENDPOINTS = "https://www.google.com/maps/search/?api=1&query={}&query_place_id={}"


    @staticmethod
    def create_template_button_url(title, url):
        return {
            "type": "web_url",
            "title": title,
            "url": url
        }

    @staticmethod
    def create_template_button_postback(title, payload):
        return {
            "type": "postback",
            "title": title,
            "payload": payload,
        }

    @staticmethod
    def create_buttons(website, postback_payload):
        buttons = []
        if website != DEFAULT_WEBSITE and website[:5] == DEFAULT_PROTOCOL:
            url_button = MessengerUtil.create_template_button_url(title="view website",
                                                                  url=website)
            buttons.append(url_button)
        postback_button = MessengerUtil.create_template_button_postback(title="more details",
                                                                        payload=postback_payload)
        buttons.append(postback_button)
        return buttons

    @staticmethod
    def create_default_action(type, url):
        return {
            "type": type,
            "url": url,
            "webview_height_ratio": "tall",
        }

    @staticmethod
    def create_template_element(title, image_url, subtitle, default_action, buttons):
        if len(buttons) == 0:
            return {
                "title": title,
                "image_url": image_url,
                "subtitle": subtitle,
                "default_action": default_action,
            }
        return {
            "title": title,
            "image_url": image_url,
            "subtitle": subtitle,
            "default_action": default_action,
            "buttons": buttons
        }

    @staticmethod
    def create_elements(photos, buttons, title, place_id, facility_type):
        elements = []

        for photo in photos:
            default_action = MessengerUtil.create_default_action(type="web_url",
                                                                 url=MessengerUtil.MAPS_ENDPOINTS.format(facility_type, place_id))

            if photo == NO_PHOTO:
                element = MessengerUtil.create_template_element(title=title,
                                                                image_url="",
                                                                subtitle="",
                                                                default_action=default_action,
                                                                buttons=buttons)
            else:
                subtitle = "powered by Google \nphoto author: "
                for author in photo.authors:
                    subtitle += author + " "
                    element = MessengerUtil.create_template_element(title=title,
                                                                    image_url=photo.path,
                                                                    subtitle=subtitle,
                                                                    default_action=default_action,
                                                                    buttons=buttons)
            elements.append(element)

        return elements


    @staticmethod
    def create_template_message(template_type, elements):
        return {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": template_type,
                    "image_aspect_ratio": "square",
                    "elements": elements
                }
            }
        }

class GetFacilityTypeAction(Action):
    """This action class allows to display buttons for each facility type
    for the user to chose from to fill the facility_type entity slot."""

    def name(self) -> Text:
        """Unique identifier of the action"""

        return "get_facility_type_action"

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
                {"title": "{}".format(facility_type.get("name").title() + " " +
                                      facility_type.get("emoji")),
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

class FindFacilitiesAction(Action):
    MAX_FACILITIES = 10

    @staticmethod
    def _resolve_name(facility_types, resource) -> Text:
        for key, value in facility_types.items():
            if value.get("name") == resource:
                return value.get("name")
        return ""

    @staticmethod
    def _create_path(query: Text, type: Text) -> Text:
        """Creates a path to find provider using the endpoints."""
        return TEXTSEARCH_ENDPOINTS["base"] + \
               TEXTSEARCH_ENDPOINTS["query"].format(query) + \
               TEXTSEARCH_ENDPOINTS["key"].format(API_KEY) + \
               TEXTSEARCH_ENDPOINTS["type"].format(type)

    @staticmethod
    def _find_facilities(query: Text, type: Text) -> List[Dict]:
        """Returns json of facilities matching the search criteria."""

        full_path = FindFacilitiesAction._create_path(query, type)

        print("Full path:")
        print(full_path)

        results = requests.get(full_path).json()
        return results['results']

    def name(self) -> Text:
        return "find_facilities_action"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        location = tracker.get_slot('location')
        facility_type = tracker.get_slot('facility_type')

        results = FindFacilitiesAction._find_facilities(location, facility_type)
        button_name = FindFacilitiesAction._resolve_name(FACILITY_TYPES, facility_type)
        if len(results) == 0:
            dispatcher.utter_message(
                "Sorry, we could not find a {} in {}.".format(button_name,
                                                              location.title()))
            return []

        #rating_sorted_results = sorted(results, key=itemgetter('rating'), reverse=True)

        max_facilities = min(FindFacilitiesAction.MAX_FACILITIES, len(results))
        elements=[]
        for facility in results[:max_facilities]:
            name = facility["name"]
            place_id = facility["place_id"]
            payload = "/inform{\"place_id\":\"" + place_id + "\", \"facility_name\":\"" + name + "\"}"

            if "photos" in facility and len(facility["photos"]) > 0:
                facility_photo = facility["photos"][0]

                photo = Photo(height=facility_photo["height"],
                              width=facility_photo["width"],
                              photo_reference=facility_photo["photo_reference"],
                              html_attributions=facility_photo["html_attributions"])
            else:
                photo = NO_PHOTO

            buttons = MessengerUtil.create_buttons(DEFAULT_WEBSITE, payload)
            element = MessengerUtil.create_elements(title=name,
                                                    place_id=place_id,
                                                    facility_type=facility_type,
                                                    photos=[photo],
                                                    buttons=buttons)
            elements.append(element[0])

        facilities_template = MessengerUtil.create_template_message(template_type="generic",
                                                                    elements=elements)

        if max_facilities == 1:
            present_facilities_message = "Here is a {} near you:".format(facility_type)
        else:
            present_facilities_message = "Here are {} {}s near you:".format(max_facilities,
                                                                            facility_type)

        dispatcher.utter_message(present_facilities_message)
        dispatcher.utter_message(json_message=facilities_template)
        return []
        """

        buttons = []
        # limit number of results to 3 for clear presentation purposes
        max_facilities = min(FindFacilitiesAction.MAX_FACILITIES, len(results))
        for r in results[:3]:
            name = r["name"]
            place_id = r["place_id"]
            payload = "/inform{\"place_id\":\"" + place_id + "\", \"facility_name\":\"" + name + "\"}"
            buttons.append(
                {"title": "{}".format(name), "payload": payload})
        if len(buttons) == 1:
            message = "Here is a {} near you:".format(button_name)
        else:
            message = "Here are {} {}s near you:".format(len(buttons),
                                                         button_name)
        dispatcher.utter_message(text=message, buttons=buttons)
        return []
        """

class DetailsForm(FormAction):
    """This form class retrieves the address of the user's
    eating facility choice to display it to the user."""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "details_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
            """A list of required slots that the form has to fill"""

            return ["facility_type", "place_id", "location", "facility_name"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"facility_type": self.from_entity(entity="facility_type",
                                                  intent=["inform",
                                                          "search_provider"]),
                "place_id": self.from_entity(entity="place_id",
                                                  intent=["inform",
                                                          "search_provider"]),
                "location": self.from_entity(entity="location",
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
        place_id = tracker.get_slot("place_id")
        location = tracker.get_slot("location")
        facility_name = tracker.get_slot("facility_name")

        message = "I am now searching for details for the {} {}".format(facility_name, facility_type)
        dispatcher.utter_message(message)
        return []

class GetDetailsAction(Action):
    def name(self) -> Text:
        return "get_details_action"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        facility_type = tracker.get_slot("facility_type")
        place_id = tracker.get_slot("place_id")
        location = tracker.get_slot("location")
        facility_name = tracker.get_slot("facility_name")

        #place_id = "ChIJIYW2hE3_sUARwjQv-T-KZh0"
        details = Details(place_id)
        success = details.retrieve()

        if success is True:
            return [SlotSet("facility_details", details.__dict__)]
        else:
            print("No address found. Most likely this action was executed "
                  "before the user choose a eating facility from the "
                  "provided list. "
                  "If this is a common problem in your dialogue flow,"
                  "using a form instead for this action might be appropriate.")

            dispatcher.utter_message("Sorry I couldn't find details for {}".format(facility_name))
            return [SlotSet("facility_details", "No details")]

class PhotosAction(Action):

    def name(self) -> Text:
        return "photos_action"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        facility_details = tracker.get_slot("facility_details")
        if facility_details is None:
            error_message = "You have to choose a facility first"
            dispatcher.utter_message(error_message)
            return []

        place_id = tracker.get_slot("place_id")
        location = tracker.get_slot("location")
        facility_name = tracker.get_slot("facility_name")
        facility_type = tracker.get_slot("facility_type")

        photos = []
        photo_counter = 0
        for photo in facility_details["photos"]:
            if photo_counter == MessengerUtil.MAX_PHOTOS:
                break
            photo_counter += 1

            photo_obj = Photo(height=photo["height"],
                              width=photo["width"],
                              photo_reference=photo["photo_reference"],
                              html_attributions=photo["html_attributions"])

            photos.append(photo_obj)

        message = "Here are some photos for {} in {}".format(facility_name, location)
        dispatcher.utter_message(message)

        buttons=[]
        elements = MessengerUtil.create_elements(title=facility_details["name"],
                                                 place_id=place_id,
                                                 facility_type=facility_type,
                                                 photos=photos,
                                                 buttons=buttons)
        template = MessengerUtil.create_template_message(template_type="generic",
                                                         elements=elements)

        dispatcher.utter_message(json_message=template)
        return []

PRICELEVEL_DICT = {
    "name": "price_level",
    "ui_name": "price level",
    "messages": {
        4: "This place is considered very expensive",
        3: "Expensive prices here",
        2: "Moderate pricing for this place",
        1: "This place is rather inexpensive",
        0: "Looks like this place is free",
        -1: "Seems like no information could be found for the price level",
    },
    "emoji": EMOJIES["money"],
}


class PriceLevelAction(Action):
    def name(self) -> Text:
        return "price_level_action"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:
        facility_details = tracker.get_slot("facility_details")

        if facility_details is None:
            error_message = "You have to choose a facility first"
            dispatcher.utter_message(error_message)
            return []

        price_level = PRICELEVEL_DICT.get("name")
        if price_level in facility_details:
            value = facility_details[price_level]
            message = value * PRICELEVEL_DICT.get("emoji") + " " + \
                      PRICELEVEL_DICT.get("messages")[value]
        else:
            message = PRICELEVEL_DICT.get("messages")[-1]
        dispatcher.utter_message(message)
        return []

ATMOSPHERE_DICT = {
    "name": "rating",
    "ui_name": "rating",
    "messages": {
        5: "Perfect rating\n{}",
        4: "Check this high rating out\n{}",
        3: "This is a medium rated facility\n{}",
        2: "The rating is\n{}",
        1: "The rating is\n{}",
        -1: "Oops! Couldn't find information about the rating :/",
    },
    "emoji": EMOJIES["star"],
}

class AtmosphereAction(Action):
    def name(self) -> Text:
        return "atmosphere_action"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        facility_details = tracker.get_slot("facility_details")
        if facility_details is None:
            error_message = "You have to choose a facility first"
            dispatcher.utter_message(error_message)
            return []

        facility_type = tracker.get_slot("facility_type")
        rating = ATMOSPHERE_DICT.get("name")
        if rating in facility_details:
            value = facility_details[rating]
            message = round(value) * ATMOSPHERE_DICT.get("emoji") + " " + \
                      ATMOSPHERE_DICT.get("messages")[math.floor(value)].format(value)
        else:
            message = ATMOSPHERE_DICT.get("messages")[-1]
        dispatcher.utter_message(message)
        return []

PHONE_DICT = {
    "name": "international_phone_number",
    "ui_name": "phone",
    "messages": {
        3: "This is the phone number for this place\n{}",
        2: "Call them to see what's new\n{}",
        1: "Reach out on the phone\n{}",
        -1: "Yikes! Those guys don't have a phone maybe? " + EMOJIES["sweat_smile"],
    },
    "emoji": EMOJIES["phone"],
}

class PhoneAction(Action):
    def name(self) -> Text:
        return "phone_action"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        facility_details = tracker.get_slot("facility_details")
        if facility_details is None:
            error_message = "You have to choose a facility first"
            dispatcher.utter_message(error_message)
            return []

        facility_type = tracker.get_slot("facility_type")
        phone = PHONE_DICT.get("name")
        if phone in facility_details:
            value = facility_details[phone]
            msg_pos = random.randint(1, 3)
            message = PHONE_DICT.get("emoji") + " " + \
                      PHONE_DICT.get("messages")[msg_pos].format(value)
        else:
            message = PHONE_DICT.get("messages")[-1]

        dispatcher.utter_message(message)
        return []

WEBSITE_DICT = {
    "name": "website",
    "ui_name": "website",
    "messages": {
        3: "See what they have to offer on their website\n{}",
        2: "Check their website\n{}",
        1: "You can find more details on\n{}",
        -1: "Yikes! Those guys don't have a website maybe?" + EMOJIES["thinking_face"],
    },
    "emoji": EMOJIES["world"],
}

class WebsiteAction(Action):


    def name(self) -> Text:
        return "website_action"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        facility_details = tracker.get_slot("facility_details")
        if facility_details is None:
            error_message = "You have to choose a facility first"
            dispatcher.utter_message(error_message)
            return []

        facility_type = tracker.get_slot("facility_type")
        website = WEBSITE_DICT.get("name")
        if website in facility_details:
            value = facility_details[website]
            msg_pos = random.randint(1, 3)
            message = WEBSITE_DICT.get("emoji") + " " + \
                      WEBSITE_DICT.get("messages")[msg_pos].format(value)
        else:
            message = WEBSITE_DICT.get("messages")[-1]
        dispatcher.utter_message(message)
        return []

ADDRESS_DICT = {
    "name": "address",
    "ui_name": "address",
    "messages": {
        3: "This is how you get there\n{}",
        2: "This is where the place is located\n{}",
        1: "Here's the address\n{}",
        -1: "I couldn't find the address for this place :/",
    },
    "emoji": EMOJIES["pin"],
}

class AddressAction(Action):
    def name(self) -> Text:
        return "address_action"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        facility_details = tracker.get_slot("facility_details")
        if facility_details is None:
            error_message = "You have to choose a facility first"
            dispatcher.utter_message(error_message)
            return []

        facility_type = tracker.get_slot("facility_type")
        address = ADDRESS_DICT.get("name")
        print(address)
        print(facility_details["address"])
        if address in facility_details:
            value = facility_details[address]
            msg_pos = random.randint(1, 3)
            message = ADDRESS_DICT.get("emoji") + " " + \
                      ADDRESS_DICT.get("messages")[msg_pos].format(value)
        else:
            message = ADDRESS_DICT.get("messages")[-1]
        dispatcher.utter_message(message)
        return []

WEEKDAY_DICT = {
    "name": "weekday_text",
    "ui_name": "opening hours",
    "messages": {
        3: "This are the opening hours for this place\n{}",
        2: "Check the programme\n{}",
        1: "The place is open between these hours\n{}",
        -1: "I wasn't able to find their programme, sorry :(",
    },
    "emoji": EMOJIES["calendar"],
}

OPENNOW_DICT = {
    "name": "open_now",
    "ui_name": "open now",
    "messages": {
        2: "The place is open now! ;)",
        1: "Seems they are closed now... :/",
        -1: "I don't know whether they are open or not. Missed maths class " + EMOJIES["laughing_face"],
    }
}

class ScheduleAction(Action):
    def name(self) -> Text:
        return "schedule_action"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        facility_details = tracker.get_slot("facility_details")
        if facility_details is None:
            error_message = "You have to choose a facility first"
            dispatcher.utter_message(error_message)
            return []

        facility_type = tracker.get_slot("facility_type")
        weekday = WEEKDAY_DICT.get("name")
        if weekday in facility_details["opening_hours"]:
            value = facility_details["opening_hours"][weekday]
            weekday_text = ""
            for day in value:
                weekday_text += day + "\n"
            msg_pos = random.randint(1, 3)
            message = WEEKDAY_DICT.get("emoji") + " " + \
                      WEEKDAY_DICT.get("messages")[msg_pos].format(weekday_text)
        else:
            message = WEEKDAY_DICT.get("messages")[-1]

        dispatcher.utter_message(message)

        open_now = OPENNOW_DICT.get("name")
        if open_now in facility_details["opening_hours"]:
            value = facility_details["opening_hours"][open_now]
            if value is True:
                message = OPENNOW_DICT.get("messages")[2]
            else:
                message = OPENNOW_DICT.get("messages")[1]
        else:
            message = OPENNOW_DICT.get("messages")[-1]

        dispatcher.utter_message(message)
        return []

class MoreResultsAction(Action):
    def name(self) -> Text:
        return "more_results_action"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        #facility_details = tracker.get_slot("facility_details")

        #facility_type = tracker.get_slot("facility_type")
        message = "This feature is currently under development. :/"
        dispatcher.utter_message(message)
        return []

class HelpAction(Action):
    def name(self) -> Text:
        return "help_action"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        message = "Here to help. First, you can choose a facility. After " + \
                  "that I  can show you more details like price level, " + \
                  "address, rating, phone, website, you just have to ask. ;) " + \
                  "If I ever get stuck, restart me by typing 'restart'."
        dispatcher.utter_message(message)
        return []

class ActionRestart(Action):
    def name(self) -> Text:
        return "action_restart"

    def run(self, dispatcher, tracker, domain):
        message = "Ok, I am now restarting"
        dispatcher.utter_message(message)
        return[AllSlotsReset(), Restarted()]
