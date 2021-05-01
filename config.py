# config file

class Config(object):
    """ config for all env """


class DevConfig(Config):
    """ dev config """

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProdConfig(Config):
    """ prod config"""

    DEBUG = False


app_config = {
    'dev': DevConfig,
    'prod': ProdConfig
}
