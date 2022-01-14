from flask import Flask

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

    return app
