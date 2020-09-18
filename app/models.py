#!/home/dh_4gxtme/rl-experiment-tracker.com/public/rl_stats_webapp_v2/.flask_venv/bin/python3
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app, request, url_for
from flask_login import UserMixin
import sqlite3

from . import db, login_manager


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash
        conn = sqlite3.connect(db_path)
        cur = conn.execute("SELECT id FROM users WHERE username = ?", 
                            (username,))
        cur = cur.fetchone()
        conn.close()
        if cur == None:
            self.id = None
        else:
            self.id = cur[0]

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class GameEvent(db.Model):
    __tablename__ = 'game_events'
    id = db.Column(db.Integer, primary_key=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


