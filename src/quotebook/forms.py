from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class QuoteForm(FlaskForm):
    quote = StringField("Quote", [DataRequired()])
    quotee = StringField("Quotee", render_kw={"placeholder": "Anonymous"})
    submit = SubmitField("Submit")
