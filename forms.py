from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired


class geolocatethisForm(FlaskForm):
    latitude = DecimalField('Latitude', validators=[DataRequired()])
    longitude = DecimalField('Longitude', validators=[DataRequired()])
    radius = DecimalField('Radius', validators=[DataRequired()])
    keyword1 = StringField('Keyword for place 1', validators=[DataRequired()])
    category1 = StringField('Category for place 1')
    keyword2 = StringField('Keyword for place 2', validators=[DataRequired()])
    category2 = StringField('Category for place 2')
    distance = DecimalField('Distance between', validators=[DataRequired()])
    submit = SubmitField('search')