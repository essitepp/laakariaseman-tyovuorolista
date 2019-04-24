from flask import render_template, request, redirect, url_for
from flask_login import login_required

from application import app, db
from application.employee.models import Employee
from application.employee.forms import EmployeeForm

@app.route("/employee", methods=["GET"])
def employee_index():
    return render_template("employee/list.html", employeeList = Employee.query.all())


@app.route("/employee/new/")
def employee_form():
    return render_template("employee/new.html", form = EmployeeForm())

@app.route("/employee/", methods=["POST"])
def employee_create():
    form = EmployeeForm(request.form)

    if not form.validate():
        return render_template("employee/new.html", form = form)

    e = Employee(form.name.data, form.role.data, form.day.data, form.week.data)
    db.session().add(e)
    db.session().commit()

    return redirect(url_for("employee_index"))
