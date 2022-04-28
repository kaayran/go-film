from flask import render_template, url_for, request, redirect, flash
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

    return render_template('pools/index.html', pools=pools)


def add_pool():
    if request.method == 'POST':
        name = request.form['name']
        number = request.form['number']
        amount = request.form['amount']
        count = request.form['count']
        user = current_user
        user_id = user.id

        new_pool = Pool(name=name, number=number, amount=amount, count=count, user_id=user_id)
        new_pool.hash_link = hash(new_pool)
        print(repr(new_pool))

        session = Session()
        session.add(new_pool)
        session.commit()

        return redirect(url_for('home.index'))

    return render_template('pools/create.html')


def get_pool(hash_link):
    session = Session()
    pool = session.query(Pool).filter_by(hash_link=hash_link).first()
    print(repr(pool))
    if pool:
        if hash_link:
            return render_template('pools/link.html', hash_link=hash_link, pool=pool)
    flash(f'Pool with hash: ({hash_link}) could not be found.', category='error')
    return redirect(url_for('home.index'))
