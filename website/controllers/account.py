from flask import render_template, url_for, request, redirect
from flask_login import current_user

from ..models import Pool


def get_profile():
    if request.method == 'POST':
        name = request.form['name']
        number = request.form['number']
        amount = request.form['amount']
        count = request.form['count']

        new_pool = Pool(name=name, number=number, amount=amount, count=count)
        print(repr(new_pool))

        return redirect(url_for('home.index', user=current_user))

    return render_template('profile.html', user=current_user)
