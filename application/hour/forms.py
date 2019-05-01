from flask_wtf import FlaskForm
from wtforms import DateField, IntegerField, SelectField, validators
from  application import db
from application.busyness.models import Busyness

class HourForm(FlaskForm):
    date = DateField("Päivämäärä (vvvv-kk-pp)", [validators.InputRequired()])
    start = IntegerField("Alkuaika", [validators.InputRequired(), validators.NumberRange(min=0, max=23)])
    end = IntegerField("Päättymisaika", [validators.InputRequired(), validators.NumberRange(min=0, max=23)])
    busyness_id = SelectField("Kiireellisyysluokka", coerce=int, validators = [validators.InputRequired()])


    class Meta:
        csrf = False
