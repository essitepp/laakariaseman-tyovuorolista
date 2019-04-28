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
    def findBusyness(hour=0):
        stmt = text("SELECT Busyness.name FROM Busyness JOIN Hour ON Hour.busyness_id = Busyness.id WHERE Hour.id=:hour").params(hour=hour)
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
        response = []
        for row in res:
            employees = Hour.findEmployees(row[0])
            l = row[3] - employees["l"]
            s = row[4] - employees["s"]
            if l < 0:
                s = s + l
            p = row[5] - employees["p"]
            if s < 0:
                p = p + s
            if l > 0 or s > 0 or p > 0:
                response.append({"date":row[1], "time":row[2], "l":l, "s":s, "p":p})
        return response


    @staticmethod
    def missingEmployees(hour=0):

        stmt = text("SELECT Busyness.laakareita, Busyness.sairaanhoitajia, Busyness.perushoitajia FROM Hour JOIN Busyness ON Busyness.id = Hour.busyness_id WHERE Hour.id = :hour").params(hour=hour)
        res = db.engine.execute(stmt)

        for row in res:
            employees = Hour.findEmployees(hour)
            l = row[0] - employees["l"]
            s = row[1] - employees["s"]
            if l < 0:
                s = s + l
            p = row[2] - employees["p"]
            if s < 0:
                p = p + s
            response = {"l":l, "s":s, "p":p}
        return response

    @staticmethod
    def findEmployees(hour=0):
        stmt = text("SELECT COUNT(Employee.id) FROM Employee JOIN employee_hours ON Employee.id = employee_hours.employee_id JOIN Hour ON Hour.id = employee_hours.hour_id WHERE Employee.role = 'Lääkäri' AND Hour.id = :hour").params(hour=hour)
        res = db.engine.execute(stmt)
        for row in res:
            l = row[0]
        stmt = text("SELECT COUNT(Employee.id) FROM Employee JOIN employee_hours ON Employee.id = employee_hours.employee_id JOIN Hour ON Hour.id = employee_hours.hour_id WHERE Employee.role = 'Sairaanhoitaja' AND Hour.id = :hour").params(hour=hour)
        res = db.engine.execute(stmt)
        for row in res:
            s = row[0]
        stmt = text("SELECT COUNT(Employee.id) FROM Employee JOIN employee_hours ON Employee.id = employee_hours.employee_id JOIN Hour ON Hour.id = employee_hours.hour_id WHERE Employee.role = 'Perushoitaja' AND Hour.id = :hour").params(hour=hour)
        res = db.engine.execute(stmt)
        for row in res:
            p = row[0]
        response = {"l":l, "s":s, "p":p}
        return response

    @staticmethod
    def listEmployees(hour=0):
        stmt = text("SELECT Employee.name FROM Employee JOIN employee_hours ON employee_hours.employee_id = Employee.id JOIN Hour ON Hour.id = employee_hours.hour_id WHERE Hour.id = :hour").params(hour=hour)
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append(row[0])
        return response

    @staticmethod
    def listHours():
        stmt = text("SELECT Hour.id, Hour.date, Hour.start FROM Hour ORDER BY Hour.date, Hour.start")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"id":row[0], "date":row[1], "start":row[2]})
        return response

    @staticmethod
    def listDates():
        stmt = text("SELECT DISTINCT Hour.date FROM Hour ORDER BY Hour.date")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append(row[0])
        return response

    @staticmethod
    def getTimes(date=0):
        stmt = text("SELECT Hour.start FROM Hour WHERE Hour.date=:date ORDER BY Hour.start").params(date=date)
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append(row[0])
        return response

    @staticmethod
    def listEmployeeHours(employee):
        stmt = text("SELECT DISTINCT Hour.date FROM Hour JOIN employee_hours ON employee_hours.hour_id = Hour.id JOIN Employee ON Employee.id = employee_hours.employee_id WHERE Employee.id = :employee ORDER BY Hour.date").params(employee=employee)
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            times = []
            stmt = text("SELECT Hour.start FROM Hour JOIN employee_hours ON employee_hours.hour_id = Hour.id JOIN Employee ON Employee.id = employee_hours.employee_id WHERE Employee.id = :employee AND Hour.date = :date ORDER BY Hour.start").params(date=row[0], employee=employee)
            res2 = db.engine.execute(stmt)
            for row2 in res2:
                times.append(row2[0])
            response.append({"date":row[0], "times":times})
        return response
