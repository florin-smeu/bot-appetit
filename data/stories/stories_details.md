## ask price
> printed_details
* ask_price
    - price_level_action
> detail_asked

## ask atmosphere with reviews
> printed_details
* ask_atmosphere
    - atmosphere_action
    - utter_ask_reviews
* affirm
    - review_summary_action
> detail_asked

## ask atmosphere without reviews
> printed_details
* ask_atmosphere
    - atmosphere_action
    - utter_ask_reviews
* deny
    - utter_ok
> detail_asked


## ask phone
> printed_details
* ask_phone
    - phone_action
> detail_asked

## ask website
> printed_details
* ask_website
    - website_action
> detail_asked

## ask address
> printed_details
* ask_address
    - address_action
> detail_asked

## ask schedule
> printed_details
* ask_schedule
    - schedule_action
> detail_asked

## ask photos
> printed_details
* ask_photos
    - photos_action
> detail_asked
