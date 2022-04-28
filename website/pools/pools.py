from flask import Blueprint, redirect, url_for
from flask_login import login_required

from .controllers import get_pools, add_pool, get_pool

pools = Blueprint('pools', __name__, template_folder='templates')


@pools.route('/', methods=['GET'])
@login_required
def index():
    return get_pools()


@pools.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    return add_pool()


@pools.route('/<hash_link>', methods=['GET'])
@login_required
def link(hash_link=None):
    if hash_link:
        return get_pool(hash_link)

    return redirect(url_for('home.index'))
