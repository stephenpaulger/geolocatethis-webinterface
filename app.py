from flask import Flask, render_template, request
from forms import geolocatethisForm
from geolocatethis import geo_locate_this

import googlemaps

app = Flask(__name__)
app.config.from_object("config.Config")


@app.route("/", methods=["GET", "POST"])
def home():
    form = geolocatethisForm(request.form)
    results = None

    if form.validate_on_submit():
        gmaps = googlemaps.Client(app.config.get("GMAPS_AUTH_KEY"))
        results = geo_locate_this(
            request.form["latitude"],
            request.form["longitude"],
            request.form["radius"],
            request.form["keyword1"],
            request.form["category1"],
            request.form["keyword2"],
            request.form["category2"],
            request.form["distance"],
            gmaps,
        )

    return render_template("index.html", form=form, results=results)


@app.route("/about")
def about():
    return render_template("about.html")
