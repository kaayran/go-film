from flask import render_template, url_for, request, redirect
from flask_login import current_user

from website.db import Session
from website.models import Pool


def get_pools():
    user = current_user
    user_id = user.id

    session = Session()
    pools = session.query(Pool).filter_by(user_id=user_id)

    for pool in pools:
        print(repr(pool))

    return render_template('pools/index.html', user=current_user, pools=pools)


def add_pool():
    if request.method == 'POST':
        name = request.form['name']
        number = request.form['number']
        amount = request.form['amount']
        count = request.form['count']
        user = current_user
        user_id = user.id

        new_pool = Pool(name=name, number=number, amount=amount, count=count, user_id=user_id)
        print(repr(new_pool))

        session = Session()
        session.add(new_pool)
        session.commit()

        return redirect(url_for('home.index'))

    return render_template('pools/create.html', user=current_user)
