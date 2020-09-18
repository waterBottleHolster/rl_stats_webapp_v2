#!/home/dh_4gxtme/rl-experiment-tracker.com/public/rl_stats_webapp_v2/.flask_venv/bin/python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config

db = SQLAlchemy()

login_manager=LoginManager()
# the login_view attribute below points to the 
# endpoint (aka 'view') for the login page.
login_manager.login_view = 'login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    login_manager.init_app(app)

    # This is where you can register blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='auth')

    return app
