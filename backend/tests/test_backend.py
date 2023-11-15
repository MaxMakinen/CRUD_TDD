#from backend.adtd_flask.database import db
from backend.adtd_flask.models import Task, db
from sqlalchemy import create_engine
import conftest

def test_request_example(client):
    response = client.get("/hello")
    assert b"Hello world" in response.data

def test_task_model(app):
    task = Task()
    with app.app_context():
        db.session.add(task)
        db.session.commit()