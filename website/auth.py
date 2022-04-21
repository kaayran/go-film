from flask import Blueprint, render_template, request, flash

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
        repeat_password = request.form.get('repeatPassword')

        if password != repeat_password:
            flash('Passwords not the same.', category='error')
            pass
        else:
            flash('Successful registration of a new user.', category='success')

    return render_template('sign_up.html')
