import sqlite3

conn = sqlite3.connect('example.db') #DB 연결
cur = conn.cursor()  #입출력 인터페이스 객체

cur.execute(r"""
            INSERT INTO users (name, age) VALUES (?, ?)
            """, ('Charlie', 40))

#DB에 변경 내용 반영
conn.commit()

#DB 연결 종료
conn.close()