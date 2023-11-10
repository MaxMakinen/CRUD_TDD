from flask import Flask, jsonify
from backend.database import db
from backend.models import Item
import os

app = Flask(__name__)

# Get absolute path
base_dir = os.path.abspath(os.path.dirname(__file__))
database_dir = os.path.join(base_dir, 'database')

# Create the 'database directory if it isn't present
os.makedirs(database_dir, exist_ok=True)

# SQLite database file will be created in the 'database' directory
database_path = 'sqlite:///' + os.path.join(database_dir, 'tasks.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = database_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()

# Sample route to test database connection
@app.route('/')
def hello():
    return 'Hello, this is your Flask backend with SQLAlchemy!'

if __name__ == '__main__':
    app.run(debug=True)