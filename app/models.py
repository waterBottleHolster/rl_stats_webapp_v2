#!/home/dh_4gxtme/rl-experiment-tracker.com/public/rl_stats_webapp_v2/.flask_venv/bin/python3
from flask_login import UserMixin
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

db_path = 'rl_stats.db'

class User(UserMixin, db.model):
    __tablename__ = 'users'
    id = db.Column(db.integer, primary_key=True)
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

@login.user_loader
def load_user(id):
    conn = sqlite3.connect(db_path)
    cur = conn.execute("SELECT id, username, password FROM users WHERE id = ?",
                        (id,))
    cur = cur.fetchone()

    if cur[0] == None:
        return None
    else:
        return User(username=cur[1], password_hash=cur[2])

