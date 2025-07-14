import sqlite3

conn = sqlite3.connect('example.db') #DB 연결
cur = conn.cursor()  #입출력 인터페이스 객체

cur.execute(r"""
            DELETE FROM users
            WHERE name = ?
            """, ('alice',))  #괄호 속이 1개인 경우 튜블인지 아닌지 자료형 구분이 되지 않으므로, 튜플을 표현하기 위해 괄호 내에 쉼표를 추가 

#DB에 변경 내용 반영
conn.commit()

#DB 연결 종료
conn.close()