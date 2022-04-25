from flask import Blueprint
from flask_login import login_required

from .controllers import get_index

home = Blueprint('home', __name__, template_folder='templates')


@home.route('/', methods=['GET'])
@login_required
def index():
    return get_index()
