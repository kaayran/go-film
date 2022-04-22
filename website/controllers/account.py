from flask import render_template, url_for, request, redirect
from flask_login import current_user


def get_profile():
    if request.method == 'POST':
        url = request.form['url']
        print(url)

        return redirect(url_for('home.index', user=current_user))

    return render_template('profile.html', user=current_user)
