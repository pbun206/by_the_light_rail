from flask import Flask, render_template, request
from session import reset_session, get_search_results
from lightrail_locations import stops_to_form, LINE_1_STATIONS

import urllib.request

from keys import APP_SECRET 


app = Flask(__name__)
app.secret_key = APP_SECRET

@app.route("/")
def index():
    d = {
        "stops": stops_to_form(LINE_1_STATIONS)
    }
    return render_template("index.html", d=d)

@app.route("/about")
def about():
    return render_template("about.html")




@app.route("/result", methods=["GET", "POST"])
def submit_page():
    name = request.form["user_name"]
    return "hello {}! ^^".format(name)

def is_it_raining_in_seattle():
    with urllib.request.urlopen('https://depts.washington.edu/ledlab/teaching/is-it-raining-in-seattle/') as response:
        is_it_raining_in_seattle = response.read().decode()
    if is_it_raining_in_seattle == "true":
        return True
    else:
        return False
