from app import db

class Spedings(db.Model):
    id = db.Column(db.Integer, primary_key = True)    
