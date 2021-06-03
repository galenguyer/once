from flask import Flask
from config import Config

once = Flask(__name__)
once.config.from_object(Config)

from once import routes
