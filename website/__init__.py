import os

from flask import Flask
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

    from .views import home_views
    from .views import auth_views

    app.register_blueprint(home_views, url_prefix='/')
    app.register_blueprint(auth_views, url_prefix='/')

    # Import all Database classes here
    from .models import User

    from .db import Base, engine, Session

    # Create or re-create tables and relationships to database server
    Base.metadata.create_all(engine)

    login_manager = LoginManager()
    login_manager.login_view = 'auth_views.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        session = Session()
        return session.query(User).get(int(user_id))

    return app
