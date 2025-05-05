# # __________________ lesson 2 _____________________
# import sqlite3 as sq
#
# with sq.connect('lesson.db') as con_bd:
#     cur = con_bd.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS players (
#         name TEXT,
#         sex INTEGER,
#         old INTEGER,
#         score INTEGER
#     )
#     """)

# import sqlite3 as sq
#
# with sq.connect('lesson.db') as con_db:
#     cur = con_db.cursor()
#     cur.execute("DROP TABLE players")

# import sqlite3 as sq
#
# with sq.connect('lesson.db') as con_bd:
#     cur = con_bd.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS players (
#         name TEXT NOT NULL,
#         sex INTEGER NOT NULL DEFAULT 1,
#         old INTEGER,
#         score INTEGER
#     )
#     """)

# import sqlite3 as sq
#
# with sq.connect('lesson.db') as con_db:
#     cur = con_db.cursor()
#     cur.execute("DROP TABLE IF EXISTS players")
#     cur.execute("""CREATE TABLE IF NOT EXISTS players (
#         user_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         sex INTEGER NOT NULL DEFAULT 1,
#         old INTEGER,
#         score INTEGER
#     )""")

# import sqlite3 as sq
#
# with sq.connect('lesson.db') as con:
#     cur = con.cursor()
#     # cur.execute("""INSERT INTO players (name, sex, old, score) VALUES ('Ксения', 2, 42, 100)""")
#     cur.execute("""SELECT * FROM players WHERE score > 500
#         ORDER BY score DESC""")
#     # resault = cur.fetchall()
#     for resault in cur:
#         print(resault)
#
# import sqlite3 as sq
#
# with sq.connect('lesson.db') as con:
#     cur = con.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXISTS games (
#         user_id INTEGER,
#         name TEXT NOT NULL,
#         score INTEGER
#     )''')