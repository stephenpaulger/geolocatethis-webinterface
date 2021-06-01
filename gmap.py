import requests


AUTH_KEY = ''


def send_request(location, radius, keyword, category, pagetoken=None):
    api_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"

    params = {
        "location": location,
        "radius": radius,
        "type": category,
        "keyword": keyword,
        "key": AUTH_KEY,
    }

    if pagetoken is not None:
        params["pagetoken"] = pagetoken

    response = requests.get(api_url, params=params)

    if response.status_code != 200:
        print("Something went wrong. Error code: {}".format(response.status_code))
        exit

    return response.json()
