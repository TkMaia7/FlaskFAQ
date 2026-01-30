from flask import Blueprint, render_template, session, redirect, url_for
from flask_faq.models import Faq

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    faqs = Faq.query.all()
    return render_template("index.html", faqs=faqs)

@bp.route("/relogin")
def relogin():
    session.clear() 
    return redirect(url_for('simplelogin.login', next='/admin'))