from gmap import send_request


def geo_locate_this(
    lat,
    lon,
    radius,
    keyword_place_1,
    keyword_place_2,
    category_place_1,
    category_place_2,
    distance,
):

    center_point = "{},{}".format(lat, lon)
    pagetoken = None
    blank_pagetoken = None
    full_results = []

    while True:
        place_1_data = send_request(
            center_point, radius, keyword_place_1, category_place_1, pagetoken
        )

        if "ZERO_RESULTS" in place_1_data["status"]:
            return "Sorry, no results with provided parameters"

        if "OVER_QUERY_LIMIT" in place_1_data["status"]:
            return "You have reached your daily API quota limit for this key."

        if "REQUEST_DENIED" in place_1_data["status"]:
            return "Request to Google API denied. Check your API key."

        if "OK" in place_1_data["status"]:
            for result in place_1_data["results"]:
                name = result["name"]
                lat = result["geometry"]["location"]["lat"]
                lng = result["geometry"]["location"]["lng"]
                location = f"{lat},{lng}"

                place_2_data = send_request(
                    location,
                    distance,
                    keyword_place_2,
                    category_place_2,
                    blank_pagetoken,
                )
                if "ZERO_RESULTS" not in place_2_data["status"]:
                    full_results.append(f"{name} (location: {location})")

            if "next_page_token" not in place_1_data:
                break

            pagetoken = place_1_data["next_page_token"]

    return full_results
