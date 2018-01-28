import os


class Config:
    """Main configurations class"""

    NEWS_API_KEY='2346cad2c3b344c8adc0026455aa8bd4'
    # NEWS_API_BASE_URL='https://newsapi.org/v2/sources/'





class ProdConfig(Config):
    """Production configuration class that inherits from the main configurations class"""
    pass


class DevConfig(Config):
    """Configuration class for development stage of the app"""
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
