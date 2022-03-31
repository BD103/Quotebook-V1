from flask import Flask

from quotebook.__version__ import __version__
from quotebook.auth import auth_bp
from quotebook.bp import bp
from quotebook.bridge import compress, config, csrf, db, login_manager


def create_app(name: str) -> Flask:
    app = Flask(name)

    config.init_app(app)

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    compress.init_app(app)

    app.register_blueprint(bp)
    app.register_blueprint(auth_bp)

    with app.app_context():
        db.create_all()

    @app.context_processor
    def inject_version():
        return dict(version=__version__)

    return app
