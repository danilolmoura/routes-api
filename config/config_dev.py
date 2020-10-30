import os

from config import Config

class ConfigDev(Config):
    DEVELOPMENT = True
    DEBUG = True
    FLASK_ENV = 'development'
