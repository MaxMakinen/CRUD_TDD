

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate, upgrade, init as migrate_init
# from sqlalchemy import inspect
# import click
# import pytest
# from backend.models import Item
# from backend.app import app, db  # Import the existing SQLAlchemy instance
# from flask.cli import FlaskGroup  # Import FlaskGroup

# @pytest.fixture
# def test_app():
#     # Use a separate test configuration with a different database
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_database.sqlite'
#     return app


# @pytest.fixture
# def test_db(test_app):
#     # Use the existing SQLAlchemy instance from the main application
#     with test_app.app_context():
#         # Ensure that the database is not yet initialized to prevent the error
#         if not hasattr(db, 'session'):
#             db.init_app(test_app)
        
#         # Create a test database
#         db.create_all()

#         # Use FlaskGroup to initialize migrations (create 'migrations' folder)
#         with app.test_request_context():
#             flask_group = FlaskGroup(create_app=lambda _: app)
#             flask_group.main(['', 'db', 'init', '--directory', 'migrations'])

#             # Initialize and apply migrations
#             migrate = Migrate(app, db)
#             migrate.init_app(app)
#             migrate.upgrade()

#     return db

# def test_migration(test_app, test_db):
#     with test_app.app_context():
#         # Check if the 'description' column has been added to the 'items' table
#         inspector = inspect(test_db.engine)
#         columns = [col['name'] for col in inspector.get_columns('items')]
#         assert 'description' in columns

#         # Optionally, you can check if the new column works as expected
#         new_item = Item(name='Test Item', description='Test Description')
#         test_db.session.add(new_item)
#         test_db.session.commit()

#         retrieved_item = Item.query.filter_by(name='Test Item').first()
#         assert retrieved_item.description == 'Test Description'
