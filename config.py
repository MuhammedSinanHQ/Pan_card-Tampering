import os
from os import environ

class Config(object):

    DEBUG = False
    TESTING = False

    basedir = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = environ.get('SECRET_KEY') or 'sinanpythonflaskpancardtamperingapp'

    # Use relative paths from basedir
    UPLOADS = os.path.join(basedir, "app", "static", "uploads")

    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None


class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False


class DebugConfig(Config):
    DEBUG = False


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
