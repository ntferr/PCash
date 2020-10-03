from app import db

class Debts(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    value = db.Column(db.Float)
    description = db.Column(db.String(180))
    due_date = db.Column(db.DateTime)
    document_date = db.Column(db.DateTime)

    spending_id = db.Column(db.Integer, db.ForeignKey('spending.debts'), nullable = False)    

    def __init__(self, debts):
        self.value = debts['value']
        self.description = debts['description']
        self.due_date = debts['due_date']
        self.document_date = debts['document_date']

        self.spending_id = debts['spending_id']
