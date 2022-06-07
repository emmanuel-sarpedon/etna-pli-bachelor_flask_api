import config

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from routes import auth

app = Flask(__name__)

# General configuration
app.config['FLASK_ENV'] = config.env
app.config['DEBUG'] = config.debug

# Database and model
app.config['SQLALCHEMY_DATABASE_URI'] = config.postgresConn
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)

# Endpoint registration
app.register_blueprint(auth.bp)


if __name__ == '__main__':
    app.run()
