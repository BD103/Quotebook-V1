from flask import Flask

from quotebook.__version__ import __version__
from quotebook.bridge import config, db, login_manager, csrf, compress
from quotebook.bp import bp


def create_app(name: str) -> Flask:
    app = Flask(name)

    config.init_app(app)

    db.init_app(app)
    # login_manager.init_app(app)
    csrf.init_app(app)
    compress.init_app(app)

    app.register_blueprint(bp)

    with app.app_context():
        db.create_all()

    @app.context_processor
    def inject_version():
        return dict(version=__version__)

    return app
