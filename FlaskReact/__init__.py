from flask import Flask
from flask_assets import Environment

def init_app():
    # Initialize core app
    app = Flask(__name__,instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize Assets Package
    assets = Environment()
    assets.init_app(app)

    # Application Context - here are all the pieces
    # of the Flask App are declared
    with app.app_context():
        # home - assets, blueprints, routes
        from .home import routes
        from .assets import compile_static_assets
        app.register_blueprint(home.routes.home_bp)
        compile_static_assets(assets)

    return app