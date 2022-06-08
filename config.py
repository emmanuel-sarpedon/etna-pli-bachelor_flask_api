import os

DB = os.environ.get("DB")
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_DATABASE_URI_LOCAL = os.environ.get("SQLALCHEMY_DATABASE_URI_LOCAL")

# App config
postgresConn = SQLALCHEMY_DATABASE_URI if DB == "cloud" else SQLALCHEMY_DATABASE_URI_LOCAL
env = os.environ.get("FLASK_ENV")
debug = os.environ.get("FLASK_DEBUG")
smtp_server = os.environ.get("SMTP_EMAIL_SERVER")
smtp_port = os.environ.get("SMTP_EMAIL_PORT")
email_sender = os.environ.get("SMTP_EMAIL_USER")
email_pwd = os.environ.get("SMTP_EMAIL_PASSWORD")
