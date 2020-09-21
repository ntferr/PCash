from app import db

class CreditCardDebts(db.Model):
    id = db.column(db.Integer, primary_key = True, autoincrement = True)
    value = db.column(db.Float)
    bank = db.column(db.String(100))
    description = db.column(db.String(180))

    spending = db.relationship('Spending', backref = 'credit_card_debts', lazy = True)
    
    def __init__(self, credit_card_debts):
        self.value = credit_card_debts['value']
        self.bank = credit_card_debts['bank']
        self.description = credit_card_debts['description']
