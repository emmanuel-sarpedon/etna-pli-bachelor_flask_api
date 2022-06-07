import config

from flask import Flask
from flask_migrate import Migrate
from flask_mail import Mail
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

# SMTP Mail
app.config.update({
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_DEBUG": False,
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": config.email_sender,
    "MAIL_PASSWORD": config.email_pwd
})

mail = Mail()
mail.init_app(app)

if __name__ == '__main__':
    app.run()
