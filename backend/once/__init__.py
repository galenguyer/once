from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

once = Flask(__name__)
once.config.from_object(Config)
once.config["JSON_SORT_KEYS"] = False
db = SQLAlchemy(once)
migrate = Migrate(once, db)

from once import routes, errors, models


@once.after_request
def add_header(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response
