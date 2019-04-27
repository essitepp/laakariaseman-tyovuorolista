from flask_wtf import FlaskForm
from wtforms import DateField, IntegerField, RadioField, validators
from application import db
from application.employee.models import Employee

class EmployeeHourForm(FlaskForm):
    date = DateField("Päivämäärä", [validators.InputRequired()])
    start = IntegerField("Alkuaika", [validators.InputRequired()])
    end = IntegerField("Päättymisaika", [validators.InputRequired()])
    employee = RadioField("Työntekijä", choices=[(x.id, x.name) for x in Employee.query.all()], coerce=int, validators=[validators.InputRequired()])

    class Meta:
        csrf = False
