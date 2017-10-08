from flask import Flask
from werkzeug.utils import find_modules, import_string
from babyshortener.extensions import db
from babyshortener.config import DefaultConfig

# ----------------------------------------------------------------------------------------------------------------------


def create_app(config=DefaultConfig()):
    """
    A factory function, depending on convetion it can actually be called "factory", I decided that 'create_app' is just
    more verbose.
    Some common stuff goes here like registering extensions (I'm already using some and there can be more), 
    registering blueprints and commands.
    """
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    register_cli(app)
    return app

# ----------------------------------------------------------------------------------------------------------------------


def register_extensions(app):
    """
    This is the only place that we iterate through all extensions are introduce it to our application.
    This can be done in a more dynamic way, than just iterating through all extensions manually.
    Not too DRY, I'd say but I don't have time for that now.
    """
    db.init_app(app)


# ----------------------------------------------------------------------------------------------------------------------


def register_blueprints(app):
    """
    Iterating through all the blueprints defined in BLUEPRINTS_LOCATION module and subpackages.
    All registered modules have to expose a Blueprint instance named 'bp'.
    
    TODO:
     - find a way to specify a precedence of Blueprints.
    """
    for name in find_modules(app.config.get('BLUEPRINTS_LOCATION'), include_packages=True):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp)


# ----------------------------------------------------------------------------------------------------------------------

def register_cli(app):
    """
    Useful CLI command for dealing with a database.
    """
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


