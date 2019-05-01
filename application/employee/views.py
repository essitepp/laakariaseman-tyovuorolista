from flask import render_template, request, redirect, url_for
from flask_login import login_required

from application import app, db
from application.employee.models import Employee
from application.hour.models import Hour
from application.employee.forms import EmployeeForm
from application.employee.hourform import EmployeeHourForm
from application.employee.selectform import EmployeeSelectForm
from application.employee.editform import EmployeeEditForm

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
    form = EmployeeHourForm()
    choices = [(x.id, x.name) for x in Employee.query.all()]
    form.employee.choices = choices
    return render_template("employee/addHours.html", form = form)

def hourform_selectField(form):
    choices = [(x.id, x.name) for x in Employee.query.all()]
    form.employee.choices = choices
    return

@app.route("/employee/hours", methods=["POST"])
def employee_addHours():
    form = EmployeeHourForm(request.form)
    hourform_selectField(form)
    if not form.validate():
        return render_template("employee/addHours.html", form = form)

    e = db.session.query(Employee).get(form.employee.data)
    for time in range(form.start.data, form.end.data):
        if Hour.hourExists(form.date.data, time):
            hour_id = Hour.findHour(form.date.data, time)
            h = db.session.query(Hour).get(hour_id)
            e.hours.append(h)
    db.session().add(e)
    db.session().commit()

    return redirect(url_for("missingEmployees_index"))

@app.route("/employee/select")
def employee_select():
    form = EmployeeSelectForm()
    choices = [(x.id, x.name) for x in Employee.query.all()]
    form.employee.choices = choices
    return render_template("employee/select.html", form = form)

def selectform_selectField(form):
    choices = [(x.id, x.name) for x in Employee.query.all()]
    form.employee.choices = choices
    return

@app.route("/employee/listhours", methods=["GET", "POST"])
def employee_listHours():
    form = EmployeeSelectForm(request.form)
    selectform_selectField(form)
    if not form.validate():
        return render_template("employee/select.html", form = form)
    hourList = Hour.listEmployeeHours(form.employee.data)
    return render_template("employee/listHours.html", hourList=hourList, employee=Employee.getName(form.employee.data))

@app.route("/employee/edit/<employee_id>/", methods=["GET", "POST"])
def employee_edit(employee_id):
    employee = Employee.query.get(employee_id)
    return render_template("employee/edit.html", form=EmployeeEditForm(obj=employee), employee_id=employee_id)

@app.route("/employee/<employee_id>/", methods=["POST"])
def employee_save(employee_id):
    form = EmployeeEditForm(request.form)

    if not form.validate():
        return render_template("employee/edit.html", form = form, employee_id = employee_id)
    e = Employee.query.get(employee_id)
    e.name = form.name.data
    e.role = form.role.data
    e.hoursPerDay = form.hoursPerDay.data
    e.hoursPerWeek = form.hoursPerWeek.data
    db.session().add(e)
    db.session().commit()
    return redirect(url_for("employee_index"))

@app.route("/employee/delete/<employee_id>/", methods=["GET", "POST"])
def employee_delete(employee_id):
    e = Employee.query.get(employee_id)
    db.session().delete(e)
    db.session().commit()
    return redirect(url_for("employee_index"))
