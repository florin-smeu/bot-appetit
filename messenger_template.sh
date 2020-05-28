curl -X POST -H "Content-Type: application/json" -d '{
  "recipient":{
    "id":"3099149793483565"
  },
  "message":{
    "attachment": {
    "type": "template",
    "payload": {
      "template_type": "generic",
      "elements": [
        {
          "title": "the ARTIST Restaurant",
          "image_url": "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=CmRaAAAAY7zHTzNiaVrVjR_7eSPwUlwFqUA-6uEFfmDbMe8ja-Oi4vMzmMsLW0hCDGpeTcNUWh6ihkrP60doUlEf-CJZbE-mdApRTSkq4nsy1L7MXXi2bVHWZG6FQJJJyMXMCjbLEhDeSEw4AnfTcVe0XlfOQIYlGhR9v6mNSAMLdT5F2v6Zb3EW-K7oTQ&key=AIzaSyAu-uc1As4xBhfge4l_9Aj4qZ-Vh6IJYWg",
          "subtitle": "powered by Google \nauthor(s): the ARTIST Restaurant ",
          "default_action": {
            "type": "web_url",
            "url": "https://maps.google.com/maps/contrib/117026730578485916496",
            "webview_height_ratio": "tall"
          },
          "buttons": [
            {
              "type": "web_url",
              "title": "view website",
              "url": "http://www.theartist.ro/"
            },
            {
              "type": "postback",
              "title": "more details",
              "payload": "DEVELOPER_DEFINED_PAYLOAD"
            }
          ]
        },
        {
          "title": "the ARTIST Restaurant",
          "image_url": "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=CmRaAAAAHG4PLOBjcCLmRVnFBiP6s4KU_5fOLzP3soVeRoWhfT1a2XFGnux4_KJ9EqnfrmpB9wktEIcgLN_MgNHSRZG9hvdiTINZqQEzRaSF_Yo4NX6Ic-XPbbjvTW8FxjFw4lhMEhBUKOfmd0WGzkCmr07IBeFdGhRWuNwOupwjoUnfgJYE_lu3adwLkQ&key=AIzaSyAu-uc1As4xBhfge4l_9Aj4qZ-Vh6IJYWg",
          "subtitle": "powered by Google \nauthor(s): the ARTIST Restaurant ",
          "default_action": {
            "type": "web_url",
            "url": "https://maps.google.com/maps/contrib/117026730578485916496",
            "webview_height_ratio": "tall"
          },
          "buttons": [
            {
              "type": "web_url",
              "title": "view website",
              "url": "http://www.theartist.ro/"
            },
            {
              "type": "postback",
              "title": "more details",
              "payload": "DEVELOPER_DEFINED_PAYLOAD"
            }
          ]
        },
        {
          "title": "the ARTIST Restaurant",
          "image_url": "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=CmRaAAAAGqrFiVbij0z1hr-zw6CqvDeKruTU98l6FaJCrJQKIOONK7SX-aq1jR9t0HC_q1FW1xezu8vWlgh0MjeJKqvdbe2AjeUFIxDHYtMcp7Q6Yw9z_XSnSgHCH_P-IqpFdRKvEhBW9futnc0mKu7LbKVKcgTmGhQljzRc4xxAmATsXEr5uun4gl7ySQ&key=AIzaSyAu-uc1As4xBhfge4l_9Aj4qZ-Vh6IJYWg",
          "subtitle": "powered by Google \nauthor(s): Stefan Vasilescu ",
          "default_action": {
            "type": "web_url",
            "url": "https://maps.google.com/maps/contrib/106525329119234610863",
            "webview_height_ratio": "tall"
          },
          "buttons": [
            {
              "type": "web_url",
              "title": "view website",
              "url": "http://www.theartist.ro/"
            },
            {
              "type": "postback",
              "title": "more details",
              "payload": "DEVELOPER_DEFINED_PAYLOAD"
            }
          ]
        },
        {
          "title": "the ARTIST Restaurant",
          "image_url": "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=CmRaAAAAixNBDW8bskqpzgzbeVA2GVby0jhZ9bMV6NO0gL_LVDwlpW-L7D7G1H5Scnx1Hdr4P5ShC_IFfilQVgpDFSPVo2_joNU7KzxkeMOlq_06xrM4Ro0uQsLirJudjYv-DbezEhCyBpv2gGosGUjNFgCdsLmVGhRo1VGhLtmbE5eNC0Tq_zGcoXptdA&key=AIzaSyAu-uc1As4xBhfge4l_9Aj4qZ-Vh6IJYWg",
          "subtitle": "powered by Google \nauthor(s): Itai Trigalo ",
          "default_action": {
            "type": "web_url",
            "url": "https://maps.google.com/maps/contrib/106506537563653866371",
            "webview_height_ratio": "tall"
          },
          "buttons": [
            {
              "type": "web_url",
              "title": "view website",
              "url": "http://www.theartist.ro/"
            },
            {
              "type": "postback",
              "title": "more details",
              "payload": "DEVELOPER_DEFINED_PAYLOAD"
            }
          ]
        }
      ]
    }
  }




  }
}' "https://graph.facebook.com/v2.6/me/messages?access_token=EAADjMOUraYABAHMaVf5mgF4ZAGUSZC3JR0z7JL07saxPCWqNAZA1GyQeWrnTf9ISAQ1UPrza0ZByWTSKQK85npv0OwyPFmWJ0jQV4fr1fLQaOGCvcKwkBXkjIpZCsoLiUw8AfKydIJG54Dc3ZCn2V2dZCaQ8p5cV0MZCsTdsJJaxZAAZDZD"
