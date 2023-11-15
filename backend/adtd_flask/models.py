# from .database import db

# class Tasks(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     task = db.Column(db.String(255), nullable=False)
#     description = db.Column(db.String(255), nullable=False)

from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import declarative_base
from flask_sqlalchemy import SQLAlchemy
from itertools import count


Base = declarative_base()
db = SQLAlchemy(model_class=Base)

class Task(db.Model):
    __tablename__ = "tasks"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String, nullable=False)
    description = Column("description", String)
    created = Column("created", DateTime, nullable=False)
    updated = Column("updated", DateTime)
    
    def __init__(self, name="New task", description=""):
        self.name = name
        self.description = description
        self.created = datetime.now()
        # self.updated = self.created

    def __repr__(self):
        return f"({self.id}) {self.name} {self.description} {self.created} {self.updated}"
