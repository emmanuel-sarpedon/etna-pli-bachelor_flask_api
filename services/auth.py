from model import User, db
from werkzeug.security import generate_password_hash
from itsdangerous import URLSafeTimedSerializer
from flask import request
from flask_mail import Message, Mail
from datetime import date
import config
import jwt

mail = Mail()


def get_user_by_email(email):
    """
    "Get the first user with the given email."

    :param email: The email address of the user you want to retrieve
    :return: The first user with the email address that matches the email argument.
    """
    return User.query.filter_by(email=email).first()


def is_user_already_registered(email):
    """
    "Return True if the user is already registered, False otherwise."

    The function is_user_already_registered() takes an email address as an argument and returns True if the user is
    already registered, False otherwise

    :param email: The email address of the user
    :return: A boolean value.
    """
    return bool(get_user_by_email(email))


def generate_confirmation_token(email):
    """
    It takes an email address, and returns a token that can be used to confirm that email address

    :param email: The email address of the user to confirm
    :return: A token that is generated from the email address.
    """
    serializer = URLSafeTimedSerializer(config.secret_key)
    return serializer.dumps(email, salt=config.security_pwd_salt)


def register_new_user(firstname, lastname, email, password, confirmation_token):
    """
    It creates a new user in the database

    :param firstname: The first name of the user
    :param lastname: The last name of the user
    :param email: The email address of the user
    :param password: The password that the user will use to login
    :param confirmation_token: a random string that will be used to validate the user's email address
    :return: A dictionary with a message and a user_created key.
    """
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
            'lastname': user_created["lastname"],
            'email': user_created["email"]
        }
    }


def send_confirmation_code(email, token):
    """
    It sends an email to the user with a link to confirm their email address

    :param email: The email address of the user
    :param token: The token that was generated in the previous step
    """
    msg = Message(subject="Vérification de votre adresse mail",
                  sender=config.email_sender,
                  recipients=[email])

    msg.body = 'Pour confirmer votre adresse mail, utilisez ce lien : {}/users/confirm-email/{}'.format(request.host_url, token)

    mail.send(msg)


def check_confirmation_token(token, expiration=3600):
    """
    It takes a token and expiration time, and returns the token if it's valid

    :param token: The token that was sent to the user
    :param expiration: The number of seconds the token is valid for, defaults to 3600 (optional)
    :return: The user's email address.
    """
    serializer = URLSafeTimedSerializer(config.secret_key)

    return serializer.loads(token, salt=config.security_pwd_salt, max_age=expiration)


def validate_account_email(email):
    """
    It validates the email of the user

    :param email: The email address of the user to validate
    :return: A dictionary with a message.
    """
    user = User.query.filter_by(email=email).first()

    user.is_email_validated = True
    user.date_of_email_validation = date.today()
    user.confirmation_token = None

    update_user_on_database(user)

    return {"message": "email validated"}


def update_user_on_database(user):
    """
    "Add the user to the database and commit the changes."

    The first line of the function is the most important. It tells the database that the user object has been modified and
    needs to be saved

    :param user: The user object that you want to update
    """
    db.session.add(user)
    db.session.commit()


def log_in(email):
    """
    It takes an email address, and returns a JSON object with a JWT

    :param email: The email of the user to log in
    :return: A dictionary with a key of jwt and a value of the encoded email.
    """
    return {"jwt": jwt.encode({"email": email}, config.secret_key, algorithm="HS256")}
