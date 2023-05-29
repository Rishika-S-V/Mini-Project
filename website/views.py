from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
import json
from .models import Disaster
from . import db


views = Blueprint("views", __name__)


@views.route("/")
@login_required
def home():
    disaster_query = Disaster.query.all()
    disasters = [
        {
            "id": disaster.id,
            "title": disaster.title,
            "description": disaster.desc,
            "location": disaster.location,
            "is_resolved": disaster.is_resolved,
            "user_id": disaster.user_id,
        }
        for disaster in disaster_query
    ]
    print(disasters)
    return render_template("home.html", user=current_user, disasters=disasters)


@views.route("/add", methods=["GET", "POST"])
@login_required
def add_disaster():
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        location = request.form.get("location")

        disaster = Disaster(
            title=title,
            desc=description,
            location=location,
            user_id=current_user.id,
        )
        db.session.add(disaster)
        db.session.commit()

        flash(f"Successfully Added Entry", "success")
        return render_template("add_disaster.html", user=current_user)

    return render_template("add_disaster.html", user=current_user)
