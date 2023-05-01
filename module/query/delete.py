from module.query import model
import sqlite3

def send():
    db = "company.db"
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    conn.commit()
    conn.close()