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
from app.helper_objects import boolean_to_binary, binary_to_boolean, rl_vehicle_list

db_path = 'rl_stats.db'

@app.route('/')
@app.route('/index/', methods=["GET", "POST"])
@login_required
def index():
    # obtain the most recent data for user (if available) to try and \
    # autopopulate some of the fields.
    try:
        # attempt to get information from the database from the current_user
        conn = sqlite3.connect(db_path)
        cur = conn.execute("SELECT * \
                            FROM game_data \
                            WHERE username = ? \
                            ORDER BY id DESC \
                            LIMIT 1", 
                            (current_user.username,))
        cur = cur.fetchone()
        conn.close()
        # Convert the tuple from the db to a list
        cur = list(cur)

        # Convert the binary (db) into boolean (webpage)
        cur[4] = binary_to_boolean(cur[4])
        cur[6] = binary_to_boolean(cur[6])
        cur[9] = binary_to_boolean(cur[9])

        form = GameDataForm(vehicle=cur[8], team=cur[7], partied=cur[6], 
                            topper=cur[4], antenna=cur[9], fov=cur[10],
                            distance=str(cur[11]), height=cur[12], angle=cur[13])
    except:
        # if there is no data in the database from the current_user \
        # then just go with some defaults.
        cur = ["0", "1970-01-01 00:00:00", current_user.username, "win", 
                False, "three_v_three", False, "blue", "batmobile16",
                False, 110, 220, 110, -4]
        form = GameDataForm(vehicle=cur[8], team=cur[7], partied=cur[6], 
                            topper=cur[4], antenna=cur[9], fov=cur[10],
                            distance=str(cur[11]), height=cur[12], angle=cur[13])

    return render_template('index.html', form=form, cur=cur)

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
    current_time = str(datetime.utcnow())[:19]
    # Collect all of the form variables
    # Convert the boolean fields to binary w/ helper function
    current_result = form.result.data
    current_topper = boolean_to_binary(form.topper.data)
    current_gamemode = form.gamemode.data
    current_partied = boolean_to_binary(form.partied.data)
    current_team = form.team.data
    current_vehicle = form.vehicle.data
    current_antenna = boolean_to_binary(form.antenna.data)
    current_fov = form.fov.data
    current_distance = form.distance.data
    current_height = form.height.data
    current_angle = form.angle.data
    current_notes = form.notes.data

    # You don't have any data validation here... was it taken care of somewhere
    # else???

    conn = sqlite3.connect(db_path)
    conn.execute("INSERT INTO game_data (date_time, username, \
                        game_result, topper, game_mode, partied, team, \
                        vehicle, antenna, fov, distance, height, angle, \
                        notes) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (
                        current_time, current_user.username, 
                        current_result, current_topper, current_gamemode, 
                        current_partied, current_team, current_vehicle, 
                        current_antenna, current_fov, current_distance, 
                        current_height, current_angle, current_notes))
    conn.commit()
    conn.close()
    
    # current_user.username
    return redirect(url_for('index'))

@app.route('/analyze/', methods=['GET', 'POST'])
@login_required
def analyze():
    form = AnalyzeForm()
    
    # By default The result_dict contains info about the most recent 20 games
    # for the user currently logged in.
    # If there aren't 20 games worth of data, it'll show as many games
    # as are available.
    result_dict = {}
    conn = sqlite3.connect(db_path)
    cur = conn.execute("SELECT * \
                        FROM game_data \
                        WHERE username=? \
                        ORDER BY id DESC \
                        LIMIT 20", 
                        (current_user.username,))

    cur = cur.fetchall()


    # Put the results of the fetchall into 20 rows of the result_dict.
    # keys are numbers 0 - 19 (inclusive)
    # values are the rows of data from cur.fetchall()
    for j in range(20):
        try:
            result_dict[j] = cur[j]
        except:
            # If there aren't twenty rows of data, just put the loop 
            # counter as the value.
            result_dict[j] = j

    # Calculate the win-loss record and store it in the result_dict
    # under the key 'record'
    win_counter = 0
    loss_counter = 0

    for j in range(20):
        # the try-except below is for making the win-loss record display
        try:
            if result_dict[j][3] == "Win" or \
                result_dict[j][3] == "Forfeit Win":
                    win_counter = win_counter + 1
            elif result_dict[j][3] == "Loss" or \
                result_dict[j][3] == "Forfeit Loss":
                    loss_counter = loss_counter + 1
        except:
            # An empty except clause is poor practice, but I really 
            # can't think of what should go here.
            pass

    record = str(win_counter) + 'W - ' + str(loss_counter) + 'L'

    result_dict['record'] = record

    return render_template('analyze.html', form=form, result_dict=result_dict)

@app.route('/filter_table/', methods=['GET', 'POST'])
@login_required
def filter_table():
    form = AnalyzeForm()

    result_dict = {}
    conn = sqlite3.connect(db_path)
    cur = conn.execute("SELECT * FROM game_data \
                        WHERE username=? \
                        AND team IN (?,?) \
                        ORDER BY id DESC \
                        LIMIT 20",
                        (current_user.username, 'blue', 'club_colors'))
    cur = cur.fetchall()

    for j in range(20):
        try:
            result_dict[j] = cur[j]
        except:
            # If there aren't twenty rows of data, just put the loop 
            # counter as the value.
            result_dict[j] = j

    # Calculate the win-loss record and store it in the result_dict
    # under the key 'record'
    win_counter = 0
    loss_counter = 0

    for j in range(20):
        try:
            if result_dict[j][3] == "win" or \
                result_dict[j][3] == "forfeit_win":
                    win_counter = win_counter + 1
            elif result_dict[j][3] == "loss" or \
                result_dict[j][3] == "forfeit_loss":
                    loss_counter = loss_counter + 1
        except:
            # An empty except clause is poor practice, but I really 
            # can't think of what should go here.
            pass

    record = str(win_counter) + 'W - ' + str(loss_counter) + 'L'

    result_dict['record'] = record

    return render_template('analyze.html', form=form, result_dict=result_dict)



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
