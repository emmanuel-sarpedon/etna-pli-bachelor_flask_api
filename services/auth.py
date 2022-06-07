import flask

from models.user import User, db
from werkzeug.security import generate_password_hash
from sqlalchemy import or_


def throw_error_user_already_exists():
    return {"error": {"message": "User already exists"}}


def is_user_already_registered(username, email):
    return bool(User.query.filter(or_(User.username == username, User.email == email)).first())


def register_new_user(username, email, password):
    new_user = User(username=username, email=email, password=generate_password_hash(password))

    db.session.add(new_user)
    db.session.commit()

    user_created = new_user.asdict()
    del user_created['password']

    return user_created
