from flask_sqlalchemy import SQLAlchemy, inspect
# from app import create_app
import config

db = SQLAlchemy()


class User(db.Model):
    id_user = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    is_email_validated = db.Column(db.Boolean, nullable=False)
    date_of_email_validation = db.Column(db.Date, nullable=True)
    phone_number = db.Column(db.String(20))
    password = db.Column(db.String, nullable=False)

    def asdict(self):
        return {c.key: getattr(self, c.key)
                for c in inspect(self).mapper.column_attrs}



