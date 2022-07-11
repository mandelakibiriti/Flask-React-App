from os import environ, path

# Base folder dir path
base_dir = path.abspath(path.dirname(__file__))

class Config:
    # Flask Configuration
    TESTING = True
    DEBUG = True
    FLASK_ENV = 'development'
    SECRET_KEY = environ.get('SECRET_KEY')

    # Front end assests
    ASSETS_DEBUG = False
    ASSETS_AUTO_BUILD = True
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'