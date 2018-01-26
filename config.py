class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_KEY='2346cad2c3b344c8adc0026455aa8bd4'
    NEWS_API_BASE_URL='https://newsapi.org/v1/sources/'
    SECRET_KEY='12345'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True