from flask import Blueprint
from flask_login import login_required

from .controllers import get_profile, get_films
from .controllers import get_create_films

account = Blueprint('account', __name__, template_folder='templates')


@account.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return get_profile()


@account.route('/films/create', methods=['GET', 'POST'])
@login_required
def create():
    return get_create_films()


@account.route('/films', methods=['GET', 'POST'])
@login_required
def films():
    return get_films()
