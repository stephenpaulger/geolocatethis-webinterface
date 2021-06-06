from os import environ, path
from dotenv import load_dotenv
from secrets import token_hex

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    FLASK_ENV = environ.get("FLASK_ENV", "development")
    SECRET_KEY = environ.get("SECRET_KEY", token_hex(16))
    GMAPS_AUTH_KEY = environ.get("GMAPS_AUTH_KEY")
