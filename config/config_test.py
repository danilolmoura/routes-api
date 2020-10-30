import os

from . import Config

class ConfigTest(Config):
    DEVELOPMENT = True
    DEBUG = True
    TESTING = True
    FLASK_ENV = 'testing'
