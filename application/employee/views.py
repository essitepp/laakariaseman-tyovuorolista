from flask import render_template, request, redirect, url_for
from flask_login import login_required

from application import app, db
from application.employee.models import Employee
from application.hour.models import Hour
from application.employee.forms import EmployeeForm
from application.employee.hourform import EmployeeHourForm
from application.employee.selectform import EmployeeSelectForm

@app.route("/employee/", methods=["GET"])
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

@app.route("/employee/addhours/")
def employee_hourform():
    return render_template("employee/addHours.html", form = EmployeeHourForm())

@app.route("/employee/hours", methods=["POST"])
def employee_addHours():
    form = EmployeeHourForm(request.form)

    if not form.validate():
        return render_template("employee/addHours.html", form = form)

    e = db.session.query(Employee).get(form.employee.data)
    for time in range(form.start.data, form.end.data):
        hour_id = Hour.findHour(form.date.data, time)
        h = db.session.query(Hour).get(hour_id)
        e.hours.append(h)
    db.session().add(e)
    db.session().commit()

    return redirect(url_for("listShifts"))

@app.route("/employee/select")
def employee_select():
    return render_template("employee/select.html", form = EmployeeSelectForm())

@app.route("/employee/listhours", methods=["GET", "POST"])
def employee_listHours():
    form = EmployeeSelectForm(request.form)

    if not form.validate():
        return render_template("employee/select.html", form = form)

    hourList = Employee.findHours(form.employee.data)
    return render_template("employee/listHours.html", hourList=hourList)
