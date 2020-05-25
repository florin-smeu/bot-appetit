curl -X POST -H "Content-Type: application/json" -d '{
  "recipient":{
    "id":"FIND ID FROM RASA X"
  },
  "message":{
    "attachment":{
      "type":"template",
      "payload":{
        "template_type":"generic",
        "elements":[
           {
            "title":"Welcome!",
            "image_url":"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=CmRaAAAAU-VUhh7xh4VAW1P8rLKGji5WjqcguRAws_cdShZk-xjeihx8VHsUkHNCtXV1T8PBEqp9zNB5WLsnwvaMM0fcy-firLF4sQoy2P77pecyC15iW9NI4T-kEEcUdmcCxyMBEhDJrbIK1wS7Gj2oYfufOM_hGhRVDgCHx0QziTii0t5sEKjoBFlwRQ&key=INSERT_API_KEY",
            "subtitle":"We have the right hat for everyone.",
            "default_action": {
              "type": "web_url",
              "url": "https://petersfancybrownhats.com/view?item=103",
              "webview_height_ratio": "tall",
            },
            "buttons":[
              {
                "type":"web_url",
                "url":"https://petersfancybrownhats.com",
                "title":"View Website"
              },{
                "type":"postback",
                "title":"Start Chatting",
                "payload":"DEVELOPER_DEFINED_PAYLOAD"
              }
            ]
          },
	  {
            "title":"Hi!",
            "image_url":"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=CmRaAAAAU-VUhh7xh4VAW1P8rLKGji5WjqcguRAws_cdShZk-xjeihx8VHsUkHNCtXV1T8PBEqp9zNB5WLsnwvaMM0fcy-firLF4sQoy2P77pecyC15iW9NI4T-kEEcUdmcCxyMBEhDJrbIK1wS7Gj2oYfufOM_hGhRVDgCHx0QziTii0t5sEKjoBFlwRQ&key=INSERT_API_KEY",
            "subtitle":"We have the right hat for everyone.",
            "default_action": {
              "type": "web_url",
              "url": "https://petersfancybrownhats.com/view?item=103",
              "webview_height_ratio": "tall",
            },
            "buttons":[
              {
                "type":"web_url",
                "url":"https://petersfancybrownhats.com",
                "title":"View Website"
              },{
                "type":"postback",
                "title":"Start Chatting",
                "payload":"DEVELOPER_DEFINED_PAYLOAD"
              }
            ]
          }
        ]
      }
    }
  }
}' "https://graph.facebook.com/v2.6/me/messages?access_token=EAADjMOUraYABALLFWrrSgSb61jsUubjscygUUUBOTAl7VZAdd7pitmEfUTydxGcDCfm8xqX8ioZClvwzIKpJzTG31dH6kixKPEAzJ7Na7lETl7IQ5olXKVWhk0iwAT16RC76oQZCscIttfTSbGFguUDFXyofo2DzVZAbmkH4ZAQZDZD"
