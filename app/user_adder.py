import sqlite3
from werkzeug.security import generate_password_hash
import sys

def insert_user(username, password):
    password_hash = generate_password_hash(password)
    conn = sqlite3.connect('rl_stats.db')
    conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", 
                (username, password_hash))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_user(sys.argv[1], sys.argv[2])