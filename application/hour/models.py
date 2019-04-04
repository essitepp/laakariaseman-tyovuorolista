from application import db
from sqlalchemy.sql import text

class Hour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    start = db.Column(db.Integer)
    busyness_id = db.Column(db.Integer, db.ForeignKey('busyness.id'))

    def __init__(self, date, start):
        self.date = date
        self.start = start


