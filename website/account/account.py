from flask import Blueprint
from flask_login import login_required

from .controllers import get_profile

account = Blueprint('account', __name__, template_folder='templates')


@account.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return get_profile()
