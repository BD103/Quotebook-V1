from datetime import datetime

from flask import Blueprint, redirect, render_template, url_for

from quotebook.bridge import db
from quotebook.forms import QuoteForm
from quotebook.models import Quote

bp = Blueprint(
    "core",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static/qb",
)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/quote/")
@bp.route("/quote/<int:id>")
def view_quote(id: int = None):
    if id is None:
        return redirect(url_for("core.all_quotes"))

    existing_quote = Quote.query.filter_by(id=id).first()

    if existing_quote is None:
        return redirect(url_for("core.all_quotes"))

    return render_template("view.html", quote=existing_quote)


@bp.route("/all")
def all_quotes():
    return render_template("all.html", quotes=Quote.query.order_by(Quote.id.desc()).all())


@bp.route("/new", methods=["GET", "POST"])
def new_quote():
    form = QuoteForm()

    if form.validate_on_submit():
        existing_quote = Quote.query.filter_by(quote=form.quote.data).first()

        if existing_quote is None:
            new_quote = Quote(
                quote=form.quote.data, quotee=form.quotee.data, created=datetime.now()
            )

            db.session.add(new_quote)
            db.session.commit()
            return redirect(url_for("core.view_quote", id=new_quote.id))

        return redirect(url_for("core.view_quote", id=existing_quote.id, exists=True))

    return render_template("new.html", form=form)
