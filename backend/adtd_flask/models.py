# from .database import db

# class Tasks(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     task = db.Column(db.String(255), nullable=False)
#     description = db.Column(db.String(255), nullable=False)

from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime
from backend.adtd_flask.database import db


class Task(db.Model):
    __tablename__ = "tasks"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String, nullable=False)
    description = Column("description", String)
    created = Column("created", DateTime, nullable=False)
    updated = Column("updated", DateTime)
    
    def __init__(self, name="New task", description="No description"):
        self.name = name
        self.description = description
        self.created = datetime.now()
        # self.updated = self.created

    def __repr__(self):
        return f"({self.id}) {self.name}, {self.description} - {self.created} {self.updated}"

class User(db.Model):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True)
    username = Column("username", String, nullable=False, unique=True)
    password = Column("password", String, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        # return f"({self.id}) {self.username}, {self.password}"
        return f"({self.id}) {self.username}"