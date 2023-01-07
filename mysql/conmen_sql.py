import pymysql


def readSql(sql):
    user = ""
    password = ""
    db = ''
    try:
        coon = pymysql.conect(user, password, db, port="3306", host="", charset="utf8")
        curosor = coon.cursor()
        # 执行sql 进行查询
        aa = curosor.execute(sql)
        info = curosor.fetchamany(aa)

    finally:
        pass
