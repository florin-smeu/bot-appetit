curl -X POST -H "Content-Type: application/json" -d '{
  "recipient":{
    "id":"3099149793483565"
  },
  "message":{
    "attachment": {
    "type": "template",
    "payload": {
      "template_type": "generic",
      "image_aspect_ratio": "square",
      "elements": [
        {
          "title": "5ENSI by BeanZ Cafe",
          "image_url": "https://maps.googleapis.com/maps/api/place/photo?maxwidth=700&photoreference=CmRaAAAAit560mIgLrE7pKk0sXhZ-PoWbmGU11MB7FMUxjziaQZSAhWciG5GLBuyX-UCCLTUY8AX5kSHT9Lw4TUxq_zHAXOwxvwV7glfiYEte8QLvd4esilm8jWQUYw8c9xF7RxeEhC5Zr2vojiXMlROd7-dxaCQGhQIWI93KedRVg4S6bMetiHEBj7yKg&key=AIzaSyAu-uc1As4xBhfge4l_9Aj4qZ-Vh6IJYWg",
          "subtitle": "powered by Google \nphoto author: Ioan Cobzarenco ",
          "default_action": {
            "type": "web_url",
            "url": "https://maps.google.com/maps/contrib/109517545881464311326",
            "webview_height_ratio": "tall"
          },
          "buttons": [
            {
              "type": "web_url",
              "title": "view website",
              "url": "https://m.facebook.com/5ENSIbyBeanZCafe/"
            },
            {
              "type": "postback",
              "title": "more details",
              "payload": "DEVELOPER_DEFINED_PAYLOAD"
            }
          ]
        },
        {
          "title": "5ENSI by BeanZ Cafe",
          "image_url": "https://maps.googleapis.com/maps/api/place/photo?maxwidth=700&photoreference=CmRaAAAA_kpbau3xYQk3MIMRo9tgbh4U-DgWE0BngJIfeIEquNxoqoYWxSBugS-_P8N1DLQCmUwJ9SwsmdRcOxRVR2a5Kcx-QvvyouxSJk9an99gzvE-snWyl_moZpKCyAsILI9REhC0MjGavtCzlSOTxakPmKcxGhQxZSLzQQ3lwwgGTE8Gg9J-VNgLYg&key=AIzaSyAu-uc1As4xBhfge4l_9Aj4qZ-Vh6IJYWg",
          "subtitle": "powered by Google \nphoto author: Dumnezeu ",
          "default_action": {
            "type": "web_url",
            "url": "https://maps.google.com/maps/contrib/110622815388718641682",
            "webview_height_ratio": "tall"
          },
          "buttons": [
            {
              "type": "web_url",
              "title": "view website",
              "url": "https://m.facebook.com/5ENSIbyBeanZCafe/"
            },
            {
              "type": "postback",
              "title": "more details",
              "payload": "DEVELOPER_DEFINED_PAYLOAD"
            }
          ]
        },
        {
          "title": "5ENSI by BeanZ Cafe",
          "image_url": "https://maps.googleapis.com/maps/api/place/photo?maxwidth=700&photoreference=CmRaAAAAneCDoaT3dJtZlcj4YB1WFubBcAuhqnFAImhhi-mPjc1CgDy2S_d10XIPbFmnQO7b9VAvtvl0OriDAXAZzFvBhXWJyrEJtCDPB-7m9QIvnY42SqiN_2ZRfe_pkzUp2ARnEhCr3bnolRaR1CT00jcTEv-rGhTsffSjERsf-YcEPD5hDoohw59pnQ&key=AIzaSyAu-uc1As4xBhfge4l_9Aj4qZ-Vh6IJYWg",
          "subtitle": "powered by Google \nphoto author: Vlad Albulescu ",
          "default_action": {
            "type": "web_url",
            "url": "https://maps.google.com/maps/contrib/105538209994368268843",
            "webview_height_ratio": "tall"
          },
          "buttons": [
            {
              "type": "web_url",
              "title": "view website",
              "url": "https://m.facebook.com/5ENSIbyBeanZCafe/"
            },
            {
              "type": "postback",
              "title": "more details",
              "payload": "DEVELOPER_DEFINED_PAYLOAD"
            }
          ]
        },
        {
          "title": "5ENSI by BeanZ Cafe",
          "image_url": "https://maps.googleapis.com/maps/api/place/photo?maxwidth=700&photoreference=CmRZAAAAg00CEySekLKeuKMHKIJaYxk5D2dRl4bqdgAYTRn60C2I4KZJwgTPnzQFW-gT3LTcbcvbiqe0lcKPD72CjpXTNodnGcpWgf23ENRLVxmD6a-07pgdaMkn1id901w7nMwJEhBKhJERnGw_NY___jroPtSnGhQ4yUX9A86wcPKUrxBBgHKz4mm5kg&key=AIzaSyAu-uc1As4xBhfge4l_9Aj4qZ-Vh6IJYWg",
          "subtitle": "powered by Google \nphoto author: raiser costin ",
          "default_action": {
            "type": "web_url",
            "url": "https://maps.google.com/maps/contrib/113592889921571241235",
            "webview_height_ratio": "tall"
          },
          "buttons": [
            {
              "type": "web_url",
              "title": "view website",
              "url": "https://m.facebook.com/5ENSIbyBeanZCafe/"
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
