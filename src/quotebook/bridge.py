try:
    from flask_compress import Compress
except ImportError:

    class Compress(object):
        def __init__(self, app=None):
            pass

        def init_app(self, app):
            pass


from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
compress = Compress()
login_manager = LoginManager()
csrf = CSRFProtect()
