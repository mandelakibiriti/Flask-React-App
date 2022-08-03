from os import environ, path
from dotenv import load_dotenv

# Base folder dir path
base_dir = path.abspath(path.dirname(__file__))
load_dotenv (path.join(base_dir,'.env'))

class Config:
    # Flask Configuration
    TESTING = True
    DEBUG = True
    FLASK_ENV = 'development'
    SECRET_KEY = environ.get('SECRET_KEY')

    # Database
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + environ.get('Db_Username') + ':' + environ.get('Db_Password') + '@' + environ.get('Db_Host') + ':3306/' + environ.get('Db_Name')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Front end assests
    ASSETS_DEBUG = False
    ASSETS_AUTO_BUILD = True
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'