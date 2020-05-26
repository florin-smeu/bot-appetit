## happy_path
* greet
    - find_facility_types
* inform{"facility_type": "restaurant"}    
    - facility_form
    - form{"name": "facility_form"}
    - form{"name": null}
    - facility_action
* inform{"facility_name": "Trattoria 20"}
    - details_form
    - form{"name": "details_form"}
    - form{"name": null}
    - details_action
    - utter_address
    - photo_action
* thanks
    - utter_noworries
* goodbye
    - utter_goodbye


## happy_path_multi_requests
* greet
    - find_facility_types
* inform{"facility_type": "restaurant"}
    - facility_form
    - form{"name": "facility_form"}
    - form{"name": null}
    - facility_action
* inform{"facility_name": "Trattoria 20"}
    - details_form
    - form{"name": "details_form"}
    - form{"name": null}
    - details_action
    - utter_address
    - photo_action
* search_provider{"facility_type": "restaurant"}
    - facility_form
    - form{"name": "facility_form"}
    - form{"name": null}
    - facility_action
* inform{"facility_name": "Trattoria 20"}   
    - details_form
    - form{"name": "details_form"}
    - form{"name": null}
    - details_action
    - utter_address
    - photo_action
## happy_path2
* search_provider{"location": "Austin", "facility_type": "restaurant"}
    - facility_form
    - form{"name": "facility_form"}
    - form{"name": null}
    - facility_action
* inform{"facility_name": "Trattoria 20"}
    - details_form
    - form{"name": "details_form"}
    - form{"name": null}
    - details_action
    - utter_address
    - photo_action
* thanks
    - utter_noworries
* goodbye
    - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## story_thankyou
* thanks
  - utter_noworries
