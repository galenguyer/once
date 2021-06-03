import os
import secrets
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get("ONCE_SECRET_KEY") or "".join(secrets.token_hex(16))
    # SQLAlchemy config
    SQLALCHEMY_DATABASE_URI = os.environ.get("ONCE_DATABASE_URI", f"sqlite:///{os.path.join(basedir, 'once.db')}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
