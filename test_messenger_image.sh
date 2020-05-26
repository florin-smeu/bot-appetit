curl -X POST -H "Content-Type: application/json" -d '{
  "recipient":{
    "id":"3099149793483565"
  },
  "message":{
    "attachment":{
      "type":"image",
      "payload":{
        "url":"http://www.messenger-rocks.com/image.jpg",
        "is_reusable":true
      }
    }
  }
}' "https://graph.facebook.com/v7.0/me/messages?access_token=EAADjMOUraYABAKkFZBWWA4MEkUcQrLBV1sZAYMnq1b4rEAYXI6bk18hR0ZBzXR1OTboPHTIJmYTkCz2TIWppidwjlH2jVvAgkgsKJUglpzOiZBeWBegZArZAHD8OpQgJuEzkJkZCNLCF8ITtkXKxiMOcP3ideM4ajBgvOc1eykZCjAZDZD"
