from model import User, db
from werkzeug.security import generate_password_hash
from itsdangerous import URLSafeTimedSerializer
from flask import render_template, copy_current_request_context
from flask_mail import Message, Mail
from datetime import date
import config

mail = Mail()


def get_user_by_email(email):
    return User.query.filter_by(email=email).first()


def is_user_already_registered(email):
    return bool(get_user_by_email(email))


def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(config.secret_key)
    return serializer.dumps(email, salt=config.security_pwd_salt)


def register_new_user(firstname, lastname, email, password, confirmation_token):
    new_user = User(firstname=firstname,
                    lastname=lastname,
                    email=email,
                    confirmation_token=confirmation_token,
                    is_email_validated=False,
                    password=generate_password_hash(password))

    update_user_on_database(new_user)

    user_created = new_user.asdict()

    return {
        'message': 'User created',
        'user_created': {
            '_id': user_created["id_user"],
            'firstname': user_created["firstname"],
            'lastnamed': user_created["lastname"],
            'email': user_created["email"]
        }
    }


def send_confirmation_code(email, token):
    msg = Message(subject="Vérification de votre adresse mail",
                  sender=config.email_sender,
                  recipients=[email])

    msg.html = render_template("auth_verify_email.html", url='{}/users/confirm-email/{}'.format(config.domain, token))

    mail.send(msg)


def check_confirmation_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(config.secret_key)

    return serializer.loads(token, salt=config.security_pwd_salt, max_age=expiration)


def validate_account_email(email):
    user = User.query.filter_by(email=email).first()

    user.is_email_validated = True
    user.date_of_email_validation = date.today()
    user.confirmation_token = None

    update_user_on_database(user)

    return {"message": "email validated"}


def update_user_on_database(user):
    db.session.add(user)
    db.session.commit()
