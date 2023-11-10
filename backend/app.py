from flask import Flask, jsonify
from backend.database import db
from backend.models import Item

app = Flask(__name__)

# SQLite database file will be created in the 'database' directory
database_path = 'sqlite:///database/database.sqlite'

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