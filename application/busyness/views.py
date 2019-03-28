from application import app, db
from flask import render_template, request, redirect, url_for
from application.busyness.models import Busyness
from application.busyness.forms import BusynessForm

@app.route("/busyness", methods=["GET"])
def busyness_index():
    return render_template("busyness/list.html", busynessList = Busyness.query.all())


@app.route("/busyness/new/")
def busyness_form():
    return render_template("busyness/new.html", form = BusynessForm())

@app.route("/busyness/", methods=["POST"])
def busyness_create():
    form = BusynessForm(request.form)

    if not form.validate():
        return render_template("busyness/new.html", form = form)

    b = Busyness(form.name.data, form.laakareita.data, form.sairaanhoitajia.data, form.perushoitajia.data)
    db.session().add(b)
    db.session().commit()

    return redirect(url_for("busyness_index"))
