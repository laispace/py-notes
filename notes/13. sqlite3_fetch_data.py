__author__ = 'lai-mini'
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('../data/test.db')

# 使用 tuple 方式输出
with con:
    cur = con.cursor()
    cur.execute('SELECT * FROM users')

    rows = cur.fetchall()
    for row in rows:
        print(row)


# 使用 list 方式输出
with con:
    con.row_factory = lite.Row

    cur = con.cursor()
    cur.execute('SELECT * FROM users')

    rows = cur.fetchall()
    for row in rows:
        print(row['id'], row['name'], row['email'])