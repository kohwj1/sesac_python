import sqlite3

conn = sqlite3.connect('example.db') #DB 연결
cur = conn.cursor()  #입출력 인터페이스 객체

#데이터 조회
cur.execute("SELECT * FROM users;")

# #커서를 fetch하여 결과를 rows라는 변수에 담는다
rows = cur.fetchall()
for _, name, age in rows:
    print (name, age)
# rows = cur.fetchone()
# print(rows)


print('-------Fetch 유형별 출력 포맷-------')
#아래와 같이 결과가 한 건만 존재하는 경우 fetchone 으로 가져오는 것이 더 나은 방법
cur.execute("""
            SELECT COUNT(*) FROM users;
            """)
rows = cur.fetchall()  #리스트가 리턴됨
print(rows)
cur.execute("""
            SELECT COUNT(*) FROM users;
            """)
rows = cur.fetchone() #튜플?
print(rows)
cur.execute("""
            SELECT COUNT(*) FROM users;
            """)
rows = cur.fetchone()[0]
print(rows)

#DB에 변경 내용 반영
conn.commit()

#DB 연결 종료
conn.close()