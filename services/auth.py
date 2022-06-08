from model import User, db
from werkzeug.security import generate_password_hash
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message, Mail
import config

mail = Mail()


def throw_error_user_already_exists():
    return {"error": {"message": "User already exists"}}


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


def send_confirmation_code(email, token):
    msg = Message(subject="Vérification de votre adresse mail",
                  sender=config.email_sender,
                  recipients=[email],
                  body='Voici votre token de confirmation : {}'.format(token))

    mail.send(msg)
