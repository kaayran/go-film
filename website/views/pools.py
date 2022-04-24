from flask import Blueprint
from flask_login import login_required

from ..controllers import get_pools
from ..controllers import add_pool

pools = Blueprint('pools', __name__)


@pools.route('/pools', methods=['GET'])
@login_required
def my_pools():
    return get_pools()


@pools.route('/pools/create', methods=['GET', 'POST'])
@login_required
def create_pool():
    return add_pool()
