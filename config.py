import os
from os import environ

class Config(object):

    DEBUG = False
    TESTING = False

    basedir = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = environ.get('SECRET_KEY') or 'sinanpythonflaskpancardtamperingapp'

    # Maximum file upload size (16MB default)
    MAX_CONTENT_LENGTH = int(environ.get('MAX_CONTENT_LENGTH', 16777216))

    # Use relative paths from basedir
    UPLOADS = os.path.join(basedir, "app", "static", "uploads")
    
    # Path to original PAN card for comparison
    ORIGINAL_PAN_CARD_PATH = os.path.join(basedir, "sample_data", "image", "original.png")

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
