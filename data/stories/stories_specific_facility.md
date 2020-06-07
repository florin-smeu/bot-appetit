## specific facility
* ask_specific_facility{"facility_name":"foo_details", "facility_type":"foo_facility_type"}
    - get_specific_facility_action
    - slot {"place_id": "foo_place_id"}
    - get_details_action
    - slot{"facility_details": "foo_details"}
    - photos_action
    - address_action
    - utter_ask_more
    > details_done
