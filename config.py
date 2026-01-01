import os
from os import environ

class Config:
    DEBUG = False
    TESTING = False

    BASEDIR = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = environ.get("SECRET_KEY", "pctdanalysis")

    UPLOADS = os.path.join(BASEDIR, "app", "static", "uploads")
    ORIGINAL_DIR = os.path.join(BASEDIR, "app", "static", "original")
    GENERATED_DIR = os.path.join(BASEDIR, "app", "static", "generated")
    ORIGINAL_FILE = os.path.join(ORIGINAL_DIR, "original.jpg")

    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True
    SESSION_COOKIE_SECURE = False
