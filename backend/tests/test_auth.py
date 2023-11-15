import pytest
from flask import g, session
from backend.adtd_flask.database import db

def test_register(client, app):
    assert client.get('/auth/register').status_code == 200
    response = client.post(
        '/auth/register', data={'username':'a', 'password':'a'}
    )
    assert response.headers['Location'] == '/auth/login'

    with app.app_context():
        assert db.session.query(User).filter_by(username='a').first() is not None

@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('', '', b'Username is required.'),
    ('a', '', b'Password is required.'),
    ('test', 'test', b'already registered'),
))

def test_register_validate_input(client, username, password, message):
    response = client.post(
        '/auth/register', data={'username':username, 'password':password}
    )
    assert message in response.data
