from flask import Blueprint, render_template
from flask_login import login_required, current_user

home_views = Blueprint('home_views', __name__)


@home_views.route('/', methods=['GET'])
@login_required
def home():
    return render_template('home.html', user=current_user)
