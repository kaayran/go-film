from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from website import Session
from website.models import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        session = Session()
        user = session.query(User).filter_by(email=email).first()
        session.close()
        if user:
            if check_password_hash(user.password, password):
                flash('User logged successfully.', category='success')
                return redirect(url_for('views.home'))

        flash('Incorrect email or/and password.', category='error')

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
            session = Session()
            user = session.query(User).filter_by(email=email).first()
            if not user:
                hashed_password = generate_password_hash(password, method='sha256')
                new_user = User(email=email, name=name, password=hashed_password)
                session = Session()
                session.add(new_user)
                session.commit()
                flash('User created successfully.', category='success')
                return redirect(url_for('views.home'))

            flash('User already exists.', category='error')

    return render_template('sign_up.html')
