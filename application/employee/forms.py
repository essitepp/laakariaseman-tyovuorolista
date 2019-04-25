from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, RadioField, DateField, validators
from application import db
from application.employee.models import Employee

class EmployeeForm(FlaskForm):
    name = StringField("Nimi", [validators.InputRequired()])
    role = SelectField("Henkilöstöluokka", choices=[("Lääkäri", "Lääkäri"), ("Sairaanhoitaja", "Sairaanhoitaja"), ("Perushoitaja", "Perushoitaja")], validators=[validators.InputRequired()])
    day = IntegerField("Työtunteja päivässä", [validators.InputRequired()])
    week = IntegerField("Työtunteja viikossa", [validators.InputRequired()])

    class Meta:
        csrf = False
