import os.path
from Django_test.common.read_data import data
from Django_test.common.loggin import logger
import pymysql
Base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(Base_path,"config","setting.ini")
data = data.load_ini(data_file_path)["mysql"]


DB_CONF= {
    "host":data[""],
    "port":data[""],
    "user":data[""],
    "password":data[""],
    "db":data[""]

}
class MySQLDB():
    def __int__(self, db_conf=DB_CONF):
        self.conn = pymysql.connect(**db_conf,autocommit=True)
        logger.info("-----------数据库连对接成功")
        self.cur = self.conn.cursor(cursor=None)
    def __del__(self):
        self.conn.close()
        self.cur.close()
        logger.info("数据库链接关闭")
    def select_db(self,sql):
        self.conn.ping(reconnect=True)
        self.cur.execute(sql)
        data = self.cur.fetchall()
        logger.info("查询数据结果：{}".format(data))
        return data

    def execute_db(self,sql):
        try:
            self.conn.ping(reconnect=True)
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:

            logger.info("操作Mysql出现错误，错误原因为：{}".format(e))
            self.conn.rollback()
db = MySQLDB(DB_CONF)