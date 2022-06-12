import config

from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_swagger import swagger

migrate = Migrate()


def create_app():
    _app = Flask(__name__)

    # General configuration
    _app.config['SECRET_KEY'] = config.secret_key
    _app.config['FLASK_ENV'] = config.env
    _app.config['DEBUG'] = config.debug

    # Database and model
    _app.config['SQLALCHEMY_DATABASE_URI'] = config.postgresConn
    _app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from model import db

    db.init_app(_app)

    if config.DB == "cloud":
        with _app.app_context():  # -----------------------------
            db.create_all()       # -- For cloud database only --
            db.session.commit()   # -----------------------------

    else:
        migrate.init_app(_app, db)

    # Endpoint registration
    import routes.root as root
    import routes.users as users
    _app.register_blueprint(root.bp)
    _app.register_blueprint(users.bp)

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

    from services.auth import mail
    mail.init_app(_app)

    # Swagger documentation
    import routes.swagger as specs
    _app.register_blueprint(specs.swaggerui_blueprint)

    @_app.route('/api/specs')
    def spec():
        swag = swagger(
            _app,
            template={
                "info": {
                    "version": "0.1.0",
                    "title": "Flask"
                }
            })

        return jsonify(swag)

    return _app


app = create_app()
