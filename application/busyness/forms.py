from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class BusynessForm(FlaskForm):
    name = StringField("Kiireellisyysluokan nimi", [validators.InputRequired()])
    laakareita = IntegerField("Lääkäreitä", [validators.InputRequired(), validators.NumberRange(min=0)])
    sairaanhoitajia = IntegerField("Sairaanhoitajia", [validators.InputRequired(), validators.NumberRange(min=0)])
    perushoitajia = IntegerField("Perushoitajia", [validators.InputRequired(), validators.NumberRange(min=0)])


    class Meta:
        csrf = False
