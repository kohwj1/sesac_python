import sqlite3

conn = sqlite3.connect('example.db') #DB 연결
cur = conn.cursor()  #입출력 인터페이스 객체

#커서
# cur.execute("""
#             CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             age INTEGER NOT NULL
#             )
#         """)
# IF NOT EXISTS 조건문은 테이블 생성 시에만 가능 (데이터 인서트같은 경우에는 불가)

# cur.execute(r"""
#             INSERT INTO users (name, age) VALUES ('alice', 30)
#             """)

#Placeholder(?)와 Prepared statement를 이용한 인서트 -- SQL injection 방지
cur.execute("""
            SELECT COUNT(*) FROM users;
        """)
count = cur.fetchone()[0]

if not count:
    cur.execute(r"INSERT INTO users (name, age) VALUES ('alice', 30)")
    cur.execute(r"INSERT INTO users (name, age) VALUES (?, ?)", ('Charlie', 40))

else:
    print(f'현재 있는 사용자 데이터 개수: {count}개')

#DB에 변경 내용 반영
conn.commit()

#DB 연결 종료
conn.close()