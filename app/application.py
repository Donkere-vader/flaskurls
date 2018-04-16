from __future__ import print_function
from flask import Flask




__all__ = ['create_app']


def create_app():
    app = Flask("Blub", template_folder="app/templates", static_folder="app/static")
    configure_blueprints(app)
    return app


def configure_blueprints(app):
    from app.blueprints.home.views import user_stats
    app.register_blueprint(user_stats)




