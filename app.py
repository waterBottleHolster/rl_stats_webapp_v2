from flask import Flask, render_template, redirect, request, flash
import sqlite3
from sqlite3 import Error
from flask import g
import json


# There is a strong debate in my head about whether to use JSON or sqlite3 for 
# storing this website's info.  I'm going to go with sqlite3 for now because
# it's much easier to "run experiments" on data stored in a sqlite3 db than
# with filtering through json.

# Conversely, the elements like title bar and dropdowns are fine to be populated
# with data stored in the json.

#flash.palletsprojects.com has a good tutorial on using sqlite3 with Flask
active_db = 'rl_stats.db'
conn = sqlite3.connect(active_db)
cur = conn.cursor()
cur.execute("SELECT * FROM nav_bar_titles")
nav_bar_titles = cur.fetchall()

app=Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html", nav_bar_titles=nav_bar_titles)

@app.route("/home/")
def home():
    flash("flash test!!")
    return redirect("/")

@app.route("/pre-game/")
def pregame_settings():
    return render_template("pre_game_settings.html")

@app.route("/camera-settings/")
def camera_settings():
    return render_template("camera_settings.html")

@app.route("/controller-settings/")
def controller_settings():
    return render_template("controller_settings.html")

@app.errorhandler(404)
def page_not_found(e):
    return("return four oh four")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")