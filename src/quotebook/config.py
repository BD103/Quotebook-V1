import os


class Default(object):
    # Flask
    SECRET_KEY = os.getenv("SECRET_KEY")

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = "sqlite:///qb.db"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
