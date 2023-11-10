from backend.database import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    items = db.Column(db.String(255), nullable=False)