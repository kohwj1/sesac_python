import sqlite3

conn = sqlite3.connect('example.db') #DB 연결
cur = conn.cursor()  #입출력 인터페이스 객체

cur.execute(r"""
            UPDATE users
            SET age = 10
            WHERE name = 'alice';
            """)

cur.execute(r"""
            UPDATE users
            SET age = ?
            WHERE name = ?;
            """, (50, 1))

#DB에 변경 내용 반영
conn.commit()

#DB 연결 종료
conn.close()