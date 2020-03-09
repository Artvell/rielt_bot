# -*- coding:utf-8 -*-
from pymysql import cursors,connect

def getConnection():
    connection=connect(host="",
                        user='',
                        password='',
                        db='',
                        cursorclass=cursors.DictCursor)
    return connection
