
# Python program to get a set of
# places according to your search
# query using Google Places API

# importing required modules
import requests, json

# enter your api key here
api_key = 'AIzaSyAu-uc1As4xBhfge4l_9Aj4qZ-Vh6IJYWg'

# url variable store url
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

def retrieve_place_details():
    global api_key
    global url

    # The text string on which to search
    query = input('Search query: ')

    # get method of requests module
    # return response object
    r = requests.get(url + 'query=' + query +
                            '&key=' + api_key)

    # json method of response object convert
    #  json format data into python format data
    x = r.json()

    # now x contains list of nested dictionaries
    # we know dictionary contain key value pair
    # store the value of result key in variable y
    y = x['results']

    # keep looping upto length of y
    for i in range(len(y)):

        # Print value corresponding to the
        # 'name' key at the ith index of y
        with open("res_api.json", "w") as f:
            json.dump(y, f, ensure_ascii=False, indent=4)
        print(y[i])
    return y

def retrieve_photos(place_details):
    global api_key

    photo_url = "https://maps.googleapis.com/maps/api/place/photo?"

    for details in place_details:
        photos = details["photos"]
        photo_reference = photos[0]["photo_reference"]

        r = requests.get(photo_url + "maxwidth=" + str(400) +
                    "&photoreference=" + photo_reference +
                    "&key=" + api_key, stream=True)

        if r.status_code == 200:
            with open(photo_reference, "wb") as g:
                #g.write(str(r.raw))
                img = r.raw.read()
                g.write(img)
        break




def main():
    place_details = retrieve_place_details()
    #retrieve_photos(place_details)




if __name__ == "__main__":
    main()
