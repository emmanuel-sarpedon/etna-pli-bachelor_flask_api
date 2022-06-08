from model import User, db
from werkzeug.security import generate_password_hash
from itsdangerous import URLSafeTimedSerializer, exc
from flask import render_template
from flask_mail import Message, Mail
from datetime import date
import config

mail = Mail()


def throw_error_user_already_exists():
    return {"error": {"message": "User already exists"}}


def throw_error_token_is_denied():
    return {"error": {"message": "Token denied"}}


def is_user_already_registered(email):
    return bool(User.query.filter_by(email=email).first())


def register_new_user(firstname, lastname, email, password, confirmation_token):
    new_user = User(firstname=firstname,
                    lastname=lastname,
                    email=email,
                    confirmation_token=confirmation_token,
                    is_email_validated=False,
                    password=generate_password_hash(password))

    db.session.add(new_user)
    db.session.commit()

    user_created = new_user.asdict()

    return {
        'message': 'User created',
        'user_created': {
            '_id': user_created["id_user"],
            'firstname': user_created["firstname"],
            '_ilastnamed': user_created["lastname"],
            'email': user_created["email"]
        }
    }


def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(config.secret_key)
    return serializer.dumps(email, salt=config.security_pwd_salt)


def check_confirmation_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(config.secret_key)

    try:
        email = serializer.loads(token, salt=config.security_pwd_salt, max_age=expiration)
    except exc:
        return False

    return email


def send_confirmation_code(email, token):
    msg = Message(subject="Vérification de votre adresse mail",
                  sender=config.email_sender,
                  recipients=[email])

    msg.html = render_template("auth_verify_email.html", url='{}/auth/confirm/{}'.format(config.domain, token))

    mail.send(msg)


def validate_account_email(email):
    user = User.query.filter_by(email=email).first()

    user.is_email_validated = True
    user.date_of_email_validation = date.today()
    user.confirmation_token = None

    db.session.add(user)
    db.session.commit()

    return {"message": "email validated"}
