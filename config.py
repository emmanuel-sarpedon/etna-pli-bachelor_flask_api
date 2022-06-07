import os
import sys


def check_if_env_variable_exists(variable):
    try:
        os.environ[variable]
    except KeyError:
        print(repr("Please set the environment variable " + variable))
        sys.exit(1)


required_variables = ("DB", "FLASK_ENV", "FLASK_DEBUG", "SMTP_EMAIL_USER", "SMTP_EMAIL_PASSWORD")

for env in required_variables:
    check_if_env_variable_exists(env)

DB = os.environ.get("DB")
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_DATABASE_URI_LOCAL = os.environ.get("SQLALCHEMY_DATABASE_URI_LOCAL")

# App config
postgresConn = SQLALCHEMY_DATABASE_URI if DB == "cloud" else SQLALCHEMY_DATABASE_URI_LOCAL
env = os.environ.get("FLASK_ENV")
debug = os.environ.get("FLASK_DEBUG")
email_sender = os.environ.get("SMTP_EMAIL_USER")
email_pwd = os.environ.get("SMTP_EMAIL_PASSWORD")
