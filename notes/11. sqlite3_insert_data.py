__author__ = 'lai-mini'
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

# 使用 with 替代以上的 try...catch 语法，更优雅
con = lite.connect('../data/test.db')
with con:
    cur = con.cursor()

    # 为了测试，删除已有的数据表
    cur.execute("DROP TABLE IF EXISTS users")

    # 先创建一个数据表
    cur.execute('CREATE TABLE IF NOT EXISTS users(id INT, name TEXT, email TEXT)')

    # 插入数据
    cur.execute('INSERT INTO users VALUES(1, "laixiaolai1", "laixiaolai1@laispace.com")')
    cur.execute('INSERT INTO users VALUES(2, "laixiaolai2", "laixiaolai2@laispace.com")')
    cur.execute('INSERT INTO users VALUES(3, "laixiaolai3", "laixiaolai3@laispace.com")')

    users = [
        (4, 'laixiaolai4', 'laixiaolai4@laispace.com'),
        (5, 'laixiaolai4', 'laixiaolai4@laispace.com'),
        (6, 'laixiaolai4', 'laixiaolai4@laispace.com')
    ]

    cur.executemany('INSERT INTO users VALUES(?, ?, ?)', users)

    # 在 with 语句中， commit 操作可缺省
    # con.commit()
    # con.close()

