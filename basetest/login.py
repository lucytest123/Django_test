import logging
import os

import pytest as pytest

from Django_test.common import Assert
from Django_test.common.loggin import logger
from Django_test.common.read_data import data
import requests

Base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(Base_path, "config", "config.ini")
data_url = data.load_ini(data_file_path)["log"]
data_login = data.load_ini(data_url)["login"]


class Test_login(pytest):
    def __int__(self):
        self.url = data_url
        self.data_json = {
            "username": data_login["username"],
            "password": data_login["password"]
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
