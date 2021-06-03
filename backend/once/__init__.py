from flask import Flask
from config import Config

once = Flask(__name__)
once.config.from_object(Config)
once.config['JSON_SORT_KEYS'] = False

from once import routes
from once import errors
