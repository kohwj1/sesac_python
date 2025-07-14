import sqlite3
MY_DATABASE = 'flaskdb.db'

def connect_db():
    conn = sqlite3.connect(MY_DATABASE) #DB 연결
    conn.row_factory = sqlite3.Row #각 행을 dict로 보내줌
    return conn

def create_table():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
            )
        """)

    conn.commit()
    conn.close()

def insert_user(name, age):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("INSERT INTO users (name, age) VALUES(?, ?)", (name, age))

    conn.commit()
    conn.close()

def get_users():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users;")
    rows = cur.fetchall()  #리스트가 리턴됨

    conn.commit()
    conn.close()
    return rows

def get_user(id):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute(f"SELECT * FROM users WHERE id = ?", (id, ))
    row = cur.fetchone()
    conn.commit()
    conn.close()
    if row: #존재하지 않는 쿼리를 요청한 경우 None으로 리턴됨
        return row
    return f'검색한 사용자 {id} 없음'

# def update_user_name(id, name):
#     conn = connect_db()
#     cur = conn.cursor()

#     cur.execute(f"UPDATE users SET name = ? WHERE id = ?", (name, id))

#     conn.commit()
#     conn.close()

# def update_user_age(id, age):
#     conn = connect_db()
#     cur = conn.cursor()

#     cur.execute(f"UPDATE users SET age = ? WHERE id = ?", (age, id))

#     conn.commit()
#     conn.close()

def update_user(id, name, age):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute(f"UPDATE users SET age = ?, name = ? WHERE id = ?", (age, name, id))
    conn.commit()

    conn.close()

def delete_user_by_id(id):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute(f"DELETE FROM users WHERE id = ?", (id, ))

    conn.commit()
    conn.close()