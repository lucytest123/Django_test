import time

import requests
from Django_test.common.loggin import logger
import pytest


@pytest
def test_01():
    times = time.struct_time
    logger.info("测试开始" + str(times))
    log = requests.get(url = " ")
    log.request.cookies()
    assert False


if __name__ == '__main__':
    test_01()
    pytest.main(allure=True)
