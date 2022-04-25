from flask import render_template
from flask_login import current_user


def get_profile():
    return render_template('account/index.html', user=current_user)
