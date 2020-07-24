#!/home/dh_4gxtme/rl-experiment-tracker.com/public/rl_stats_webapp_v2/venv_rl_webapp/bin/python3
from flask import render_template, flash, redirect, g, url_for, request
from app import app
from app.forms import LoginForm, RegistrationForm, GameDataForm, AnalyzeForm
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash
from werkzeug.urls import url_parse
from app.models import User
import sqlite3
from datetime import datetime

db_path = 'rl_stats.db'

@app.route('/')
@app.route('/index/', methods=["GET", "POST"])
@login_required
def index():
    form = GameDataForm()
    return render_template('index.html', form=form, current_time=datetime.utcnow())

@app.route('/register/', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        conn = sqlite3.connect(db_path)
        password_hash = generate_password_hash(form.password.data)
        conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (form.username.data, password_hash))
        conn.commit()
        conn.close()

        user = User(username=form.username.data,
                    password_hash=password_hash)
        
        return redirect(url_for('index'))

    return render_template('register.html', form=form)


@app.route('/data_submit/', methods=['GET', 'POST'])
def data_submit():
    form = GameDataForm()

    return redirect(url_for('index'))

@app.route('/analyze/', methods=['GET', 'POST'])
@login_required
def analyze():
    form = AnalyzeForm()
    print(form.validate_on_submit())
    return render_template('analyze.html', form=form)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        conn = sqlite3.connect(db_path)
        cur = conn.execute('SELECT * FROM users WHERE username = ?', (form.username.data,))
        cur = cur.fetchone()
        user = User(cur[1], cur[2])
        # at this point cur contains either [] or the row of data for the user
        # which includes userid (int), username(string), and password(string)
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=True)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            flash('Hello \"' + user.username + '\"')
            next_page = url_for('index')
        return redirect(next_page)

    return render_template('login_v2.html', form=form)

@app.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('You\'ve Been Successfully Logged Out')
    return redirect(url_for('login'))
