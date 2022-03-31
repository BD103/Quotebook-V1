from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class QuoteForm(FlaskForm):
    quote = StringField("Quote", [DataRequired()])
    quotee = StringField("Quotee", render_kw={"placeholder": "Anonymous"})
    submit = SubmitField("Submit")


class LoginForm(FlaskForm):
    username = StringField("Username", [DataRequired()])
    password = PasswordField("Password", [DataRequired()])
    submit = SubmitField("Log in")
