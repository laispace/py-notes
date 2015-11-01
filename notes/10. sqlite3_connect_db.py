__author__ = 'lai-mini'
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('../data/test.db')
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    ver = cur.fetchone()
    print('sqlite3 version is: %s' % ver)
except lite.Error as e:
    print('Error: %s' % e.args[0])
    sys.exit(1)
finally:
    if (con):
        con.close()


# 使用 with 替代以上的 try...catch 语法，更优雅
# con = lite.connect('../data/test.db')
# with con:
#     cur = con.cursor()
#     cur.execute('SELECT SQLITE_VERSION()')
#     ver = cur.fetchone()
#     print('sqlite3 version is: %s' % ver)


