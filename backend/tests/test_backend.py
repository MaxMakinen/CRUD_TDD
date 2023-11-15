from backend.adtd_flask.models import Task
from backend.adtd_flask.database import db
import pytest

# Test if the /hello endpoint returns "Hello world"
def test_request_example(client):
    response = client.get("/hello")
    assert b"Hello world" in response.data

# Fixture to provide app context for the tests
@pytest.fixture
def app_ctx(app):
    with app.app_context():
        yield

# Test if a Task can be created and committed to the database
@pytest.mark.usefixtures("app_ctx")
def test_task_model():
    task1 = Task()
    db.session.add(task1)
    db.session.commit()

# Test if multiple Tasks can be created, committed to the database, and then retrieved
@pytest.mark.usefixtures("app_ctx")
def test_task_new():
    task1 = Task()
    task2 = Task("Test task", "Test description")
    db.session.add(task1)
    db.session.add(task2)
    db.session.commit()
    result = db.session.query(Task).all()
    assert task2 in result