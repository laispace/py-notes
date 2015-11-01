__author__ = 'lai-mini'
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('../data/test.db')

id = 3
name = 'laixiaolai333333'


# 列出表头
with con:

    cur = con.cursor()

    cur.execute('PRAGMA table_info(users)')

    data = cur.fetchall()

    for d in data:
        print(d[0], d[1], d[2])


# 列出表头和数据
with con:

    cur = con.cursor()
    cur.execute('SELECT * FROM users')

    # 输出列名
    col_names = [cn[0] for cn in cur.description]

    rows = cur.fetchall()

    print("%2s %-20s %s" % (col_names[0], col_names[1], col_names[2]))

    for row in rows:
        print("%2s %-20s %s" % row)

# 列出所有的数据表
with con:

    cur = con.cursor()
    # 表信息存放在 sqlite_master 中
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")

    rows = cur.fetchall()

    for row in rows:
        print(row[0])