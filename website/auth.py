from flask import Blueprint, render_template, request, flash

from website import Session
from website.models import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return render_template('logout.html')


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        repeat_password = request.form.get('repeat-password')

        print(request.form)

        if password != repeat_password:
            flash('Passwords not the same.', category='error')
            pass
        else:
            flash('Successful registration of a new user.', category='success')
            new_user = User(email=email, name=name, password=password)
            session = Session()
            session.add(new_user)
            session.commit()

    return render_template('sign_up.html')
