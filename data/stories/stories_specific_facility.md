## specific facility
> details_done
* ask_specific_facility{"facility_name":"foo_details", "facility_type":"foo_facility_type"}
    - get_specific_facility_action
    - slot {"place_id": "foo_place_id"}
    - get_details_action
    - slot{"facility_details": "foo_details"}
    - photos_action
    - address_action
    - utter_ask_more
    > details_done

## specific facility 2
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
    - slot{"facility_list": "foo_facility_list"}
* ask_specific_facility{"facility_name":"foo_details", "facility_type":"foo_facility_type"}
    - get_specific_facility_action
    - slot {"place_id": "foo_place_id"}
    - get_details_action
    - slot{"facility_details": "foo_details"}
    - photos_action
    - address_action
    - utter_ask_more
    > details_done
