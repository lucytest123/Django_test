import re

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Renshe_NetWork.com import red_config
from Renshe_NetWork.com.video import video_operate
from common.loggin import logger
from com.button import *


class Renshe_NetWork(webdriver):
    def __init__(self):
        self.driver = None
        self.TIME_10 = 10
        self.TIME_480 = 60 * 8
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
        logger.info("登录成功")
        self.driver.get(self.couser_url)
        Renshe_NetWork.switch(self)
        logger.info("打开学习列表")
        Renshe_NetWork.video_list(self, "开始学习")
        Renshe_NetWork.switch(self)
        Renshe_NetWork.Click_learn(self)
        Renshe_NetWork.quit(self)

    def video_list(self, text):
        html = self.driver.page_source
        pattern = r'\b({})\b(?=.*\1)'.format(text)
        # 使用正则表达式匹配页面HTML代码，获取重复出现的文字
        matches = re.findall(pattern, html)
        # 统计重复出现的文字的总数
        count = {}
        for match in matches:
            if match in count:
                count[match] += 1
            else:
                count[match] = 1
        logger.info("视频总数为：{}".format(count))
        return count

    def log_on(self):
        """登录"""
        self.driver.find_element(by=By.XPATH, value=passwork()).send_keys(self.username)
        logger.info("输入账号：")
        time.sleep(self.TIME_10)
        self.driver.find_element(by=By.XPATH, value=uesrname()).send_keys(self.password)
        logger.info("输入密码：")
        time.sleep(self.TIME_10)
        self.driver.find_element(by=By.XPATH, value=logon()).click()
        logger.info("点击登录：")

    def switch(self, position=-1, close=False):
        """切换句柄"""
        all_handles = self.driver.window_handles
        logger.info("当前所有页句柄{}".format(all_handles))
        self.driver.switch_to.window(all_handles[position])
        logger.info("切换后句柄{}".format(all_handles[position]))
        if close:
            self.driver.close()

    def video_paly(self):
        """每八分钟判断一次"""
        times = video_operate.video_time(self) / 5
        while True:
            if times > 1:
                time.sleep(self.TIME_480)
                video_operate.video_paused(self)
                times -= 1
            else:
                logger.info("播放结束")
                break

    def Click_learn(self):
        """相同按钮，依次点击"""
        buttons = self.driver.find_element(by=By.NAME, value="点击学习")
        for button in buttons:
            button.click()
            time.sleep(self.TIME_10)
            Renshe_NetWork.video_paly(self)
            time.sleep(self.TIME_10)
            self.driver.back()

    def quit(self):
        """退出浏览器"""
        self.driver.quit()


if __name__ == '__main__':
    i = Renshe_NetWork()
    i.web_get()
