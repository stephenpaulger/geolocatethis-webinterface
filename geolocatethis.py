import googlemaps


AUTH_KEY = ''


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

    center_point = f"{lat},{lon}"
    page_token = None
    full_results = []
    gmaps = googlemaps.Client(AUTH_KEY)

    while True:
        place_1_data = gmaps.places_nearby(
            location=center_point,
            radius=radius,
            keyword=keyword_place_1,
            type=category_place_1,
            page_token=page_token
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

                place_2_data = gmaps.places_nearby(
                    location=location,
                    radius=distance,
                    keyword=keyword_place_2,
                    type=category_place_2,
                    page_token=None,
                )

                if "ZERO_RESULTS" not in place_2_data["status"]:
                    full_results.append(f"{name} (location: {location})")

            if "next_page_token" not in place_1_data:
                break

            page_token = place_1_data["next_page_token"]

    return full_results
