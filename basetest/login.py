import logging
import pytest as pytest

from Django_test.common import Assert
from Django_test.common.loggin import logger
from Django_test.common.config_path import commfig
import requests




class Test_login(pytest):
    def __int__(self):
        self.url = commfig("log")
        data = commfig("login")
        self.data_json = {
            "username": data["username"],
            "password": data["password"]
        }

    @pytest.fixture()
    def testlogin(self):
        login = requests.get(url=self.url, params=self.data_json)
        logger.info("请求地址:{}".format(login))
        """判断返回的状态码"""
        code = login.status_code
        Assert.Assertion.Assert_code(self, code=code, expected_code="200")
        cookies = login.cookies()
        logger.info("请求地址后cookies:{}".format(cookies))
        return cookies
