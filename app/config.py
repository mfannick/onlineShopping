import os
class Config:
    '''
    General configuration parent class
    '''
    
    SECRET_KEY ='Fannick'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://annick:escofavi@localhost/shopping'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

     #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
    
    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://annick:escofavi@localhost/shopping_test'


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://annick:escofavi@localhost/shopping'
    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
 
