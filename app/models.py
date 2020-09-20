#!/home/dh_4gxtme/rl-experiment-tracker.com/public/rl_stats_webapp_v2/.flask_venv/bin/python3
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app, request, url_for
from flask_login import UserMixin

from . import db, login_manager


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    game_events = db.relationship('GameEvent', backref='user', lazy='dynamic')

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class GameEvent(db.Model):
    __tablename__ = 'game_events'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    username = db.Column(db.String, db.ForeignKey('users.username'))
    game_result = db.Column(db.String, nullable=False)
    topper = db.Column(db.String, nullable=False)
    game_mode = db.Column(db.String, nullable=False)
    partied = db.Column(db.String, nullable=False)
    team = db.Column(db.String, nullable=False)
    vehicle = db.Column(db.String, nullable=False)
    antenna = db.Column(db.String, nullable=False)
    fov = db.Column(db.Integer, nullable=False)
    distance = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    angle = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.String, nullable=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
