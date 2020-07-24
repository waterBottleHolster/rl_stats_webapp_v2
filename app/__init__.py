#!/home/dh_4gxtme/rl-experiment-tracker.com/public/rl_stats_webapp_v2/venv_rl_webapp/bin/python3
from flask import Flask
from config import Config
from flask_login import LoginManager
from flask_moment import Moment

app = Flask(__name__)
moment = Moment(app)
login = LoginManager(app)
login.login_view = 'login'
app.config.from_object(Config)

from app import routes
