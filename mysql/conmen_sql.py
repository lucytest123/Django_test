import os.path
from tkinter import E

import pymysql

from Django_test.mysql import getconfig


# 数据库查询，输出所有结果
def readSql(sql):
    user = getconfig.get_config_mysql("user")
    password = getconfig.get_config_mysql("password")
    host = getconfig.get_config_mysql("host")
    database = getconfig.get_config_mysql("mysql_name")

    try:
        coon = pymysql.connect(user=user, password=password, database=database, port="3306", host=host, charset="utf8")
        curosor = coon.cursor()
        # 执行sql 进行查询
        curosor.execute(sql)
        sql_read = curosor.fetchall()
        coon.commit()
        coon.close()
        return sql_read
    except Exception:

        print("数据库连接异常" + E)

