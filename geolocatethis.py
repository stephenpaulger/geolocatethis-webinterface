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
    match_count = 0
    full_results = []

    while True:
        place_1_data = send_request(
            center_point, radius, keyword_place_1, category_place_1, pagetoken
        )

        if "OK" in place_1_data["status"]:
            for result in place_1_data["results"]:
                temp_name = result["name"]
                temp_lat = result["geometry"]["location"]["lat"]
                temp_lng = result["geometry"]["location"]["lng"]
                temp_location = "{},{}".format(temp_lat, temp_lng)

                place_2_data = send_request(
                    temp_location,
                    distance,
                    keyword_place_2,
                    category_place_2,
                    blank_pagetoken,
                )
                if "ZERO_RESULTS" not in place_2_data["status"]:
                    """print ("Found match at {} (location: {})".format(temp_name, temp_location))"""
                    full_results.append(
                        "Found match at {} (location: {})".format(
                            temp_name, temp_location
                        )
                    )
                    match_count += 1

            if "next_page_token" not in place_1_data:
                print(
                    "Done. Found {} locations matching given criteria.".format(
                        match_count
                    )
                )
                return full_results
                break

            else:
                pagetoken = place_1_data["next_page_token"]

        elif "ZERO_RESULTS" in place_1_data["status"]:
            print("Sorry, no results with provided parameters")
            return "Sorry, no results with provided parameters"

            break

        elif "OVER_QUERY_LIMIT" in place_1_data["status"]:
            print("You have reached your daily API quota limit for this key.")
            return "You have reached your daily API quota limit for this key."
            break

        elif "REQUEST_DENIED" in place_1_data["status"]:
            print("Request to Google API denied. Check your API key.")
            return "Request to Google API denied. Check your API key."
            break

    return full_results
