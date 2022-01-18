try:
    from flask_compress import Compress
except ImportError:
    # For when brotli not correctly installed
    class Compress(object):
        def __init__(self, app=None):
            self.init_app(app)

        def init_app(self, app):
            pass


from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from quotebook.config import Configuration

configuration = Configuration()
db = SQLAlchemy()
compress = Compress()
login_manager = LoginManager()
csrf = CSRFProtect()
