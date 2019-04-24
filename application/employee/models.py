from application import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144))
    role = db.Column(db.String(144))
    hoursPerDay = db.Column(db.Integer)
    hoursPerWeek = db.Column(db.Integer)

    def __init__(self, name, role, hoursPerDay, hoursPerWeek):
        self.name = name
        self.role = role
        self.hoursPerDay = hoursPerDay
        self.hoursPerWeek = hoursPerWeek
