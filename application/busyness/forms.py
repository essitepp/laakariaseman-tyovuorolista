from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class BusynessForm(FlaskForm):
    name = StringField("Kiireellisyysluokan nimi", [validators.InputRequired()])
    laakareita = IntegerField("Lääkäreitä", [validators.InputRequired()])
    sairaanhoitajia = IntegerField("Sairaanhoitajia", [validators.InputRequired()])
    perushoitajia = IntegerField("Perushoitajia", [validators.InputRequired()])


    class Meta:
        csrf = False
