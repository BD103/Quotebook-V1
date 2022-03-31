from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from quotebook.bridge import db


class Quote(db.Model):
    # __tablename__ = "quotebook-quotes"

    id = db.Column(db.Integer, primary_key=True)
    quote = db.Column(db.String(200), index=False, unique=True, nullable=False)
    quotee = db.Column(db.String(40), index=False, unique=False, nullable=True)
    created = db.Column(db.DateTime, index=False, unique=False, nullable=False)

    def __repr__(self):
        return f"<Quote '{self.quote}>"


class User(UserMixin, db.Model):
    __tablename__ = "quotebook-users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20, collation="NOCASE"), unique=True, nullable=False)
    password = db.Column(
        db.String(200), primary_key=False, unique=False, nullable=False
    )
    created_on = db.Column(db.DateTime, unique=False, nullable=True)
    last_login = db.Column(db.DateTime, unique=False, nullable=True)

    def set_password(self, password: str) -> None:
        self.password = generate_password_hash(password, method="sha256")

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"<User '{self.username}'>"
