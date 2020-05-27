import requests
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from typing import Dict, Text, Any, List

from operator import itemgetter

from rasa_sdk import Action
from rasa_sdk.events import SlotSet, FollowupAction, Restarted, AllSlotsReset
from rasa_sdk.forms import FormAction

import json


API_KEY = 'AIzaSyAu-uc1As4xBhfge4l_9Aj4qZ-Vh6IJYWg'

class Facility:
    """Wrapper class that encapsulates all  the information about a facility"""
    def __init__(self):
        self.photo_index = 0

    def set_details(self, details):
        self.details = details

    def set_photos(self, photos):
        self.photos = photos


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

        return True


class Photo:
    """Class that stores all the information about a photo of a facility"""
    #MAX_WIDTH = 764
    MAX_WIDTH = 400

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

    def create_photo_path(self):
        self.path = Photo.ENDPOINTS["base"] + \
                    Photo.ENDPOINTS["maxwidth"].format(self.maxwidth) + \
                    Photo.ENDPOINTS["photoreference"].format(self.photo_reference) + \
                    Photo.ENDPOINTS["key"].format(API_KEY)

        return self.path

    def retrieve(self):
        return requests.get(self.path)




    """def main():
        input_text = input('Search query: ')

        results = _find_facilities(input_text)

        # now x contains list of nested dictionaries
        # we know dictionary contain key value pair
        # store the value of result key in variable y

        # keep looping upto length of y
        #for i in range(len(results)):
        # Print value corresponding to the
        # 'name' key at the ith index of y
        #print(results[i])
        with open("res_api.json", "w") as f:
            json.dump(results, f, ensure_ascii=False, indent=4)

        # Find details about all the facilities
        facilities = []
        for result in results[:1]:
            facility_details = Details(place_id = result["place_id"])
            facility_details.retrieve()
            with open("details" + facility_details.name.replace(" ", "") + ".json", "w") as f:
                json.dump(facility_details.__dict__, f, ensure_ascii=False, indent=4)
            facilities.append(facility_details)

        photos = []
        for facility in facilities[:1]:
            for photo in facility.photos:
                new_photo = Photo(height=photo["height"],
                                  width=photo["width"],
                                  photo_reference=photo["photo_reference"],
                                  html_attributions=photo["html_attributions"])
                photos.append(new_photo)

        for photo in photos:
            path = photo.create_photo_path()
            print(path)


    if __name__ == "__main__":
        main()
    """
