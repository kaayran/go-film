from flask import render_template
from flask_login import current_user


def get_index():
    return render_template('home/index.html', user=current_user)
