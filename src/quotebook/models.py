from quotebook.bridge import db


class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quote = db.Column(db.String(200), index=False, unique=True, nullable=False)
    quotee = db.Column(db.String(40), index=False, unique=False, nullable=True)
    created = db.Column(db.DateTime, index=False, unique=False, nullable=False)

    def __repr__(self):
        return f"<Quote '{self.quote}>"
