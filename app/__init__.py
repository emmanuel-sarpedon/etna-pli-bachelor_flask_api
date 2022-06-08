import config

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail

import routes.auth as auth

migrate = Migrate()


def create_app():
    _app = Flask(__name__)

    # General configuration
    _app.config['FLASK_ENV'] = config.env
    _app.config['DEBUG'] = config.debug

    # Database and model
    _app.config['SQLALCHEMY_DATABASE_URI'] = config.postgresConn
    _app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from model import db, User

    db.init_app(_app)
    # with _app.app_context():
    #     db.create_all()
    #     db.session.commit()

    migrate.init_app(_app, db)
    # Endpoint registration
    _app.register_blueprint(auth.bp)

    # SMTP Mail
    _app.config.update({
        "MAIL_SERVER": config.smtp_server,
        "MAIL_DEBUG": False,
        "MAIL_PORT": config.smtp_port,
        "MAIL_USE_TLS": False,
        "MAIL_USE_SSL": True,
        "MAIL_USERNAME": config.email_sender,
        "MAIL_PASSWORD": config.email_pwd
    })

    mail = Mail()
    mail.init_app(_app)

    return _app


app = create_app()
# app.app_context().push()

# if __name__ == '__main__':
#     app.run()
