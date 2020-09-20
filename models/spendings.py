from app import db

class Speding(db.Model):
    id = db.Column(db.Integer, primary_key = True)
