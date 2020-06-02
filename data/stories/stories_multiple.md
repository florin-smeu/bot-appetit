## multiple affirm
> details_done
* search_provider{"facility_type": "facility_foo"}
    - utter_ask_correct_params
* affirm
    - find_facilities_action
* inform{"place_id": "ChIJ0wYwUjD_sUAR3d-lY7wFbg8", "facility_name": "Noeme - former GUXT"}
    - slot{"facility_name": "Noeme - former GUXT"}
    - slot{"place_id": "ChIJ0wYwUjD_sUAR3d-lY7wFbg8"}
    - details_form
    - form{"name": "details_form"}
    - slot{"facility_type": "restaurant"}
    - slot{"place_id": "ChIJ0wYwUjD_sUAR3d-lY7wFbg8"}
    - slot{"location": "Bucharest Romania"}
    - slot{"facility_name": "Noeme - former GUXT"}
    - slot{"place_id": "ChIJ0wYwUjD_sUAR3d-lY7wFbg8"}
    - slot{"facility_name": "Noeme - former GUXT"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - get_details_action
    - slot{"facility_details": "foo_details"}
    - photos_action
    - address_action

## multiple deny
> details_done
* search_provider{"facility_type": "facility_foo"}
    - utter_ask_correct_params
* deny
    - utter_ask_location
* inform{"location":"location_foo"}
    - slot{"loaction": "location_foo"}
    - find_facilities_action
* inform{"place_id": "ChIJ0wYwUjD_sUAR3d-lY7wFbg8", "facility_name": "Noeme - former GUXT"}
    - slot{"facility_name": "Noeme - former GUXT"}
    - slot{"place_id": "ChIJ0wYwUjD_sUAR3d-lY7wFbg8"}
    - details_form
    - form{"name": "details_form"}
    - slot{"facility_type": "restaurant"}
    - slot{"place_id": "ChIJ0wYwUjD_sUAR3d-lY7wFbg8"}
    - slot{"location": "Bucharest Romania"}
    - slot{"facility_name": "Noeme - former GUXT"}
    - slot{"place_id": "ChIJ0wYwUjD_sUAR3d-lY7wFbg8"}
    - slot{"facility_name": "Noeme - former GUXT"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - get_details_action
    - slot{"facility_details": "foo_details"}
    - photos_action
    - address_action
