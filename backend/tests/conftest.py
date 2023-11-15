import os
import tempfile
import pytest
from backend.adtd_flask import create_app
#from backend.adtd_flask.models import Task, db
from backend.adtd_flask.database import db

@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app({
        'TESTING':True,
        'DATABASE': db_path,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///',
    })

    with app.app_context():
#        db.init_app(app)
        db.create_all()
    
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()