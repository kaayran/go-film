from flask import Blueprint

from ..controllers import get_profile

account = Blueprint('account', __name__)


@account.route('/profile', methods=['GET', 'POST'])
def profile():
    return get_profile()
