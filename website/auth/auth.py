from flask import Blueprint
from flask_login import login_required

from .controllers import get_login, get_logout, get_signup

auth = Blueprint('auth', __name__, template_folder='templates')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return get_login()


@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    return get_logout()


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    return get_signup()
