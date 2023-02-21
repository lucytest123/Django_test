import time
from Django_test.common.loggin import logger

def test_01():
    times = time.struct_time
    logger.info("测试开始" + str(times))
    logger.info("测试1")

    # assert True
def test_02():
    time.time_ns()
    logger.info("测试结束")
    logger.info("测死2")

