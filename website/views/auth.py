from flask import Blueprint
from flask_login import login_required

from ..controllers import auth

auth_views = Blueprint('auth_views', __name__)


@auth_views.route('/login', methods=['GET', 'POST'])
def login():
    return auth.login()


@auth_views.route('/logout', methods=['GET'])
@login_required
def logout():
    return auth.logout()


@auth_views.route('/signup', methods=['GET', 'POST'])
def signup():
    return auth.signup()
