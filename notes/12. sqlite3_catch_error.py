__author__ = 'lai-mini'
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

try:
    con = lite.connect('../data/test.db')
    cur = con.cursor()

    # 使用 executescript 一次执行完所有 sql 语句
    cur.executescript("""
        DROP TABLE IF EXISTS users;
        CREATE TABLE users(id INT, name TEXT, email TEXT);
        INSERT INTO users VALUES(1,'laixiaolai1','laixiaolai1@laispace.com');
        INSERT INTO users VALUES(2,'laixiaolai2','laixiaolai2@laispace.com');
        INSERT INTO users VALUES(3,'laixiaolai3','laixiaolai3@laispace.com');
        INSERT INTO users VALUES(4,'laixiaolai4','laixiaolai4@laispace.com');
        INSERT INTO users VALUES(5,'laixiaolai5','laixiaolai5@laispace.com');
        INSERT INTO users VALUES(6,'laixiaolai6','laixiaolai6@laispace.com');
        """)

    # 不是用 with 语句的，则必须手动 commit 提交修改
    con.commit()

except lite.Error as e:
    if con:
        # 回滚
        con.rollback()
    print("Error %s:" % e.args[0])
    sys.exit(1)

finally:
    if con:
        con.close()
