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



# import sqlite3 as sq
#
# with sq.connect('lesson.db') as con_db:
#     cur = con_db.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS students (
#         id INTEGER,
#         name TEXT,
#         sex TEXT,
#         old INTEGER
#     )""")
#     cur.execute("""CREATE TABLE IF NOT EXISTS marks (
#         id INTEGER,
#         subject TEXT,
#         mark INTEGER
#     )""")

#
# import sqlite3 as sq
#
# with sq.connect('lesson.db') as con:
#     cur = con.cursor()
#     cur.execute("""SELECT mark FROM marks WHERE id = 2 AND subject LIKE 'Python'""")
#     cur.execute("""SELECT name, subject, mark FROM marks
#         JOIN students ON students.rowid = marks.id
#         WHERE mark > 3 AND subject LIKE 'Python'""")
#     resault = cur.fetchall()
#     print(resault)



# import sqlite3 as sq
#
# with sq.connect('lesson.db') as con:
#     cur = con.cursor()
#     cur.execute("""SELECT name, subject, mark FROM marks
#         JOIN students ON students.rowid = marks.id
#         WHERE mark > (SELECT mark FROM marks WHERE id = 2 AND subject LIKE 'Python')
#         AND subject LIKE 'Python'""")
#     resault = cur.fetchall()
#     print(resault)


# import sqlite3 as sq
#
# with sq.connect('lesson.db') as con_db:
#     cur = con_db.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS females (
#         id INTEGER,
#         name TEXT,
#         sex TEXT,
#         old INTEGER
#     )""")



# import sqlite3 as sq
#
# with sq.connect('lesson.db') as con:
#     cur = con.cursor()
#     cur.execute("""INSERT INTO females SELECT * FROM students WHERE sex = 'жен'""")
#     resault = cur.fetchall()
#     print(resault)


# import sqlite3 as sq
#
# with sq.connect('lesson.db') as con:
#     cur = con.cursor()
#     cur.execute("""UPDATE marks SET mark = 0 WHERE mark <= (SELECT min(mark) FROM marks WHERE id = 2)""")


#
# import sqlite3 as sq
#
# with sq.connect('lesson.db') as con:
#     cur = con.cursor()
#     cur.execute("""DELETE FROM students WHERE old < (SELECT old FROM students WHERE id = 2)""")


# import sqlite3 as sq
#
# with sq.connect('lesson.db') as con:
#     cur = con.cursor()
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS cars (
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )""")
#
#     cur.execute("""INSERT INTO cars VALUES (1, 'audi', 254125)""")
#     cur.execute("""INSERT INTO cars VALUES (2, 'opel', 564125)""")
#     cur.execute("""INSERT INTO cars VALUES (3, 'skoda', 112125)""")
#     cur.execute("""INSERT INTO cars VALUES (4, 'volvo', 254565)""")
#     cur.execute("""INSERT INTO cars VALUES (5, 'mersedes', 1455125)""")
#     cur.execute("""INSERT INTO cars VALUES (6, 'lada', 25554)""")

# import sqlite3 as sq
#
# cars = [
#     ('kia', 656455),
#     ('tank', 856458),
#     ('haval', 268758),
# ]
#
# with sq.connect('lesson.db') as con:
#     cur = con.cursor()
#
#     for car in cars:
#         cur.execute("""INSERT INTO cars VALUES (NULL, ?, ?)""", car)


# import sqlite3 as sq
#
# cars = [
#     ('ford', 54684),
#     ('honda', 587658),
#     ('bmw', 6847687),
# ]
#
# with sq.connect('lesson.db') as con:
#     cur = con.cursor()
#
#     cur.executemany("""INSERT INTO cars VALUES (NULL, ?, ?)""", cars)


# import sqlite3 as sq
#
# with sq.connect('lesson.db') as con:
#     cur = con.cursor()
#
#     cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'l%'", {'Price': 0})


# import sqlite3 as sq
#
# with sq.connect('lesson.db') as con:
#     cur = con.cursor()
#
#     cur.executescript("""DELETE FROM cars WHERE model LIKE 'l%';
#         UPDATE cars SET price = price + 5000
#                       """)


# import sqlite3 as sq
#
# con = None
# try:
#     con = sq.connect('lesson.db')
#     cur = con.cursor()
#
#     cur.executescript("""CREATE TABLE IF NOT EXISTS cars (
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     BEGIN;
#     INSERT INTO cars VALUES (NULL, 'audi', 254125);
#     INSERT INTO cars VALUES (NULL, 'opel', 564125);
#     INSERT INTO cars VALUES (NULL, 'skoda', 112125);
#     INSERT INTO cars VALUES (NULL, 'volvo', 254565);
#     INSERT INTO cars VALUES (NULL, 'mersedes', 1455125);
#     INSERT INTO cars VALUES (NULL, 'lada', 25554);
#     UPDATE cars SET price = price + 5000
#     """)
#
#     con.commit()
#
# except sq.Error as er:
#     if con: con.rollback()
#     print('Ошибка запроса')
# finally:
#     if con: con.close()


# import sqlite3 as sq
#
# con = None
# try:
#     con = sq.connect('lesson.db')
#     cur = con.cursor()
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS cust
#     (name TEXT, tr_in INTEGER, buy INTEGER)""")
#
#     cur.execute("INSERT INTO cars VALUES (NULL, 'запорожец', 1000)")
#
#     last_row_id = cur.lastrowid
#     buy_car_id = 2
#     cur.execute("INSERT INTO cust VALUES('Федор', ?, ?)", (last_row_id, buy_car_id))
#
#     con.commit()
#
# except sq.Error as er:
#     if con: con.rollback()
#     print('Ошибка запроса')
# finally:
#     if con: con.close()