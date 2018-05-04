from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RadForm(FlaskForm):
    example = RadioField('Label', choices=[('first_name','First Names'),('last_name','Last Names')])
    