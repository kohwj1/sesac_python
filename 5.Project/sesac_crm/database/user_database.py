import sqlite3

DATABASE = 'database/mycrm.db'

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def get_all_list(page, pagesize) -> list | None:
    off_start = (page - 1) * pagesize
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT *, COUNT(*) OVER() AS Totalcount FROM users LIMIT ? OFFSET ?", (pagesize, off_start))
    return cur.fetchall()

def search_users_by_name(name, page, pagesize) -> list | None:
    off_start = (page - 1) * pagesize
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT *, COUNT(*) OVER() AS Totalcount FROM users WHERE Name LIKE ? LIMIT ? OFFSET ?", (f'%{name}%', pagesize, off_start))
    return cur.fetchall()

def filter_gender(gender, page, pagesize) -> list | None:
    off_start = (page - 1) * pagesize
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT *, COUNT(*) OVER() AS Totalcount FROM users WHERE Gender = ? LIMIT ? OFFSET ?", (gender, pagesize, off_start))
    return cur.fetchall()

def get_user_info(userid):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE Id = ?", (userid, ))
    user_info = cur.fetchone()

    def get_user_history(userid):
        cur.execute("""SELECT o.Id AS OrderId, o.OrderAt AS OrderAt, s.Name AS StoreName, s.Id AS StoreId
                    FROM users u
                    JOIN orders o ON u.Id = o.UserId
                    JOIN stores s ON o.StoreId = s.Id 
                    WHERE u.Id = ?
                    ORDER BY OrderAt DESC""", (userid, ))
        user_history = cur.fetchall()
        return user_history

    user_history = get_user_history(userid)
    
    #로그 확인좀
    for u in user_history:
        print(dict(u))

    return {'info':user_info, 'history':user_history}