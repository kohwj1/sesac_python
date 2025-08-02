import sqlite3
from model.init_db import create_connector
import datetime

def get_user(tpacode):
    conn = create_connector()
    # conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    result = cursor.execute("SELECT * FROM users WHERE tpacode = ?", (tpacode, ))
    data = result.fetchone()

    conn.close()

    if data == None:
        return {}
    return dict(data)

def join_user(tpacode, grade, address):
    joindate = str(datetime.datetime.now())
    conn = create_connector()
    cursor = conn.cursor()

    cursor.execute("""
            INSERT INTO users(tpacode, grade, address, joindate)
                VALUES(?, ?, ?, ?)""", (tpacode, grade, address, joindate))
    conn.commit()
    conn.close()


def update_user(tpacode, grade, address):
    conn = create_connector()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users
            SET grade = ?, address = ?
            WHERE tpacode = ?""", (grade, address, tpacode))
    
    conn.commit()
    conn.close()