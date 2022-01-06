from flask import Flask, redirect, request, url_for
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = MongoEngine()
bcrypt = Bcrypt()
login_manager = LoginManager()


from .users.routes import users


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile("config.py", silent=False)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(users, url_prefix="/user")

    login_manager.login_view = "users.login"

    return app


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for("users.login") + "?next=" + request.path)
