from flask import render_template


def get_profile():
    return render_template('account/index.html')
