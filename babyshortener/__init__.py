from flask import Flask
from werkzeug.utils import find_modules, import_string
from babyshortener.extensions import db
from babyshortener.config import DefaultConfig

# ----------------------------------------------------------------------------------------------------------------------


def create_app(config=DefaultConfig()):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    return app

# ----------------------------------------------------------------------------------------------------------------------


def register_extensions(app):
    db.init_app(app)


# ----------------------------------------------------------------------------------------------------------------------


def register_blueprints(app):
    for name in find_modules('babyshortener.blueprints'):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp)


# ----------------------------------------------------------------------------------------------------------------------


