import sqlite3
# import hashlib
import bcrypt

def hash_password(pw):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pw.encode(), salt)

def create(userid, userpw, name):
    hashpw = hash_password(userpw)
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.cursor()
    cur.execute(f"INSERT INTO users (username, password, name) VALUES (?, ?, ?)", (userid, hashpw, name))
    conn.commit()
    conn.close()

DB_FILENAME = 'users.db'

conn = sqlite3.connect(DB_FILENAME)
cur = conn.cursor()

#테이블 생성 / 컬럼 세팅
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    name TEXT NOT NULL
)
""")

if __name__ == '__main__':
    # #테스트 데이터 추가
    create('user1', 'password1', 'UserName1')
    create('user2', 'password2', 'UserName2')

    #db 쓰기 커밋
    conn.commit()
    conn.close()