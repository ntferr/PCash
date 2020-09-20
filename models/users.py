from app import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    cpf = db.Column(db.String(11), nullable = False, unique = True)
    name = db.Column(db.String(225), nullable = False)
    password = db.Column(db.String(100), nullable = False)
    email =  db.Column(db.String(225), unique = True)
    date_of_birth = db.Column(db.DateTime)

    def __init__(self, user):
        self.cpf = user['cpf']
        self.name = user['name']
        self.password = user['password']
        self.email = user['email']
        self.date_of_birth = user['date_of_birth']