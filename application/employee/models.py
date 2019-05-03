from application import db
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text

employee_hours = db.Table('employee_hours',
    db.Column('employee_id', db.Integer, db.ForeignKey('employee.id')),
    db.Column('hour_id', db.Integer, db.ForeignKey('hour.id'))
)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144))
    role = db.Column(db.String(144))
    hoursPerDay = db.Column(db.Integer)
    hoursPerWeek = db.Column(db.Integer)
    hours = db.relationship(
        'Hour',
        secondary=employee_hours,
        back_populates='employees')

    def __init__(self, name, role, hoursPerDay, hoursPerWeek):
        self.name = name
        self.role = role
        self.hoursPerDay = hoursPerDay
        self.hoursPerWeek = hoursPerWeek

    def findHours(employee):

        stmt = text("SELECT Hour.date, Hour.start FROM Employee JOIN employee_hours ON Employee.id = employee_hours.employee_id JOIN Hour ON Hour.id = employee_hours.hour_id WHERE Employee.id = :employee").params(employee=employee)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"date":row[0], "time":row[1]})
        return response

    def getName(id):
        stmt = text("SELECT Employee.name FROM Employee WHERE Employee.id = :id").params(id=id)
        res = db.engine.execute(stmt)
        for row in res:
            return row[0]
