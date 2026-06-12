from lightrail import LightRailStation
from keys import GOOGLE_MAPS_PLATFORM_KEY
import urllib.parse
import urllib.request
import urllib.error
import json
from math import cos, pi

EARTH_RADIUS = 6378137
COUNT = 10
MAIN_URL = "https://places.googleapis.com/v1/"
NEARBY_SEARCH_URL = "https://places.googleapis.com/v1/places:searchNearby"
TEXT_SEARCH_URL = "https://places.googleapis.com/v1/places:searchText"


def get_places_from_stop(stop, query=None, minutes=10):
    # https://www.medicalnewstoday.com/articles/average-walking-speed#average-speed-by-age
    radius = 57 * minutes
    body = {"maxResultCount": COUNT, "locationRestriction": {}}
    if query:
        body["textQuery"] = query
        body["locationRestriction"] = to_square(stop.coord, radius)
    else:
        body["locationRestriction"] = {
            "circle": {
                "center": {"latitude": stop.coord.lat, "longitude": stop.coord.long},
                "radius": radius,
            }
        }

    encoded_body = json.dumps(body).encode()
    if query:
        req = urllib.request.Request(
            url=TEXT_SEARCH_URL,
            headers={
                "User-Agent": "Mozilla/5.0",
                "Content-Type": "application/json",
                "X-Goog-Api-Key": GOOGLE_MAPS_PLATFORM_KEY,
                "X-Goog-FieldMask": "places.displayName,places.priceLevel,places.rating,places.websiteUri,places.userRatingCount,places.photos,places.googleMapsUri",
            },
            data=encoded_body,
            method="POST",
        )
    else:
        req = urllib.request.Request(
            url=NEARBY_SEARCH_URL,
            headers={
                "User-Agent": "Mozilla/5.0",
                "Content-Type": "application/json",
                "X-Goog-Api-Key": GOOGLE_MAPS_PLATFORM_KEY,
                "X-Goog-FieldMask": "places.displayName,places.priceLevel,places.rating,places.websiteUri,places.userRatingCount,places.photos",
            },
            data=encoded_body,
            method="POST",
        )
    response = json.loads(urllib.request.urlopen(req).read())
    if "places" in response:
        for r in response["places"]:
            r["lightRailStation"] = stop.name
        return response
    else:
        None


def get_places_from_stops(stops, query=None, minutes=10):
    res = []
    for stop in stops:
        inner_res = get_places_from_stop(stop, query, minutes)
        if inner_res is not None:
            for pl in inner_res["places"]:
                res.append(pl)
    return res


# https://gis.stackexchange.com/questions/2951/algorithm-for-offsetting-latitude-longitude-by-some-amount-of-meters
def to_square(coord, meters):
    return {
        "rectangle": {
            "low": {
                "latitude": coord.lat - meters/EARTH_RADIUS,
                "longitude": coord.long - meters/(EARTH_RADIUS*cos(pi*coord.lat/180)),
            },
            "high": {
                "latitude": coord.lat + meters/EARTH_RADIUS,
                "longitude": coord.long + meters/(EARTH_RADIUS*cos(pi*coord.lat/180)),
            },
        }
    }

def get_photo_url(photo):
    url = MAIN_URL + photo["name"] + "/media"
    url += "?maxHeightPx=200&maxWidthPx=400&key=" + GOOGLE_MAPS_PLATFORM_KEY
    return url

def get_best_photo_url(photos):
    best_photo = None
    # find the photo with the greatest height to width ratio
    best_photo_ratio = -1
    for photo in photos:
        ratio = photo["widthPx"] / photo["heightPx"]
        if ratio > best_photo_ratio:
            best_photo = photo
            best_photo_ratio = ratio
    return get_photo_url(photo)

        
