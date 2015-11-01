__author__ = 'lai-mini'
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('../data/test.db')

id = 3
name = 'laixiaolai333333'

with con:
    cur = con.cursor()
    cur.execute('UPDATE users SET name=? WHERE id=?', (name, id))
    con.commit()

    print('%s row(s) updated' % cur.rowcount)

with con:
    cur = con.cursor()
    cur.execute('SELECT * FROM users WHERE id=:id', {'id': id})

    row = cur.fetchone()
    print(row)