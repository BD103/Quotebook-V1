from flask import Flask

from quotebook.__version__ import __version__
from quotebook.bridge import compress, configuration, csrf, db, login_manager
from quotebook.core.bp import bp as core_bp


def create_app(name: str) -> Flask:
    app = Flask(name)
    # Config first, everything else later
    configuration.init_app(app)

    app.register_blueprint(core_bp)

    db.init_app(app)
    compress.init_app(app)
    csrf.init_app(app)

    with app.app_context():
        db.create_all()

    @app.context_processor
    def inject_version():
        return dict(version=__version__)

    return app
