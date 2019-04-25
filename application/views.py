from flask import render_template
from application import app
from application.hour.models import Hour

@app.route("/")
def index():
    return render_template("index.html", missing_employees=Hour.hoursMissingEmployees())
