import time

import requests
from Django_test.common.loggin import logger
import pytest



def test_01():
    times = time.struct_time
    logger.info("测试开始" + str(times))


    # assert True


if __name__ == '__main__':
    test_01()

