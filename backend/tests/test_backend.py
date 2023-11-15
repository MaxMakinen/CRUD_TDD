# original tests
# from test_database import *

# Testing after including SQLAlchemy
from backend.app import app, db
from sqlalchemy import inspect
from backend.models import Item

# database_path = '../database/database.sqlite'
# table_name = 'mlem'
# 
# 
# def test_database_presence():
    # assert is_database_present(database_path)
# 
# def test_database_table_presence():
    # assert is_table_present(database_path, table_name)
# 
def test_items_table_exists():
    with app.app_context():
        inspector = inspect(db.engine)
        actual_table_names = inspector.get_table_names()
        expected_table_name = Item.__table__.name
        print("actual_table_names = {}\nexpected_table_name = {}".format(actual_table_names, expected_table_name))
        assert expected_table_name in actual_table_names

def test_add_new_item():
    with app.app_context():
        # Ensure the 'items' table is empty before adding a new item
        db.session.query(Item).delete()
        db.session.commit()

        # Add a new item
        new_item = Item(task='New task', description='Original description')
        db.session.add(new_item)
        db.session.commit()

        # Query the 'items' table to check if the new item was added
        items = Item.query.all()
        assert len(items) == 1
        assert items[0].task == 'New task'

# Add more tests for other CRUD operations if needed