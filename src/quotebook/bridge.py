
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from quotebook.config import Configuration

try:
    from flask_compres import Compress
except ImportError:
    # Some computers do not support C modules
    class Compress(object):
        def __init__(self, app=None):
            if app is not None:
                self.init_app(app)

        def init_app(self, app):
            app.logger.info(
                "Compression is not enabled. Your computer may not support C modules."
            )

config = Configuration()
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
compress = Compress()
