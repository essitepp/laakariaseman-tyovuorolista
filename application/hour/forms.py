from flask_wtf import FlaskForm
from wtforms import DateField, IntegerField, SelectField, validators
from  application import db
from application.busyness.models import Busyness

class HourForm(FlaskForm):
    date = DateField("Päivämäärä", [validators.InputRequired()])
    start = IntegerField("Alkuaika", [validators.InputRequired()])
    end = IntegerField("Päättymisaika", [validators.InputRequired()])
    busyness_id = SelectField("Kiireellisyysluokka", choices=[(x.id, x.name) for x in Busyness.query.all()], coerce=int)


    class Meta:
        csrf = False
