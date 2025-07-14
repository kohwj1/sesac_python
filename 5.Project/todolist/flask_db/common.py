import sqlite3
my_todo = 'flask_todo.db'

def connect_db():
    conn = sqlite3.connect(my_todo) #DB 연결
    conn.row_factory = sqlite3.Row #각 행을 dict로 보내줌
    return conn

def create_table():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS todo (
        idx INTEGER PRIMARY KEY AUTOINCREMENT,
        status TEXT,
        content TEXT NOT NULL,
        duedate DATE
        )
    """)

    conn.commit()
    conn.close()

def get_all_list():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM todo ORDER BY status, duedate")
    rows = cur.fetchall()
    
    all_list = [dict(row) for row in rows]

    conn.commit()
    conn.close()
    return all_list

def delete_todo(idx):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("DELETE FROM todo WHERE idx = ?", (idx,))
    conn.commit()
    conn.close()
    # return True

def add_todo(content, duedate=''):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO todo (content, status, duedate) VALUES(?, '', ?)", (content, duedate))
    conn.commit()
    conn.close()
    

def switch_todo(idx):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM todo WHERE idx = ?", (idx, ))
    old_status = cur.fetchone()['status']

    if old_status == 'checked':
        new_status = ''
    else:
        new_status = 'checked'

    cur.execute("UPDATE todo SET status = ? WHERE idx = ?", (new_status, idx))
    conn.commit()
    conn.close()