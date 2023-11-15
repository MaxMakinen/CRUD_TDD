import os
import tempfile
import pytest
from backend.adtd_flask import create_app
#from backend.adtd_flask.models import Task, db
from backend.adtd_flask.database import db

@pytest.fixture
def app():
    app = create_app({
        'TESTING':True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///',
    })

    with app.app_context():
        # Create all tables in database
        db.create_all()
    
    yield app

# Fixture for creating a test client
@pytest.fixture
def client(app):
    return app.test_client()

# Fixture for creating a test CLI runner
@pytest.fixture
def runner(app):
    return app.test_cli_runner()

# Class for handling authentication actions in tests
class AuthActions(object):
    def __init__(self, client):
        self._client = client

        # Method for logging in a test user
        def login(self, username='test', password='test'):
            return self._client.post(
                '/auth/login',
                data={'username':username, 'password':password}
            )
        
        # Method for logging out a test user
        def logout(self):
            return self._client.get('/auth/logout')

@pytest.fixture
def auth(client):
    return AuthActions(client)