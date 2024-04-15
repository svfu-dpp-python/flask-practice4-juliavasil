from flask import Flask

from .models import db, migrate
from . import views


def create_app():
    app = Flask(__name__)

    # Конфигурация
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

    app.config["SECRET_KEY"] = "secret"

    # База данных
    db.init_app(app)
    migrate.init_app(app, db)

    # Функции представления
    app.add_url_rule("/", view_func=views.index_page)
    app.add_url_rule("/login/", view_func=views.login_page, methods=["GET", "POST"])
    app.add_url_rule("/logout/", view_func=views.logout)


    return app
