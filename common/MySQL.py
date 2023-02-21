from Django_test.common.loggin import logger
from Django_test.common.config_path import commfig
import pymysql

data = commfig("mysql")
DB_CONF = {
    "host": data["host"],
    "port": data["port"],
    "user": data["username"],
    "password": data["password"],
    "db": data[""]

}


class MySQLDB:
    def __int__(self, db_conf=None):
        if db_conf is None:
            db_conf = DB_CONF
        self.conn = pymysql.connect(**db_conf, autocommit=True)
        logger.info("-----------数据库连对接成功")
        self.cur = self.conn.cursor(cursor=None)

    def __del__(self):
        self.conn.close()
        self.cur.close()
        logger.info("数据库链接关闭")

    def select_db(self, sql):
        self.conn.ping(reconnect=True)
        self.cur.execute(sql)
        sql_data = self.cur.fetchall()
        logger.info("查询数据结果：{}".format(sql_data))
        return sql_data

    def execute_db(self, sql):
        try:
            self.conn.ping(reconnect=True)
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            logger.debug("操作Mysql出现错误，错误原因为：{}".format(e))
            self.conn.rollback()


db = MySQLDB()
