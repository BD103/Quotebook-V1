import os


class Default(object):
    # Flask
    SECRET_KEY = os.getenv("SECRET_KEY")

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = "sqlite:///qb.db"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Configuration(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        defaults = [
            # Allow creating new users
            ("QB_ENABLE_SIGNUPS", True),
            # Allow creating new quotees
            ("QB_QUOTEE_CREATION", True),
            # Require authentication to view quotes
            ("QB_AUTH_VIEW", False),
            # Requires authentication to create quotes
            ("QB_AUTH_CREATE", True)
            # Pre-created quotees to be supplied
            ("QB_QUOTEES", [])
            # List of usernames with admin powers
            ("QB_ADMINS", []),
        ]

        for k, v in defaults:
            app.config.setdefault(k, v)

        app.config.from_object(Default)
