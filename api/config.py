import os
from dotenv import load_dotenv

# load env variables
load_dotenv('.env')


class Config:
    '''
        Base config class. Holds default config seetings for the app
    '''

    # define default configs
    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY', default='')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    '''
        config class to define developement environment configuration for the app
    '''
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URL_DEV', default='')

class ProductionConfig(Config):
    '''
        config class to define Production environment configuration
    '''
    FLASK_ENV = "production"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URL_PROD', default='')

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True