


from dotenv import load_dotenv
import os
load_dotenv()

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
import openai



import config

db=SQLAlchemy()
migrate= Migrate()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    #ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    #CSRF 보호 적용
    csrf.init_app(app)

    #블루프린트
    from .views import diary,main,account,weekly
    app.register_blueprint(diary.bp)
    app.register_blueprint(main.bp)
    app.register_blueprint(account.bp)
    app.register_blueprint(weekly.bp)

    #필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    return app
