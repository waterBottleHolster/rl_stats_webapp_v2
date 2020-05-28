from flask import Flask, render_template, redirect, request
import sqlite3
from sqlite3 import Error
from flask import g

DATABASE = 'rl_stats.db'


app=Flask(__name__)

#flash.palletsprojects.com has a good tutorial on using sqlite3 with Flask
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    return render_template("index.html")
    cur = get_db().cursor()

@app.route("/home")
def home():
    return redirect("/")

@app.route("/pre-game")
def pregame_settings():
    return render_template("pre_game_settings.html")

@app.route("/camera-settings")
def camera_settings():
    return render_template("camera_settings.html")

@app.route("/controller-settings")
def controller_settings():
    return render_template("controller_settings.html")

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")