import os

from dotenv import load_dotenv


if not os.getenv("FLASK_SECRET_KEY", ""):
    load_dotenv()


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
    

class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DEV_DB_URI")


class ProductionConfig(Config):
    '''This production string does not exist yet'''
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")