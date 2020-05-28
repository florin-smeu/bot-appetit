import requests
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from typing import Dict, Text, Any, List

from operator import itemgetter

from rasa_sdk import Action
from rasa_sdk.events import SlotSet, FollowupAction, Restarted, AllSlotsReset
from rasa_sdk.forms import FormAction

import json




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


class MessengerUtil:
    """Class that stores util fields and methods for posting messages to
    Facebook Messenger"""

    MAX_PHOTOS = 4

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
    def create_buttons(website):
        buttons = []
        if website is not None:
            url_button = MessengerUtil.create_template_button_url("view website", website)
            buttons.append(url_button)
        postback_button = MessengerUtil.create_template_button_postback("more details", "DEVELOPER_DEFINED_PAYLOAD")
        buttons.append(postback_button)
        return buttons

    @staticmethod
    def create_default_action(type, url):
        return {
            "type": type,
            "url": "https://bot-appetit.com",
            "webview_height_ratio": "tall",
        }

    @staticmethod
    def create_template_element(title, image_url, subtitle, default_action, buttons):
        return {
            "title": title,
            "image_url": image_url,
            "subtitle": subtitle,
            "default_action": default_action,
            "buttons": buttons
        }

    @staticmethod
    def create_elements(photo_paths, default_action, buttons):
        elements = []
        for photo_path in photo_paths:
            element = create_template_element(title="title",
                                              image_url=photo_path,
                                              subtitle="subtitle",
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
                    "elements": elements
                }
            }
        }


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
