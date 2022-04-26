from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user

from ...db import Session
from ...models import Film
from ...parser import get_film_id, get_film_data


def get_create_films():
    if request.method == 'POST':
        url = request.form['url']
        user = current_user
        user_id = user.id
        film_id = get_film_id(url)
        new_film = get_film_data(film_id)
        new_film.user_id = user_id
        print(repr(new_film))

        flash('Film successfully added to your list.', category='success')

        session = Session()
        session.add(new_film)
        session.commit()

        return redirect(url_for('account.create'))

    return render_template('account/create.html')


def get_films():
    user = current_user
    user_id = user.id

    session = Session()
    films = session.query(Film).filter_by(user_id=user_id)
    session.close()

    return render_template('account/films.html', films=films)
