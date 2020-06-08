## specific facility after printed facilities name type
> printed_facilities
* ask_specific_facility{"facility_name":"foo_name", "facility_type":"foo_facility_type"}
    - slot{"facility_name": "foo_name"}
    - slot{"facility_type": "foo_facility_type"}
    - get_specific_facility_action
    - slot {"place_id": "foo_place_id"}
    - get_details_action
    - slot{"facility_details": "foo_details"}
    - photos_action
    - address_action
    - utter_ask_more
    > printed_details

## specific facility after printed details name type
> printed_details
* ask_specific_facility{"facility_name":"foo_name", "facility_type":"foo_facility_type"}
    - slot{"facility_name": "foo_name"}
    - slot{"facility_type": "foo_facility_type"}
    - get_specific_facility_action
    - slot {"place_id": "foo_place_id"}
    - get_details_action
    - slot{"facility_details": "foo_details"}
    - photos_action
    - address_action
    - utter_ask_more
    - printed_details

## specific facility after detail asked name type
> detail_asked
* ask_specific_facility{"facility_name":"foo_name", "facility_type":"foo_facility_type"}
    - slot{"facility_name": "foo_name"}
    - slot{"facility_type": "foo_facility_type"}
    - get_specific_facility_action
    - slot {"place_id": "foo_place_id"}
    - get_details_action
    - slot{"facility_details": "foo_details"}
    - photos_action
    - address_action
    - utter_ask_more
    - printed_details

################################################################################

## specific facility after printed facilities name
> printed_facilities
* ask_specific_facility{"facility_name":"foo_name"}
    - slot{"facility_name": "foo_name"}
    - get_specific_facility_action
    - slot {"place_id": "foo_place_id"}
    - get_details_action
    - slot{"facility_details": "foo_details"}
    - photos_action
    - address_action
    - utter_ask_more
    > printed_details

## specific facility after printed details name
> printed_details
* ask_specific_facility{"facility_name":"foo_name"}
    - slot{"facility_name": "foo_name"}
    - get_specific_facility_action
    - slot {"place_id": "foo_place_id"}
    - get_details_action
    - slot{"facility_details": "foo_details"}
    - photos_action
    - address_action
    - utter_ask_more
    - printed_details

## specific facility after detail asked name
> detail_asked
* ask_specific_facility{"facility_name":"foo_name"}
    - slot{"facility_name": "foo_name"}
    - get_specific_facility_action
    - slot {"place_id": "foo_place_id"}
    - get_details_action
    - slot{"facility_details": "foo_details"}
    - photos_action
    - address_action
    - utter_ask_more
    - printed_details

################################################################################
################################################################################

## specific facility after printed facilities name type
* ask_specific_facility{"facility_name":"foo_name", "facility_type":"foo_facility_type"}
    - slot{"facility_name": "foo_name"}
    - utter_sorry_specific

## specific facility after printed details name type
* ask_specific_facility{"facility_name":"foo_name", "facility_type":"foo_facility_type"}
    - slot{"facility_name": "foo_name"}
    - utter_sorry_specific

## specific facility after detail asked name type
* ask_specific_facility{"facility_name":"foo_name", "facility_type":"foo_facility_type"}
    - slot{"facility_name": "foo_name"}
    - utter_sorry_specific

################################################################################

## specific facility after printed facilities name
* ask_specific_facility{"facility_name":"foo_name"}
    - slot{"facility_name": "foo_name"}
    - utter_sorry_specific

## specific facility after printed details name
* ask_specific_facility{"facility_name":"foo_name"}
    - slot{"facility_name": "foo_name"}
    - utter_sorry_specific

## specific facility after detail asked name
* ask_specific_facility{"facility_name":"foo_name"}
    - slot{"facility_name": "foo_name"}
    - utter_sorry_specific
