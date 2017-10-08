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
    register_cli(app)
    return app

# ----------------------------------------------------------------------------------------------------------------------


def register_extensions(app):
    db.init_app(app)


# ----------------------------------------------------------------------------------------------------------------------


def register_blueprints(app):
    for name in find_modules('babyshortener.blueprints', include_packages=True):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp)


# ----------------------------------------------------------------------------------------------------------------------

def register_cli(app):
    @app.cli.command('initdb')
    def initdb_command():
        db.create_all()
        print('Initialized the database.')

    @app.cli.command('cleardb')
    def initdb_command():
        db.drop_all()
        print('Dropped the database.')

    @app.cli.command('refreshdb')
    def initdb_command():
        db.drop_all()
        db.create_all()
        print('Recreated the database.')

# ----------------------------------------------------------------------------------------------------------------------


