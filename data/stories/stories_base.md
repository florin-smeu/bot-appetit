## print facilities
* greet
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
    - slot{"facility_list": "foo_facility_list"}
> printed_facilities

## choose facility
> printed_facilities
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
    - utter_ask_more
> printed_details

## thank you
* thanks
    - utter_noworries

## goodbye
* goodbye
    - utter_goodbye

## restart after details done
> printed_details
* restart
    - action_restart
    - utter_init
    - get_facility_type_action

## restart after detail_asked
> detail_asked
* restart
    - action_restart
    - utter_init
    - get_facility_type_action


## help
* ask_help
    - utter_help
