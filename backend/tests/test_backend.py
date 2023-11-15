#from backend.adtd_flask.database import db
from backend.adtd_flask.models import Task
from backend.adtd_flask.database import db
#from sqlalchemy import create_engine
import pytest
import conftest

def test_request_example(client):
    response = client.get("/hello")
    assert b"Hello world" in response.data

@pytest.fixture
def app_ctx(app):
    with app.app_context():
        yield

@pytest.mark.usefixtures("app_ctx")
def test_task_model():
    task1 = Task()
    db.session.add(task1)
    db.session.commit()

@pytest.mark.usefixtures("app_ctx")
def test_task_new():
    task1 = Task()
    task2 = Task("Test task", "Test description")
    db.session.add(task1)
    db.session.add(task2)
    db.session.commit()
    result = db.session.query(Task).all()
    # for r in result:
        # print(r)
    assert task2 in result

# @pytest.mark.usefixtures("app_ctx")
# def test_task_update():
    # task = Task("Initial task", "Initial description")
    # db.session.add(task)
    # db.session.commit()
    # initial = db.session.query(Task).all()
    # db.session.flush()
    # task.name = "Updated name"
    # task.description = "Updated description"
    # db.session.commit()
    # updated = db.session.query(Task).all()
    # assert initial != updated
 




