from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, validators

class EmployeeEditForm(FlaskForm):
    name = StringField("Nimi", [validators.InputRequired()])
    role = SelectField("Henkilöstöluokka", choices=[("Lääkäri", "Lääkäri"), ("Sairaanhoitaja", "Sairaanhoitaja"), ("Perushoitaja", "Perushoitaja")], validators = [validators.InputRequired()])
    hoursPerDay = IntegerField("Työtunteja päivässä", [validators.InputRequired(), validators.NumberRange(min=0, max=24)])
    hoursPerWeek = IntegerField("Työtunteja viikossa", [validators.InputRequired(), validators.NumberRange(min=0, max=168)])

    class Meta:
        csrf = False
