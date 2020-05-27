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
* inform{"facility_name": "Pizzeria Volare"}
    - slot{"facility_name": "Pizzeria Volare"}
    - details_form
    - form{"name": "details_form"}
    - slot{"facility_type": "restaurant"}
    - slot{"facility_name": "Pizzeria Volare"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - details_action
    - slot{"facility_address": "Parter, Calea Văcărești 203B, București, Romania"}
    - photos_action
    - utter_address
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
* inform{"facility_name": "Le Bab"}
    - slot{"facility_name": "Le Bab"}
    - details_form
    - form{"name": "details_form"}
    - slot{"facility_type": "restaurant"}
    - slot{"facility_name": "Le Bab"}
    - slot{"location": "Calea Victoriei Bucharest"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - details_action
    - slot{"facility_address": "Calea Victoriei 12A, București 030026, Romania"}
    - photos_action
    - utter_address
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
* inform{"facility_name": "Restaurant Vulturul S.R.L."}
    - slot{"facility_name": "Restaurant Vulturul S.R.L."}
    - details_form
    - form{"name": "details_form"}
    - slot{"facility_type": "restaurant"}
    - slot{"facility_name": "Restaurant Vulturul S.R.L."}
    - slot{"location": "Lujerului Bucharest"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - details_action
    - slot{"facility_address": "Intrarea Blejoi nr. 2, Bulevardul Iuliu Maniu 408-410, București 062391, Romania"}
    - photos_action
    - utter_address
    - action_slot_reset
    - action_restarted

## story_get_address_provided_facility_type_and_location_and_facility_name
* search_provider{"facility_type": "restaurant", "facility_name": "Capsa", "location": "Bucharest"}
    - slot{"facility_name": "Capsa"}
    - slot{"facility_type": "restaurant"}
    - slot{"location": "Bucharest"}
    - details_action
    - slot{"facility_address": "Calea Victoriei 36, București 030167, Romania"}
    - photos_action
    - utter_address
    - action_slot_reset
    - action_restarted
