import sqlite3

conn = sqlite3.connect('example.db') #DB 연결
cur = conn.cursor()  #입출력 인터페이스 객체

#커서
cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
            )
        """)
# IF NOT EXISTS 조건문은 테이블 생성 시에만 가능 (데이터 인서트같은 경우에는 불가)

#DB에 변경 내용 반영
conn.commit()

#DB 연결 종료
conn.close()