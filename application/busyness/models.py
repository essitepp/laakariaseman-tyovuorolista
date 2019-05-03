from application import db

class Busyness(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144))
    laakareita = db.Column(db.Integer)
    sairaanhoitajia = db.Column(db.Integer)
    perushoitajia = db.Column(db.Integer)


    def __init__(self, name, laakareita, sairaanhoitajia, perushoitajia):
        self.name = name
        self.laakareita = laakareita
        self.sairaanhoitajia = sairaanhoitajia
        self.perushoitajia = perushoitajia

    def get_id(self):
       return self.id

    def get_name(self):
        return self.name

