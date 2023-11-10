from flask import Flask, jsonify
from backend.database import db
from backend.models import Item

app = Flask(__name__)

# Replace 'sqlite:///database.sqlite' with the actual connection URL for your database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
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