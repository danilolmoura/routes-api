import os

from config import Config

class ConfigProd(Config):
    DEVELOPMENT = False
    DEBUG = False
    FLASK_ENV = 'production'
