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

    @staticmethod
    def getBusyness(busyness=0):

        stmt = text("SELECT Busyness.name FROM Busyness WHERE Busyness.id = :busyness").params(busyness=busyness)
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def hoursMissingEmployees():
        return 1
