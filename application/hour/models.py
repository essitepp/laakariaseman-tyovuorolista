from application import db
from sqlalchemy.sql import text
from sqlalchemy.orm import relationship
from application.employee.models import employee_hours

class Hour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    start = db.Column(db.Integer)
    busyness_id = db.Column(db.Integer, db.ForeignKey('busyness.id'))
    employees = db.relationship(
        'Employee',
        secondary=employee_hours,
        back_populates="hours")

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
    def findHour(date=0, start=0):

        stmt = text("SELECT Hour.id FROM Hour WHERE Hour.date = :date AND Hour.start = :start").params(date=date, start=start)
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def hoursMissingEmployees():

        stmt = text("SELECT Hour.id, Hour.date, Hour.start, Busyness.laakareita, Busyness.sairaanhoitajia, Busyness.perushoitajia FROM Hour JOIN Busyness ON Busyness.id = Hour.busyness_id")
        res = db.engine.execute(stmt)
        print("test3")
        response = []
        for row in res:
            print("test4")
            print(row[0])
            employees = Hour.findEmployees(row[0])
            print(employees)
            l = row[3] - employees["l"]
            s = row[4] - employees["s"]
            if l < 0:
                s = s + l
            p = row[5] - employees["p"]
            if s < 0:
                p = p + s
            response.append({"date":row[1], "time":row[2], "l":l, "s":s, "p":p})
        return response

    @staticmethod
    def findEmployees(hour=0):
        print("test")
        stmt = text("SELECT COUNT(Employee.id) FROM Employee JOIN employee_hours ON Employee.id = employee_hours.employee_id JOIN Hour ON Hour.id = employee_hours.hour_id WHERE Employee.role = 'Lääkäri' AND Hour.id = :hour").params(hour=hour)
        res = db.engine.execute(stmt)
        print("test2")
        for row in res:
            print(row[0])
            l = row[0]
            print(l)
        stmt = text("SELECT COUNT(Employee.id) FROM Employee JOIN employee_hours ON Employee.id = employee_hours.employee_id JOIN Hour ON Hour.id = employee_hours.hour_id WHERE Employee.role = 'Sairaanhoitaja' AND Hour.id = :hour").params(hour=hour)
        res = db.engine.execute(stmt)
        for row in res:
            s = row[0]
            print(s)
        stmt = text("SELECT COUNT(Employee.id) FROM Employee JOIN employee_hours ON Employee.id = employee_hours.employee_id JOIN Hour ON Hour.id = employee_hours.hour_id WHERE Employee.role = 'Perushoitaja' AND Hour.id = :hour").params(hour=hour)
        res = db.engine.execute(stmt)
        for row in res:
            p = row[0]
            print(p)
        response = {"l":l, "s":s, "p":p}
        print(response)
        return response
