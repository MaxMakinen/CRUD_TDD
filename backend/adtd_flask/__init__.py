from flask import Flask
#from .models import db, Task
from .database import db
import os

# Application factory function
def create_app(test_config=None):
    # Create and confgigure app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'database.sqlite'),
    )

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'database.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialize the database
    db.init_app(app)

    # Create tables
    with app.app_context():
        db.create_all()

    # Sample route to test database connection
    @app.route('/hello')
    def hello():
        return 'Hello world!'

    # Register blueprint for user authentication
    from . import auth
    app.register_blueprint(auth.bp)

    return app

# if __name__ == '__main__':
#     app.run(debug=True)