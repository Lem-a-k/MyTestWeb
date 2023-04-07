# про БД
# sqlite
# результат в csv

import sqlite3

connect = sqlite3.connect('db.db')  # input()
# запросы
cur = connect.cursor()
# data = cur.execute(...).fetchall()
connect.close()

import csv
with open('...', 'w', newline='') as f:
    # DictWriter, fieldnames, delimiter,
    # .writeheader()
    pass
