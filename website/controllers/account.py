from flask import render_template, url_for, request, redirect
from flask_login import current_user

from ..parser import get_film_id, get_film_data


def get_profile():
    if request.method == 'POST':
        url = request.form['url']
        film_id = get_film_id(url)
        print(url)
        print(film_id)
        film_name, film_poster = get_film_data(film_id)


        print(film_name, film_poster)

        return redirect(url_for('home.index', user=current_user))

    return render_template('profile.html', user=current_user)
