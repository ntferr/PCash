from app import db

class Debts(db.Model):
    id = db.column(db.Integer, primary_key = True)
    value = db.column(db.Float)
    description = db.column(db.String(180))
    due_date = db.column(db.DateTime)
    document_date = db.column(db.DateTime)

    spending = db.relantionship('Spending', backref = 'debts', lazy = True)
