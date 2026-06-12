from flask import Flask, render_template, request
from session import reset_session, get_search_results

import urllib.request

from keys import APP_SECRET 


app = Flask(__name__)
app.secret_key = APP_SECRET

@app.route("/")
def index():
    reset_session()
    res = get_search_results()
    render = []
    for p in res:
        render.append(p["displayName"]["text"])
    return render_template("index.html", d=str(render))

@app.route("/about")
def about():
    return render_template("about.html")




@app.route("/submit-page", methods=["GET", "POST"])
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
