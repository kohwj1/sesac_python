import sqlite3

DATABASE = 'testdb.db'

def create_connector():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

conn = create_connector()
cur = conn.cursor()

cur.execute(r"""
    CREATE TABLE IF NOT EXISTS users (
        idx INTEGER PRIMARY KEY AUTOINCREMENT,
        tpacode TEXT NOT NULL,
        grade TEXT,
        address TEXT NOT NULL,
        joindate TEXT
    )
""")

conn.commit()
conn.close()