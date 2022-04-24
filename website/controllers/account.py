from flask import render_template, url_for
from flask_login import current_user


def get_profile():
    return render_template('profile.html', user=current_user)
