#!/home/dh_4gxtme/rl-experiment-tracker.com/public/rl_stats_webapp_v2/venv_rl_webapp/bin/python3
from flask import render_template, flash, redirect, g, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User
import sqlite3

db_path = 'rl_stats.db'

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        conn = sqlite3.connect(db_path)
        cur = conn.execute('SELECT * FROM users WHERE username = ?', (form.username.data,))
        cur = cur.fetchone()
        user = User(cur[0], cur[1], cur[2])
        # at this point cur contains either [] or the row of data for the user
        # which includes userid (int), username(string), and password(string)
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=True)
        return redirect(url_for('index'))

    return render_template('login.html', form=form)

    
