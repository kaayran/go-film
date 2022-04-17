from flask import Blueprint, render_template, url_for, request

views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
def home():
    return render_template('home.html')
