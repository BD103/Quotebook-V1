import datetime


class Default(object):
    # Flask
    PREFERRED_URL_SCHEME = "https"

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = "sqlite:///qb.db"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Caching
    CACHE_TYPE = "redislite_cache.RedisliteCache"
    CACHE_DEFAULT_TIMEOUT = 300


class Config(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        defaults = [
            ("QB_TIMEZONE", datetime.timezone(datetime.timedelta(hours=-5), "EST"))
        ]

        for k, v in defaults:
            app.config.setdefault(k, v)

        app.config.from_object(Default)
