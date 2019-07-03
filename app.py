from flask import Flask, render_template, request,flash
from secrets import token_hex
from forms import geolocatethisForm
from geolocatethis import geo_locate_this

app = Flask(__name__)
app.config['SECRET_KEY'] = token_hex(16)


@app.route('/', methods=['GET', 'POST'])
def home():
    form = geolocatethisForm(request.form)

    if form.validate():
        results = geo_locate_this(request.form['latitude'], request.form['longitude'],
                                  request.form['radius'],   request.form['keyword1'],
                                  request.form['category1'], request.form['keyword2'],
                                  request.form['category2'], request.form['distance'])
        flash(results)
    else:
        print(form.errors)
        flash('There was an error submitting your request')

    return render_template('index.html', title='GeoLocateThis Web Application', form=form)


if __name__ == '__main__':
    app.run()
