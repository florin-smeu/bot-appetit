## multiple affirm after printed details type
> printed_details
* search_provider{"facility_type": "facility_foo"}
    - slot{"facility_type": "facility_foo"}
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
    - utter_ask_more

## multiple deny after printed details type
> printed_details
* search_provider{"facility_type": "facility_foo"}
    - slot{"facility_type": "facility_foo"}
    - utter_ask_correct_params
* deny
    - utter_ask_location
* inform{"location":"location_foo"}
    - slot{"location": "location_foo"}
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
    - utter_ask_more

## multiple affirm after detail asked type
> detail_asked
* search_provider{"facility_type": "facility_foo"}
    - slot{"facility_type": "facility_foo"}
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
    - utter_ask_more

## multiple deny after detail asked type
> detail_asked
* search_provider{"facility_type": "facility_foo"}
    - slot{"facility_type": "facility_foo"}
    - utter_ask_correct_params
* deny
    - utter_ask_location
* inform{"location":"location_foo"}
    - slot{"location": "location_foo"}
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
    - utter_ask_more

## multiple affirm after printed details type location
> printed_details
* search_provider{"facility_type": "facility_foo", "location": "foo_location"}
    - slot{"facility_type": "facility_foo"}
    - slot{"location": "foo_location"}
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
    - utter_ask_more

## multiple deny after printed details type location
> printed_details
* search_provider{"facility_type": "facility_foo", "location": "foo_location"}
    - slot{"facility_type": "facility_foo"}
    - slot{"location": "foo_location"}
    - utter_ask_correct_params
* deny
    - utter_ask_location_and_type
* inform{"location":"location_foo", "facility_type": "foo_facility_type"}
    - slot{"location": "location_foo"}
    - slot{"facility_type": "foo_facility_type"}
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
    - utter_ask_more

## multiple affirm after detail asked type location
> detail_asked
* search_provider{"facility_type": "facility_foo", "location": "foo_location"}
    - slot{"facility_type": "facility_foo"}
    - slot{"location": "foo_location"}
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
    - utter_ask_more

## multiple deny after detail asked type location
> detail_asked
* search_provider{"facility_type": "facility_foo", "location": "foo_location"}
    - slot{"facility_type": "facility_foo"}
    - slot{"location": "foo_location"}
    - utter_ask_correct_params
* deny
    - utter_ask_location_and_type
* inform{"location":"location_foo", "facility_type": "foo_facility_type"}
    - slot{"location": "location_foo"}
    - slot{"facility_type": "foo_facility_type"}
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
    - utter_ask_more
