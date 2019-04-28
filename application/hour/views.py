from flask import render_template, request, redirect, url_for
from flask_login import login_required

from application import app, db
from application.hour.models import Hour
from application.hour.forms import HourForm
from application.busyness.models import Busyness

@app.route("/hour", methods=["GET"])
def hour_index():
    list = []
    dateList = Hour.listDates()
    for date in dateList:
        hourList = []
        hours = Hour.getTimes(date)
        for hour in hours:
            busyness = Hour.findBusyness(Hour.findHour(date, hour))
            missing = Hour.missingEmployees(Hour.findHour(date, hour))
            hourList.append({"time":hour, "busyness":busyness})
        list.append({"date":date, "times":hourList})
    return render_template("hour/list.html", hourList = list)
    hours = Hour.query.order_by(Hour.date, Hour.start)
    hourList = []
    for hour in hours:
        hourList.append({"hour":hour, "busyness":hour.getBusyness(hour.busyness_id)})
    return render_template("hour/list.html", hourList = hourList)


@app.route("/hour/new/")
def hour_form():
    return render_template("hour/new.html", form = HourForm())


@app.route("/hour/", methods=["GET", "POST"])
def hour_create():
    busyness_list=[(x.id, x.name) for x in Busyness.query.all()]
    form = HourForm(request.form)
    form.busyness_id.choices = busyness_list

    if not form.validate():
        return render_template("hour/new.html", form = form)

    for time in range(form.start.data, form.end.data):
        h = Hour(form.date.data, time)
        h.busyness_id = form.busyness_id.data
        db.session().add(h)
        db.session().commit()

    return redirect(url_for("hour_index"))

@app.route("/missingemployees/", methods=["GET"])
def missingEmployees_index():
    list = []
    dateList = Hour.listDates()
    for date in dateList:
        hourList = []
        hours = Hour.getTimes(date)
        for hour in hours:
            missing = Hour.missingEmployees(Hour.findHour(date, hour))
            hourList.append({"time":hour, "employees":missing})
        list.append({"date":date, "times":hourList})
    return render_template("hour/missingEmployees.html", missing_employees=list)

@app.route("/shifts/", methods=["GET", "POST"])
def listShifts():
    shiftList = []
    dateList = Hour.listDates()
    for date in dateList:
        hourList = []
        hours = Hour.getTimes(date)
        for hour in hours:
            employees = Hour.listEmployees(Hour.findHour(date, hour))
            hourList.append({"time":hour, "employees":employees})
        shiftList.append({"date":date, "times":hourList})
    return render_template("hour/shifts.html", shiftList=shiftList)
