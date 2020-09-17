#!/home/dh_4gxtme/rl-experiment-tracker.com/public/rl_stats_webapp_v2/.flask_venv/bin/python3
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()

login_manager=LoginManager()
# the login_view attribute below points to the 
# endpoint (aka 'view') for the login page.
login_manager.login_view = 'login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    login_manager.init_app(app)
    db.init_app(app)

    # This is where you can register blueprints

    return app
