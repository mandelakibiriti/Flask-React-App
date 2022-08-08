from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from flask import Flask
from flask_assets import Environment
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    # Initialize FastAPI app
    app = FastAPI()
    
    # Initialize core Flask app
    flaskapp = Flask(__name__,instance_relative_config=False)
    flaskapp.config.from_object('config.Config')

    # Initialize db
    db.init_app(flaskapp)

    # Initialize Assets Package
    assets = Environment()
    assets.init_app(flaskapp)

    # Application Context - here are all the pieces
    # of the Flask App are declared
    with flaskapp.app_context():
        
        # home - assets, blueprints, routes
        from .home import routes
        from . import forms
        from .assets import compile_static_assets

        # Register Blueprints
        flaskapp.register_blueprint(home.routes.home_bp)
        flaskapp.register_blueprint(forms.form_bp)

        # Compile static assets
        compile_static_assets(assets)  # Execute logic

        # Get routers
        from .fastAPI.routers import api_router, db_router

        # Register routers
        app.include_router(api_router.router)
        app.include_router(db_router.router)
        
        # Mount flask app to fastapi app
        app.mount("/vf", WSGIMiddleware(flaskapp))

        # Our database lives 
        db.create_all()
    
    return app