import time

import pytest as pytest

from Django_test.common.loggin import logger
from Django_test.common.MySQL import MySQLDB

INSERT_sql = "INSERT INTO 'edc.ecoding_taige_edc_mh_raw'(taige_data_point_id,project_no,subject_no,grid_row,mhterm,taige_updated_date,data_from,etl_time)VALUES ({},'TQB2450-III-99',666111,99,'咳痰','2023-03-01 16:10:17','oncology01','2023-03-01 16:10:17')"
delect_sql = "DELETE FROM 'edc'.'ecoding_taige_edc_mh_raw' WHERE project_no = 'TQB2450-III-99'"


def test_mysql():
    for i in range(0, 400000):
        MySQLDB.execute_db( sql=INSERT_sql.format(1630561399338164226 + i))
        logger.info("查询数据{}个".format(i))
        time.sleep(1)


if __name__ == '__main__':
    test_mysql()
