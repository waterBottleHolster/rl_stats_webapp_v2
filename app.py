from flask import Flask, render_template, redirect, request
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return redirect("/")

@app.route("/pre-game")
def pregame_settings():
    return render_template("pre_game_settings.html")

@app.route("/camera-settings")
def camera_settings():
    return render_template("camera_settings_v2.html")

@app.route("/controller-settings")
def controller_settings():
    return render_template("controller_settings_v2.html")