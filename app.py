from flask import Flask, render_template, request, flash
from secrets import token_hex
from forms import geolocatethisForm
from geolocatethis import geo_locate_this

app = Flask(__name__)
app.config["SECRET_KEY"] = token_hex(16)


@app.route("/", methods=["GET", "POST"])
def home():
    form = geolocatethisForm(request.form)

    if form.validate_on_submit():
        results = geo_locate_this(
            request.form["latitude"],
            request.form["longitude"],
            request.form["radius"],
            request.form["keyword1"],
            request.form["category1"],
            request.form["keyword2"],
            request.form["category2"],
            request.form["distance"],
        )

        for hit in results:
            flash(hit)

    return render_template("index.html", form=form)


@app.route("/about")
def about():
    return render_template("about.html")
