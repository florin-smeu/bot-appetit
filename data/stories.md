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
* form: inform{"location": "Tineretului"}
    - slot{"location": "Tineretului"}
    - form: facility_form
    - slot{"location": "Tineretului"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - facility_action
* inform{"place_id": "Pizzeria Volare"}
    - slot{"place_id": "Pizzeria Volare"}
    - details_form
    - form{"name": "details_form"}
    - slot{"facility_type": "restaurant"}
    - slot{"place_id": "Pizzeria Volare"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - details_action
    - slot{"facility_details": "Parter, Calea Văcărești 203B, București, Romania"}
    - photos_action
    - utter_details
    - action_slot_reset
    - action_restarted

## story_get_address_provided_facility_type
* search_provider{"facility_type": "restaurant"}
    - slot{"facility_type": "restaurant"}
    - facility_form
    - form{"name": "facility_form"}
    - slot{"facility_type": "restaurant"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Calea Victoriei Bucharest"}
    - slot{"location": "Calea Victoriei Bucharest"}
    - form: facility_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - facility_action
* inform{"place_id": "Le Bab"}
    - slot{"place_id": "Le Bab"}
    - details_form
    - form{"name": "details_form"}
    - slot{"facility_type": "restaurant"}
    - slot{"place_id": "Le Bab"}
    - slot{"location": "Calea Victoriei Bucharest"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - details_action
    - slot{"facility_details": "Calea Victoriei 12A, București 030026, Romania"}
    - photos_action
    - utter_details
    - action_slot_reset
    - action_restarted

## story_get_address_provided_facility_type_and_location
* search_provider{"facility_type": "restaurant", "location": "Lujerului Bucharest"}
    - slot{"facility_type": "restaurant"}
    - slot{"location": "Lujerului Bucharest"}
    - facility_form
    - form{"name": "facility_form"}
    - slot{"facility_type": "restaurant"}
    - slot{"location": "Lujerului Bucharest"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - facility_action
* inform{"place_id": "Restaurant Vulturul S.R.L."}
    - slot{"place_id": "Restaurant Vulturul S.R.L."}
    - details_form
    - form{"name": "details_form"}
    - slot{"facility_type": "restaurant"}
    - slot{"place_id": "Restaurant Vulturul S.R.L."}
    - slot{"location": "Lujerului Bucharest"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - details_action
    - slot{"facility_details": "Intrarea Blejoi nr. 2, Bulevardul Iuliu Maniu 408-410, București 062391, Romania"}
    - photos_action
    - utter_details
    - action_slot_reset
    - action_restarted

## story_get_address_provided_facility_type_and_location_and_place_id
* search_provider{"facility_type": "restaurant", "place_id": "Capsa", "location": "Bucharest"}
    - slot{"place_id": "Capsa"}
    - slot{"facility_type": "restaurant"}
    - slot{"location": "Bucharest"}
    - details_action
    - slot{"facility_details": "Calea Victoriei 36, București 030167, Romania"}
    - photos_action
    - utter_details
    - action_slot_reset
    - action_restarted
