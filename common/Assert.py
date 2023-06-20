import json

from common.loggin import logger
import common


class Assertion:

    def Assert_code(self, code, expected_code):
        """
        判断code 是否符合预期结果
        code:
        :excepted_code :
        """
        try:
            assert code == expected_code
            return True
        except:
            logger.error("statusCode error, expected_code is %s, statusCode is %s " % (expected_code, code))
            common.RESULT_LIST.append("fail")
            raise

    def Assert_in_text(self, body, expected_msg):
        """
        验证boby中是否包含预期字段（expected_msg）
        body: 输入字段
        expected_msg ： 预期包含字段
        """

        try:
            text = json.dumps(body, ensure_ascii=ReferenceError)
            assert expected_msg in text
            return True
        except:
            logger.error("Response body Does not contain expected_msg, expected_msg is %s" % expected_msg)
            common.RESULT_LIST.append("fail")
            raise

    def Assert_time(self, time, expected_time):
        """
        判断请求时间是否超出预期时间
        time: 请求时间（毫秒）
        expected_time :  预期时间（毫秒）
        """
        try:
            assert time < expected_time
            return True
        except:
            logger.debug("Response time > expected_time, expected_time is {}, time is {}".format(expected_time, time))
            common.RESULT_LIST.append("fail")
            raise
