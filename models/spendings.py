from app import db

class Spendings(db.Model):
    id = db.Column(db.Integer, primary_key = True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.spendings'), nullable=False)

    debts = db.relationship('Debts', backref = 'debts', lazy = True)
    credit_card = db.relationship('CreditCardDebts', backref = 'credit_card_debts', lazy = True)


def __init__(self, spendings)
    self.user_id = spendings['user_id']