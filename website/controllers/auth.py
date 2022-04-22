from flask import render_template, flash, url_for, request, redirect
from flask_login import login_user, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from ..db import Session
from ..models import User


def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        session = Session()
        user = session.query(User).filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('User logged successfully.', category='success')
                login_user(user, remember=True)
                return redirect(url_for('home_views.home', user=current_user))

        session.close()
        flash('Incorrect email or/and password.', category='error')

    return render_template('login.html', user=current_user)


def logout():
    logout_user()
    return redirect(url_for('auth_views.login', user=current_user))


def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        repeat_password = request.form.get('repeat-password')

        if password != repeat_password:
            flash('Passwords not the same.', category='error')
            pass
        else:
            session = Session()
            user = session.query(User).filter_by(email=email).first()
            if not user:
                hashed_password = generate_password_hash(password, method='sha256')
                new_user = User(email=email, name=name, password=hashed_password)
                session.add(new_user)
                session.commit()
                flash('User created successfully.', category='success')
                login_user(new_user, remember=True)
                return redirect(url_for('home_views.home', user=current_user))

            session.close()
            flash('User already exists.', category='error')

    return render_template('sign_up.html', user=current_user)
