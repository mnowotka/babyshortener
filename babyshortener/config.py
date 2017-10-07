# ----------------------------------------------------------------------------------------------------------------------


class DefaultConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = 'filesystem'
    SECRET_KEY = 'change me!!'

# ----------------------------------------------------------------------------------------------------------------------


class ProductionConfig(DefaultConfig):
    DATABASE_URI = 'mysql://user@localhost/foo'

# ----------------------------------------------------------------------------------------------------------------------


class DevelopmentConfig(DefaultConfig):
    DEBUG = True

# ----------------------------------------------------------------------------------------------------------------------


class TestingConfig(DefaultConfig):
    TESTING = True

# ----------------------------------------------------------------------------------------------------------------------
