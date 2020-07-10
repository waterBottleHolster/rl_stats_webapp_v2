from app import login
from flask_login import UserMixin
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

db_path = 'rl_stats.db'

class User (UserMixin):
    def __init__(self, id, username, password_hash):
        self.username = username
        self.id = id
        self.password_hash = password_hash

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

@login.user_loader
def load_user(id="0"):
    conn = sqlite3.connect(db_path)
    cur = conn.execute("SELECT id, username, password FROM users WHERE id = ?", (id,))
    cur = cur.fetchone()

    if cur[0] == None:
        return None
    else:
        return User(id=cur[0], username=cur[1], password_hash=cur[2])

