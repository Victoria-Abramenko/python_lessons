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

#
# import sqlite3 as sq
#
# with sq.connect('lesson.db') as con_db:
#     cur = con_db.cursor()
#     cur.execute("DROP TABLE IF EXISTS players")
#     cur.execute("DROP TABLE IF EXISTS games")
#     cur.execute("""CREATE TABLE IF NOT EXISTS games (
#         user_id INTEGER,
#         score INTEGER,
#         time INTEGER
#     )""")
#     cur.execute("""CREATE TABLE IF NOT EXISTS players (
#         name TEXT NOT NULL,
#         sex INTEGER NOT NULL DEFAULT 1,
#         old INTEGER,
#         score INTEGER
#     )""")


# import sqlite3 as sq
#
# with sq.connect('lesson.db') as con:
#     cur = con.cursor()
#     cur.execute("""SELECT name, sex, games.score FROM games JOIN players ON games.user_id = players.ROWID""")
#     resault = cur.fetchall()
#     print(resault)

# import sqlite3 as sq
#
# with sq.connect('lesson.db') as con:
#     cur = con.cursor()
#     cur.execute("""SELECT name, sex, sum(games.score) as sum
#         FROM games
#         JOIN players ON games.user_id = players.ROWID
#         GROUP BY user_id
#         ORDER BY sum DESC
#         """)
#     resault = cur.fetchall()
#     print(resault)


# import sqlite3 as sq
#
# with sq.connect('lesson.db') as con_db:
#     cur = con_db.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS tab1 (
#         score INTEGER,
#         `from` TEXT
#     )""")
#     cur.execute("""CREATE TABLE IF NOT EXISTS tab2 (
#         val INTEGER,
#         type TEXT
#     )""")


# import sqlite3 as sq
#
# with sq.connect('lesson.db') as con:
#     cur = con.cursor()
#     cur.execute("""SELECT score, `from` FROM tab1 UNION SELECT val, `type` FROM tab2""")
#     resault = cur.fetchall()
#     print(resault)


# import sqlite3 as sq
#
# with sq.connect('lesson.db') as con:
#     cur = con.cursor()
#     cur.execute("""UPDATE tab1 SET `from` = 'tab2'""")
#     cur.execute("""SELECT score, `from` FROM tab1 UNION SELECT val, `type` FROM tab2""")
#     resault = cur.fetchall()
#     print(resault)

#
# import sqlite3 as sq
#
# with sq.connect('lesson.db') as con:
#     cur = con.cursor()
#     cur.execute("""UPDATE tab1 SET `from` = 'tab1'""")
#     cur.execute("""SELECT score, 'table 1' as tbl FROM tab1 UNION SELECT val, 'table 2' FROM tab2 ORDER BY score DESC""")
#     resault = cur.fetchall()
#     print(resault)