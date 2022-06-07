import config

from flask import Flask
from flask_migrate import Migrate
from models.user import db
from routes import auth

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.postgresConn
app.config['FLASK_ENV'] = config.env
app.config['DEBUG'] = config.debug
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(auth.bp)
db.init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()
