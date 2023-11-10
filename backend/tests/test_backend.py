# original tests
from test_database import *
#Tetsing after including SQLAlchemy
from backend.app import app, db
from sqlalchemy import inspect
from backend.models import Item

database_path = './backend/database/tasks.db'
table_name = 'tasks'


def test_database_presence():
    assert is_database_present(database_path)

def test_database_table_presence():
    assert is_table_present(database_path, table_name)

def test_items_table_exists():
    with app.app_context():
        inspector = inspect(db.engine)
        assert 'items' in inspector.get_table_names()