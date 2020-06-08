## ask price
> details_done
* ask_price
    - price_level_action
> detail_asked

## ask atmosphere with reviews
> details_done
* ask_atmosphere
    - atmosphere_action
    - utter_ask_reviews
* affirm
    - review_summary_action
> detail_asked

## ask atmosphere without reviews
> details_done
* ask_atmosphere
    - atmosphere_action
    - utter_ask_reviews
* deny
    - utter_ok
> detail_asked


## ask phone
> details_done
* ask_phone
    - phone_action
> detail_asked

## ask website
> details_done
* ask_website
    - website_action
> detail_asked

## ask address
> details_done
* ask_address
    - address_action
> detail_asked

## ask schedule
> details_done
* ask_schedule
    - schedule_action
> detail_asked

## ask photos
> details_done
* ask_photos
    - photos_action
> detail_asked


## more results
> details_done
* more_results
    - more_results_action
> detail_asked
