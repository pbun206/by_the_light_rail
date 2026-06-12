from lightrail import LightRailStation
from keys import GOOGLE_MAPS_PLATFORM_KEY 
import urllib.parse
import urllib.request
import urllib.error
import json

COUNT = 1
NEARBY_SEARCH_URL = "https://places.googleapis.com/v1/places:searchNearby"

def get_places_from_stop(stop):
    body = {
        "includedTypes": ["restaurant"],
        "maxResultCount": COUNT,
        "locationRestriction": {
            "circle": {
                "center": {
                    "latitude": stop.coord.lat,
                    "longitude": stop.coord.long
                },
                "radius": 3000.0
            }
        }
    }
    encoded_body = json.dumps(body).encode()
    req = urllib.request.Request(
        url = NEARBY_SEARCH_URL,
        headers={
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "application/json",
            "X-Goog-Api-Key": GOOGLE_MAPS_PLATFORM_KEY,
            "X-Goog-FieldMask":"places.displayName,places.priceLevel,places.rating,places.websiteUri,places.userRatingCount,places.photos"
        },
        data=encoded_body,
        method='POST'
    )
    try:
        response = json.loads(urllib.request.urlopen(req).read())
        for r in response["places"]:
            r["lightRailStation"] = stop.name
        return response
    except urllib.error.URLError as err:
        print("Error trying to retrieve data: " + str(err))
        return None
    except urllib.error.HTTPError as err:
        print("Error trying to retrieve data: " + str(err))
        return None


def get_places_from_stops(stops):
    res = []
    for stop in stops:
        inner_res = get_places_from_stop(stop)
        if inner_res is not None:
            for pl in inner_res["places"]:
                res.append(pl)
    return res
