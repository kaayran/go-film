from flask import Blueprint, render_template, url_for, request
from flask_login import login_user, login_required, current_user

views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
@login_required
def home():
    return render_template('home.html', user=current_user)
