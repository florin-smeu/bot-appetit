##### TODO UPDATE STORIES !!!!!!!!

## story_thank_you
* thanks
  - utter_noworries
  - action_slot_reset
  - action_restarted

## story_goodbye
* goodbye
  - utter_goodbye
  - action_slot_reset
  - action_restarted

## story_get_address
* greet
    - find_facility_types
* inform{"facility_type": "restaurant"}
    - slot{"facility_type": "restaurant"}
    - facility_form
    - form{"name": "facility_form"}
    - slot{"facility_type": "restaurant"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "foo_location"}
    - slot{"location": "foo_location"}
    - form: facility_form
    - slot{"location": "foo_location"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - facility_action
* inform{"place_id": "foo_id", "facility_name": "foo_name"}
    - slot{"place_id": "foo_id"}
    - slot{"facility_name": "foo_name"}
    - details_form
    - form{"name": "details_form"}
    - slot{"facility_type": "restaurant"}
    - slot{"place_id": "foo_id"}
    - slot{"facility_name": "foo_name"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - details_action
    - slot{"facility_details": "foo_details"}
    - photos_action
    - provide_details_action
    - action_slot_reset
    - action_restarted

## story_get_address_provided_facility_type
* search_provider{"facility_type": "restaurant"}
    - slot{"facility_type": "restaurant"}
    - facility_form
    - form{"name": "facility_form"}
    - slot{"facility_type": "restaurant"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "foo_location"}
    - slot{"location": "foo_location"}
    - form: facility_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - facility_action
* inform{"place_id": "foo_id", "facility_name": "foo_name"}
    - slot{"place_id": "foo_id"}
    - slot{"facility_name": "foo_name"}
    - details_form
    - form{"name": "details_form"}
    - slot{"facility_type": "restaurant"}
    - slot{"place_id": "foo_id"}
    - slot{"facility_name": "foo_name"}
    - slot{"location": "foo_location"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - details_action
    - slot{"facility_details": "foo_details"}
    - photos_action
    - provide_details_action
    - action_slot_reset
    - action_restarted

## story_get_address_provided_facility_type_and_location
* search_provider{"facility_type": "restaurant", "location": "foo_location"}
    - slot{"facility_type": "restaurant"}
    - slot{"location": "foo_location"}
    - facility_form
    - form{"name": "facility_form"}
    - slot{"facility_type": "restaurant"}
    - slot{"location": "foo_location"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - facility_action
* inform{"place_id": "foo_id", "facility_name": "foo_name"}
    - slot{"place_id": "foo_id"}
    - slot{"facility_name": "foo_name"}
    - details_form
    - form{"name": "details_form"}
    - slot{"facility_type": "restaurant"}
    - slot{"place_id": "foo_id"}
    - slot{"facility_name": "foo_name"}
    - slot{"location": "foo_location"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - details_action
    - slot{"facility_details": "foo_details"}
    - photos_action
    - provide_details_action
    - action_slot_reset
    - action_restarted

## story_get_address_provided_facility_type_and_location_and_place_id
* search_provider{"facility_type": "restaurant", "place_id": "foo_id", "place_id": "foo_name", "location": "foo_location"}
  - slot{"place_id": "foo_id"}
  - slot{"facility_name": "foo_name"}
    - slot{"facility_type": "restaurant"}
    - slot{"location": "foo_location"}
    - details_action
    - slot{"facility_details": "foo_details"}
    - photos_action
    - provide_details_action
    - action_slot_reset
    - action_restarted
