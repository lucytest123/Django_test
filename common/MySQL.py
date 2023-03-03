from Django_test.common.loggin import logger
from Django_test.common.read_data import data
import pymysql
import os

Base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(Base_path, "config", "config.ini")
host = data.load_ini(data_file_path)["edcmsql"]["host"]
logger.info("输出结果为：" + host)
port = int(data.load_ini(data_file_path)["edcmsql"]["port"])
logger.info("输出结果为：" + str(port))
username = data.load_ini(data_file_path)["edcmsql"]["username"]
logger.info("输出结果为：" + username)
password = data.load_ini(data_file_path)["edcmsql"]["password"]
logger.info("输出结果为：" + password)
DB_CONF = {
    "host": host,
    "port": port,
    "user": username,
    "password": password,

}


# 对sql语句进行处理
def MySqlHandle(file_name):
    try:
        file_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        file_path_name = os.path.join(file_path, "MySql", file_name)
        if os.path.exists(file_path_name):
            with open(file_path_name, "r", encoding="utf-8") as f:
                sql_list = f.read().split(";")[::-1]
                for x in sql_list:
                    if "\n" in x:
                        x.replace("\n", " ")
                    if "\r" in x:
                        x.replace("\r", " ")
                    if "  " in x:
                        x.replace("  ", "")
                    sql_item = x + ";"
                    logger.info(".........." + sql_item)
                    return sql_item
    except FileNotFoundError as e:
        logger.debug("文件不存在")
        assert FileNotFoundError


class MySQLDB:
    def __init__(self, db_conf=None):
        if db_conf is None:
            db_conf = DB_CONF
        self.conn = pymysql.connect(**db_conf, autocommit=True)
        logger.info("-----------数据库连对接成功")
        self.cur = self.conn.cursor(cursor=None)

    def __del__(self):
        self.conn.close()
        self.cur.close()
        logger.info("数据库链接关闭")

    def select_db(self, sql_name):
        self.conn.ping(reconnect=True)
        sql = MySqlHandle(sql_name)
        self.cur.execute(sql)
        sql_data = self.cur.fetchall()
        logger.info("查询数据结果：{}".format(sql_data))
        return sql_data

    def execute_db(self, sql_name):
        try:
            self.conn.ping(reconnect=True)
            sql = MySqlHandle(sql_name)
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            logger.debug("操作Mysql出现错误，错误原因为：{}".format(e))
            self.conn.rollback()


db = MySQLDB()
