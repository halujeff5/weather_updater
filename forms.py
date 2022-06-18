from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    name= StringField ("Name of City: ")
    submit = SubmitField("Add City" )


