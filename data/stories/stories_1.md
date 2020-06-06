## interactive_story
* greet
    - connect_db_action
    - utter_init
    - get_facility_type_action
* inform{"facility_type": "restaurant"}
    - slot{"facility_type": "restaurant"}
    - facility_form
    - form{"name": "facility_form"}
    - slot{"facility_type": "restaurant"}
    - slot{"facility_type": "restaurant"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Bucharest Romania"}
    - slot{"location": "Bucharest Romania"}
    - form: facility_form
    - slot{"location": "Bucharest Romania"}
    - form{"name": null}
    - slot{"requested_slot": null}
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
    > details_done

## thank you
* thanks
    - utter_noworries

## goodbye
* goodbye
    - utter_goodbye

## restart
* restart
    - action_restart

## help
* ask_help
    - help_action
