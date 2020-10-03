from app import db

class CreditCardDebts(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    value = db.Column(db.Float)
    bank = db.Column(db.String(100))
    description = db.Column(db.String(180))

    spending_id = db.relationship(db.Integer, db.ForeignKey('speding.credit_card'), nullable = False)
    
    def __init__(self, credit_card_debts):
        self.value = credit_card_debts['value']
        self.bank = credit_card_debts['bank']
        self.description = credit_card_debts['description']
        
        self.spending_id = credit_card_debts['spending_id']
