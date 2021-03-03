from flask import Flask
from lib.core.appdata import config


def create_app():
    app = Flask(config.app.name)
    with app.app_context():
        # init

        # other func(404...)

        # import Blueprint
        from web.api import api_home
        from web.api import api_scan

        # register Blueprint
        app.register_blueprint(api_home, url_prefix='/')
        app.register_blueprint(api_scan, url_prefix='/api/scan/')

        return app
