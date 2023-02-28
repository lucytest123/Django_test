import time
from Django_test.common.loggin import logger
import pytest



def open():
    times = time.struct_time
    logger.info("测试开始" + str(times))
    print(" 测试开始")
    yield
    logger.info("测试结束")
    print("测试结束")
    # assert True



def test_02():
    logger.info("测试用例1")
    logger.info("测死2")
