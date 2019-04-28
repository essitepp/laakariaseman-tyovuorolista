from flask import render_template, redirect, url_for
from application import app
from application.hour.models import Hour

@app.route("/")
def index():
    return redirect(url_for("missingEmployees_index"))

