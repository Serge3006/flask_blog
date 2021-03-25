from flask import render_template, session, redirect, url_for, flash
from datetime import datetime
from . import main
from .forms import EditUserForm
from .. import db
from ..models import User
from flask_login import current_user

@main.route("/user/<username>", methods=["GET"])
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template("user.html", user=user)

@main.route("/edit-profile", methods=["GET", "POST"])
def user(username):
    form = EditUserForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        db.session.commit()
        flash("Your profile has been updated.")
        return redirect(url_for("main.user", username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template("edit-profile.html", form=form)


    return render_template("user_profile.html", form=form, user=current_user)