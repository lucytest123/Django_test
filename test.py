import time
from Django_test.common.loggin import logger

def test_01():
    times = time.struct_time
    logger.info("测试开始"+ str(times))

if __name__ == '__main__':

    test_01()