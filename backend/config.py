import os
import secrets


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "".join(secrets.token_hex(16))