
# import pytest
# import json
# from requests import put
# from backend.adtd_flask.models import Tasks
# from backend.adtd_flask.database import db

# @pytest.fixture
# def client():
#     app.config['TESTING'] = True
#     client = app.test_client()

#     # Create a test item for updating
#     with app.app_context():
#         test_task = Item(task='Test Item', description='Initial Description')
#         db.session.add(test_task)
#         db.session.commit()

#     yield client, test_task  # Return both the client and the test_task

# def test_update_task(client):
#     client, test_task = client  # Unpack the client and test_task from the fixture

#     # Send an update request
#     update_data = {'task': 'Updated Item', 'description': 'Updated Description'}
#     response = client.put(f'/items/{test_task.id}', json=update_data)

#     # Check the response
#     assert response.status_code == 200  # Assuming 200 is the success status code

#     # Retrieve the updated task from the database with an active session
#     with app.app_context():
#         # Refresh the test_task within the active session
#         db.session.expunge_all()  # Expunge any detached instances
#         updated_task = Item.query.get(test_task.id)
#         db.session.refresh(updated_task)

#     # Assert the changes
#     assert updated_task.task == 'Updated Item'
#     assert updated_task.description == 'Updated Description'