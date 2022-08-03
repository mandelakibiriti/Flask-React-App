from flask import Flask
from flask_assets import Environment
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    # Initialize core app
    app = Flask(__name__,instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize db
    db.init_app(app)

    # Initialize Assets Package
    assets = Environment()
    assets.init_app(app)

    # Application Context - here are all the pieces
    # of the Flask App are declared
    with app.app_context():
        
        # home - assets, blueprints, routes
        from .home import routes
        from . import forms
        from .assets import compile_static_assets

        # Register Blueprints
        app.register_blueprint(home.routes.home_bp)
        app.register_blueprint(forms.form_bp)

        # Compile static assets
        compile_static_assets(assets)  # Execute logic

        # Our database lives 
        db.create_all()
    return app