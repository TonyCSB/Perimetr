from flask import Blueprint, redirect, url_for, render_template, flash, request
from flask_login import current_user, login_required, login_user, logout_user

from .. import bcrypt
from ..models import User
from ..forms import RegistrationForm, LoginForm

import string

users = Blueprint("users", __name__)

# @user.route("/")
# def index():
#     raise NotImplementedError()


@users.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("gifts.index"))

    form = RegistrationForm()
    if form.validate_on_submit():
        p = form.password.data

        if (len(p) < 8 or len(list(filter(lambda x: x in string.ascii_uppercase, p))) == 0 or len(list(filter(lambda x: x in string.digits, p))) == 0 or len(list(filter(lambda x: x in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~", p))) == 0):
            flash("Password Requirement Not Met\nYou have been a naughty boy this year")
            return render_template("register.html", title="Account Registration", form=form)

        hashed = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hashed)
        user.save()

        return redirect(url_for("users.login"))

    return render_template("register.html", title="Account Registration", form=form)


@users.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("account"))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.objects(username=form.username.data).first()

        if user is None:
            print("here")
            flash("Username does not exist!")
        elif not bcrypt.check_password_hash(user.password, form.password.data):
            flash("Username/Password incorrect!")
        else:
            login_user(user)

            if request .args.get("next") is not None:
                return redirect(request.args.get("next"))
            else:
                return redirect(url_for("users.account"))

    return render_template("login.html", title="Account Login", form=form)


@users.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("gifts.index"))


@users.route("/account")
@login_required
def account():
    return "NotImplemented"
