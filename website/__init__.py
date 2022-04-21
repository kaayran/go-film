import os
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy_utils import database_exists, create_database

Base = declarative_base()
engine = create_engine(os.environ['PS_URL'])
Session = sessionmaker(bind=engine)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    Base.metadata.create_all(engine)

    return app
