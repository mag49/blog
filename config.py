# class Config:
#     '''
#     General configuration parent class
#     '''
#     SECRET_KEY = 'maggie'
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:word@localhost/blog'
import os
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = 'maggie'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:word@localhost/blog'

    #  email configurations
    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # SUBJECT_PREFIX = 'Pitch'
    # SENDER_EMAIL = 'ciru930@gmail.com'
class ProdConfig(Config):
    '''
    Production configuration child class
    '''
    pass
class DevConfig(Config):
    '''
    Development configuration child class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:word@localhost/blog'
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}
