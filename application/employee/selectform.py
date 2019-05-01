from flask_wtf import FlaskForm
from wtforms import RadioField, validators
from application import db
from application.employee.models import Employee

class EmployeeSelectForm(FlaskForm):
    employee = RadioField("Työntekijä", coerce=int, validators=[validators.InputRequired()])


    class Meta:
        csrf = False
