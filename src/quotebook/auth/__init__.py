import datetime
import click
from flask import Blueprint, current_app, flash, redirect, render_template, url_for
from flask_login import current_user, login_required, login_user, logout_user

from quotebook.bridge import db, login_manager
from quotebook.forms import LoginForm
from quotebook.models import User


auth_bp = Blueprint(
    "auth",
    __name__,
    template_folder = "templates"
)


# Routing

@auth_bp.route("/login", methods = ["GET", "POST"])
def login():
    if current_user.is_authenticated:
        flash("Already logged in")
        return redirect(url_for("core.all_quotes"))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user and user.check_password(password=form.password.data):
            login_user(user)
            return redirect(url_for("core.all_quotes"))

        flash("Invalid username or password")
        return redirect(url_for("auth.login"))

    return render_template("auth/login.jinja2", form=form)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Successfully logged out")
    return redirect(url_for("auth.login"))


# Flask-Login

@login_manager.user_loader
def load_user(id_):
    if id_ is not None:
        return User.query.get(id_)

    return None


@login_manager.unauthorized_handler
def unauthorized():
    flash("You must be logged in to view this page")
    return redirect(url_for("auth.login"))


# CLI

auth_bp.cli.short_help = auth_bp.cli.help = "Manage registered accounts."

def _abort_if_false(ctx, param, value):
    if not value:
        ctx.abort()


@auth_bp.cli.command("create")
@click.argument("username")
@click.password_option()
def cli_create(username: str, password: str):
    existing_user = User.query.filter_by(username=username).first()

    if existing_user is None:
        user = User(
            username=username,
            created_on=datetime.datetime.now(tz=current_app.config["QB_TIMEZONE"]),
        )
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        print(f"New user '{user}' created")
    else:
        print(f"User '{existing_user}' already exists")


@auth_bp.cli.command("get")
@click.option("-u", "--user", "usernames", multiple=True)
@click.option("-a", "--all", "all_", is_flag=True, default=False)
def cli_get(usernames: tuple[str], all_: bool):
    # No username specified
    if all_:
        for user in User.query.all():
            print(repr(user))
    elif usernames == ():
        print("No users specified, please use the --user option")
    else:
        for username in usernames:
            user = User.query.filter_by(username=username).first()

            if user is not None:
                print(
                    {
                        "username": user.username,
                        "created_on": user.created_on,
                        "last_login": user.last_login,
                    }
                )
            else:
                print(f"User '{username}' does not exist")


@auth_bp.cli.command("delete")
@click.argument("username")
@click.option(
    "-y",
    "--yes",
    is_flag=True,
    callback=_abort_if_false,
    expose_value=False,
    prompt="Are you sure you want to delete this user?",
)
def cli_delete(username: str):
    User.query.filter_by(username=username).delete()
    db.session.commit()
