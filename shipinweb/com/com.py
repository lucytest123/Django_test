import time

from selenium import webdriver

from Django_test.common.loggin import logger
from Django_test.shipinweb.com.picture import click_imread


class Test_web_url():
    def __init__(self):
        self.url = None
        self.time1 = 1
        self.Current_time = time.time()

    def get_web(self):
        self.derver = webdriver.Chrome
        self.derver.get(self.url)
        self.derver.maximize_window()
        time.sleep(self.time1)

    # 页面定位查找 支持多种定位方法，默认使用xpath
    #     ID = "id"
    #     XPATH = "xpath"
    #     LINK_TEXT = "link text"
    #     PARTIAL_LINK_TEXT = "partial link text"
    #     NAME = "name"
    #     TAG_NAME = "tag name"
    #     CLASS_NAME = "class name"
    #     CSS_SELECTOR = "css selector"
    def elements(self, by="xpath", positioning=None):
        if positioning != None:
            self.derver.find_element(by=by, value=positioning)
        else:
            logger.debug("定位地址为空.{}".format(positioning))
            assert False

    # 窗口句柄切换，默认切换到最新一个
    def switch(self, position=-1):
        if not position.isdigit():
            logger.debug("position传参错误，只能为整数")
            assert False
        else:
            all_handles = self.derver.window_handles
            logger.info("当前所有页句柄{}".format(all_handles))
            self.derver.switch_to.window(all_handles[position])
            logger.info("切换后句柄{}".format(all_handles[position]))

    # 窗口切换到首页
    def current(self):
        all_handle = self.derver.current_window_handle
        self.derver.switch_to.window(all_handle)

    # 滑动页面查找文字
    def fand_text(self, text):
        while True:
            time2 = self.Current_time + 1000
            find_text = self.derver.find_element(by="text", value=text)
            if find_text:
                return True
            elif time2 < self.Current_time:
                return False
            # 向下滑动500像素
            self.derver.execute_script("window.scrollBy(0,500)")

    # 根据图片寻找位置并点击
    def fand_picture(self, picture):
        click_imread(picture, number=1)
