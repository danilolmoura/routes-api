import os

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ['SECRET_KEY']
    POTION_DEFAULT_PER_PAGE = 20

config_by_name = dict(
    dev='config.config_dev.ConfigDev',
    test='config.config_test.ConfigTest',
    prod='config.config_test.ConfigProd'
)
