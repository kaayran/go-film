from flask import Blueprint
from flask_login import login_required

from .controllers import get_pools, add_pool

pools = Blueprint('pools', __name__, template_folder='templates')


@pools.route('/', methods=['GET'])
@login_required
def my_pools():
    return get_pools()


@pools.route('/create', methods=['GET', 'POST'])
@login_required
def create_pool():
    return add_pool()
