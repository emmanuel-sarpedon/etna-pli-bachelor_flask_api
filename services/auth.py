from model import User, db
from werkzeug.security import generate_password_hash
from flask_sqlalchemy import SQLAlchemy


def throw_error_user_already_exists():
    return {"error": {"message": "User already exists"}}


def is_user_already_registered(email):
    return bool(User.query.filter_by(email=email).first())


def register_new_user(firstname, lastname, email, password):
    new_user = User(firstname=firstname,
                    lastname=lastname,
                    email=email,
                    is_email_validated=False,
                    password=generate_password_hash(password))

    # db = SQLAlchemy()
    db.session.add(new_user)
    db.session.commit()

    user_created = new_user.asdict()
    del user_created['password']

    return user_created
