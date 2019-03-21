from application import app, db
from flask import render_template, request, redirect, url_for
from application.busyness.models import Busyness

@app.route("/busyness", methods=["GET"])
def busyness_index():
    return render_template("busyness/list.html", busynessList = Busyness.query.all())


@app.route("/busyness/new/")
def busyness_form():
    return render_template("busyness/new.html")

@app.route("/busyness/", methods=["POST"])
def busyness_create():

    b = Busyness(request.form.get("name"),request.form.get("laakareita"),request.form.get("sairaanhoitajia"),request.form.get("perushoitajia"))
    db.session().add(b)
    db.session().commit()

    return redirect(url_for("busyness_index"))
