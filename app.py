from flask import Flask, render_template, request
from lightrail_locations import stops_to_form, LINE_1_STATIONS, LINE_2_STATIONS
from slugify import slugify
from api import get_places_from_stops, get_best_photo_url

import urllib.request

from keys import APP_SECRET 


app = Flask(__name__)
app.secret_key = APP_SECRET

@app.route("/")
def index():
    d = {
        "stops_line_1": stops_to_form(LINE_1_STATIONS),
        "stops_line_2": stops_to_form(LINE_2_STATIONS)
    }
    return render_template("index.html", d=d)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/results", methods=["GET", "POST"])
def result():
    if request.method == "GET":
        return "Error: was expecting a POST request", 400
    stops_to_use = []
    for stop in LINE_1_STATIONS:
        if slugify(stop.name) in request.form:
            stops_to_use.append(stop)
    for stop in LINE_2_STATIONS:
        if slugify(stop.name) in request.form:
            stops_to_use.append(stop)
    minute = int(request.form["minutes"])
    if minute < 1:
        minute = 1
    query = request.form["query"]
    if query == "":
        query = None
    try:
        res = get_places_from_stops(stops_to_use, query, minute)
    except urllib.error.URLError as err:
        return ("Error trying to retrieve data: " + str(err))
    except urllib.error.HTTPError as err:
        return ("Error trying to retrieve data: " + str(err))

    if len(res) == 0:
        return "Found no results :c"

    res.sort(key=lambda p: p.get("rating", 0) * max(1, p.get("userRatingCount", 1)/7.0), reverse=True)
    print(res)
    res_html = ""
    for place in res:
        res_html += "<tr>"
        if "websiteUri" in place:
            res_html += f"<td scope=\"row\"><a style=\"color: oklch(0.5 0.1 270)\" href=\"{place["websiteUri"]}\">{place["displayName"]["text"]}</a></td>"
        else:
            res_html += f"<td scope=\"row\">{place["displayName"]["text"]}</td>"
        if "photos" in place:
            res_html += f"<td><img alt=\"Photo of {place["displayName"]["text"]}\" src=\"{get_best_photo_url(place["photos"])}\"></td>"
        else:
            res_html += "<td></td>"
        if "rating" in place:
            res_html += f"<td>{place["rating"]}</td>"
        else:
            res_html += "<td></td>"
        res_html += "<td>"
        if "priceLevel" not in place or place["priceLevel"] == "PRICE_LEVEL_UNSPECIFIED":
            res_html += ""
        elif place["priceLevel"] == "PRICE_LEVEL_FREE":
            res_html += "FREE"
        elif place["priceLevel"] == "PRICE_LEVEL_INEXPENSIVE":
            res_html += "$"
        elif place["priceLevel"] == "PRICE_LEVEL_MODERATE":
            res_html += "$$"
        elif place["priceLevel"] == "PRICE_LEVEL_EXPENSIVE":
            res_html += "$$$"
        elif place["priceLevel"] == "PRICE_LEVEL_VERY_EXPENSIVE":
            res_html += "$$$$"
        res_html += "</td>"
        res_html += f"<td>{place["lightRailStation"]}</td>"
        if "googleMapsUri" in place:
            res_html += f"<td><a style=\"color: oklch(0.5 0.1 270)\" href=\"{place["googleMapsUri"]}\">Link</a></td>"
        else:
            res_html += "<td></td>"
        res_html += "</tr>"
    d = {
        "results": res_html
    }
    return render_template("result.html", d=d)

