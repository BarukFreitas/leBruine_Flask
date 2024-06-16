from flask import Flask
from flask_migrate import Migrate
from config import Config
from db import db
from routes import init_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = 'your_secret_key'

    db.init_app(app)
    migrate = Migrate(app, db)

    init_routes(app)

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
