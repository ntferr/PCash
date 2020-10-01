from app import db

class Spedings(db.Model):
    id = db.Column(db.Integer, primary_key = True)

    debts = db.relantionship('Debts', backref = 'debts', lazy = True)
    credit_card = db.relantionship('CreditCardDebts', backref = 'credit_card_debts', lazy = True)
