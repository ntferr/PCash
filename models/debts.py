from app import db

class Debts(db.Model):
    id = db.column(db.Integer, primary_key = True, autoincrement = True)
    value = db.column(db.Float)
    description = db.column(db.String(180))
    due_date = db.column(db.DateTime)
    document_date = db.column(db.DateTime)

    spending_id = db.Column(db.Integer, db.ForeignKey('spending.debts'), nullable = False)    

    def __init__(self, debts):
        self.value = debts['value']
        self.description = debts['description']
        self.due_date = debts['due_date']
        self.document_date = debts['document_date']
