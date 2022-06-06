import os

postgresConn = os.environ.get("SQLALCHEMY_DATABASE_URI")
env = os.environ.get("FLASK_ENV")
debug = os.environ.get("FLASK_DEBUG")
