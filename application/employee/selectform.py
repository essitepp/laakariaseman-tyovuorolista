from flask_wtf import FlaskForm
from wtforms import RadioField, validators
from application import db
from application.employee.models import Employee

class EmployeeSelectForm(FlaskForm):
    employee = RadioField("Työntekijä", choices=[(x.id, x.name) for x in Employee.query.all()], coerce=int, validators=[validators.InputRequired()])


    class Meta:
        csrf = False
