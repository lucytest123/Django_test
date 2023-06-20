from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Renshe_NetWork.com import red_config
from common.loggin import logger
from com.button import *


class Renshe_NetWork(object):
    def __init__(self):
        self.TIME_10 = 10
        self.TIME_100 = 100
        self.log_url = red_config.zu_config("log_url")
        self.username = red_config.zu_config("username")
        self.password = red_config.zu_config("password")
        self.couser_url = red_config.zu_config("course_list_url")

    def web_get(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        time.sleep(self.TIME_10)
        self.driver.get(self.log_url)
        Renshe_NetWork.log_on(self)
        self.driver.get(self.couser_url)
        Renshe_NetWork.switch(self)

    def video_list(self):
        pass

    def log_on(self):
        self.driver.find_element(by=By.XPATH, value=passwork()).send_keys(self.username)
        logger.info("输入账号：")
        time.sleep(self.TIME_10)
        self.driver.find_element(by=By.XPATH, value=uesrname()).send_keys(self.password)
        logger.info("输入密码：")
        time.sleep(self.TIME_10)
        self.driver.find_element(by=By.XPATH, value=logon()).click()
        logger.info("点击登录：")

    def switch(self, position=-1):
        all_handles = self.driver.window_handles
        logger.info("当前所有页句柄{}".format(all_handles))
        self.driver.switch_to.window(all_handles[position])
        logger.info("切换后句柄{}".format(all_handles[position]))


if __name__ == '__main__':
    i = Renshe_NetWork()
    i.web_get()
