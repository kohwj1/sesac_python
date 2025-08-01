import sqlite3
import hashlib

def hash_password(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

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

# #테스트 데이터 추가
# cur.execute(f"INSERT INTO users (username, password, name) VALUES (?, ?, ?)", ('user1', hash_password('password1'), 'UserName1'))
# cur.execute(f"INSERT INTO users (username, password, name) VALUES (?, ?, ?)", ('user2', hash_password('password2'), 'UserName2'))

#db 쓰기 커밋
conn.commit()
conn.close()