from flask import Blueprint, render_template, flash, redirect, url_for, request
from app.forms import LoginForm, SignupForm
from flask_login import current_user, login_user, logout_user
from app.models import User
from werkzeug.urls import url_parse
from app import db

user = Blueprint("user", __name__)


@user.route('/signup', methods=['POST', 'GET'])
def signup():
    # User logged In -> go home
    if current_user.is_authenticated:
        return redirect(url_for('note.home'))
    # User logging in -> check in DB
    form = SignupForm()
    if form.validate_on_submit      ():
        new_user = User(form.username.data, form.email.data)
        new_user.hash_pw(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Congratulations, you are now a New user!', category='success')
        return redirect(url_for('user.login'))
    return render_template('signup.html', form=form)


@user.route('/', methods=['GET', 'POST'])
@user.route('/login', methods=['GET', 'POST'])
def login():
    # User logged In -> go home
    if current_user.is_authenticated:
        return redirect(url_for('note.home'))
    # User logging in -> check in DB
    form = LoginForm()
    if form.validate_on_submit():  # POST = TRUE, GET + FALSE
        logging_user = User.query.filter_by(username=form.username.data).first()
        # check user in db and check password
        if logging_user is None or logging_user.check_pw(form.password.data) == False:
            flash('Invalid Name or Password Incorrect', category='error')
        # Correct
        else:
            login_user(logging_user, remember=form.remember_me.data)
            # Nextpage
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('note.home')
                return redirect(next_page)

            return redirect(url_for('note.home'))

    return render_template('login.html', form=form)


@user.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('user.login'))
