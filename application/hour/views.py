from flask import render_template, request, redirect, url_for
from flask_login import login_required

from application import app, db
from application.hour.models import Hour
from application.hour.forms import HourForm
from application.busyness.models import Busyness

@app.route("/hour", methods=["GET"])
def hour_index():
    return render_template("hour/list.html", hourList = Hour.query.all())


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
        db.session().add(h)
        db.session().commit()

    return redirect(url_for("hour_index"))
