import os

from flask import Flask
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

    from .home import home
    from .auth import auth
    from .account import account
    from .pools import pools

    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(account, url_prefix='/account')
    app.register_blueprint(pools, url_prefix='/pools')

    # Import all Database classes here
    from .models import User, Pool, Film

    from .db import Base, engine, Session

    # Create or re-create tables and relationships to database server
    Base.metadata.create_all(engine)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        session = Session()
        return session.query(User).get(int(user_id))

    return app
