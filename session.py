import time
from lightrail_locations import LIGHTRAIL_STATIONS
from api import get_places_from_stops

from flask import Flask, session


def reset_session():
    session["user_category"] = None
    session["stops"] = [False] * len(LIGHTRAIL_STATIONS)
    session["stops"][0] = True

def get_search_results():
    search_results = get_places_from_stops([s for s, keep in zip(LIGHTRAIL_STATIONS, session["stops"]) if keep])
    search_results.sort(key=lambda p: p["rating"] * max(1, p["userRatingCount"]), reverse=True)
    return search_results

