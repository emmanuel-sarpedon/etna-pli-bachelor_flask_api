import os
import sys


def check_if_env_variable_exists(variable):
    try:
        os.environ[variable]
    except KeyError:
        print(repr("Please set the environment variable " + variable))
        sys.exit(1)


required_variables = ("DB", "FLASK_ENV", "FLASK_DEBUG")
for env in required_variables:
    check_if_env_variable_exists(env)

DB = os.environ.get("DB")
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_DATABASE_URI_LOCAL = os.environ.get("SQLALCHEMY_DATABASE_URI_LOCAL")
FLASK_ENV = os.environ.get("FLASK_ENV")
FLASK_DEBUG = os.environ.get("FLASK_DEBUG")

postgresConn = SQLALCHEMY_DATABASE_URI if DB == "cloud" else SQLALCHEMY_DATABASE_URI_LOCAL
env = FLASK_ENV
debug = FLASK_DEBUG
