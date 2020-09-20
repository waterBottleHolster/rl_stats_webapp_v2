#!/home/dh_4gxtme/rl-experiment-tracker.com/public/rl_stats_webapp_v2/.flask_venv/bin/python3
from flask import render_template, flash, redirect, url_for, request, current_app
from .forms import LoginForm, RegistrationForm, GameDataForm, AnalyzeForm
from flask_login import current_user, login_user, logout_user, login_required
from . import main
from .. import db
from ..models import User, GameEvent

from werkzeug.security import generate_password_hash
from werkzeug.urls import url_parse

from datetime import datetime
from app.helper_objects import boolean_to_binary, binary_to_boolean, \
                                rl_vehicle_list


@main.route('/')
@main.route('/index/', methods=["GET", "POST"])
def index():
    # obtain the most recent data for user (if available) to try and \
    # autopopulate some of the fields.
    form = GameDataForm()

    return render_template('index.html', form=form)


@main.route('/data_submit/', methods=['GET', 'POST'])
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

    
    # current_user.username
    return redirect(url_for('index'))

@main.route('/analyze/', methods=['GET', 'POST'])
def analyze():
    form = AnalyzeForm()
    
    # By default The result_dict contains info about the most
    # recent 20 games for the user currently logged in.
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
        # the try-except below makes the win-loss record display
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

@main.route('/filter_table/', methods=['GET', 'POST'])
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