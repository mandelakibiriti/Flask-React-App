from flask import current_app as app
from flask_assets import Bundle

def compile_static_assets(assets):
    assets.auto_build = True
    assets.debug = False
    
    home_common_css_bundle = Bundle(
        'home_bp/src/index.css',
        output='build/css/home.css',
        extra={'rel': 'stylesheet/css'}
    )

    home_common_js_bundle = Bundle(
        'home_bp/src/index.js',
        output='build/js/home.js'
    )

    assets.register('home.css',home_common_css_bundle,)
    assets.register('home.js',home_common_js_bundle)

    if app.config['FLASK_ENV'] == 'development':
        # Build bundles
        home_common_css_bundle.build()
        home_common_js_bundle.build()

    return assets