from flask_wtf import FlaskForm
from wtforms import DateField, IntegerField, RadioField, validators
from application import db
from application.employee.models import Employee

class EmployeeHourForm(FlaskForm):
    date = DateField("Päivämäärä (vvvv-kk-pp)", [validators.InputRequired()])
    start = IntegerField("Alkuaika", [validators.InputRequired(), validators.NumberRange(min=0, max=23)])
    end = IntegerField("Päättymisaika", [validators.InputRequired(), validators.NumberRange(min=0, max=23)])
    employee = RadioField("Työntekijä", coerce=int, validators=[validators.InputRequired()])

    class Meta:
        csrf = False
