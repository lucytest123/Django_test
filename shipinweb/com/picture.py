# 实现连续点击屏幕
import os.path
from ctypes import windll
import win32api
import win32con
import time
import aircv as ac
import pyautogui
from Django_test.common.loggin import logger


class picture_main(object):

    # 图片地址
    def picture_path(self):
        pass
        Base_path = os.path.dirname(os.path.realpath(__file__))
        prcture_path = os.path.join(Base_path, "prctures")
        if os.path.exists(prcture_path):
            os.remove(prcture_path)
            logger.info("文件目录已清除{}".format(prcture_path))
        else:
            os.mkdir(prcture_path)
            logger.info("文件目录不存在，已创建{}".format(prcture_path))
        return prcture_path

    def screenshot(self):
        # 截取屏幕
        # 设置休眠时间，方便切换页面
        print("请在3秒内切换到需要点击的页面！")
        time.sleep(3)
        filename = picture_main.picture_path(self) + 'desktop.png'
        img = pyautogui.screenshot(filename)
        return filename

    def imread_xy(self, imgobj):
        # 获取x,y
        imsrc = ac.imread(picture_main.screenshot(self))
        imobj = ac.imread(imgobj)
        match_result = ac.find_template(imsrc, imobj)
        logger.info(match_result)
        result = str(match_result)
        # 注意这里只能为int类型，否则windll.user32.SetCursorPos(x, y)会报错
        x = int(result[12:14])
        # 工具定位为与程序定位会有偏差，横坐标不变，纵坐标减去25左右（根据实际情况调试）
        y = int(result[18:21]) - 25
        logger.info(x, y)
        return x, y

    # 图片寻找并点击完成
    # imgobj 图片地址
    #  number 点击次数，默认点击一次
    def click_imread(self, imgobj, number=1):
        imgobj_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Photo _Gallery", imgobj)
        x, y = pyautogui.imread_xy(self, imgobj_path)
        # 鼠标移动至指定位置
        for i in range[0, number]:
            windll.user32.SetCursorPos(x, y)
            # 鼠标点击操作
            # MOUSEEVENTF_LEFTDOWN为鼠标左键按住，
            # MOUSEEVENTF_LEFTUP为鼠标左键松开，
            # MOUSEEVENTF_RIGHTDOWN为鼠标右键按住，
            # MOUSEEVENTF_RIGHTUP为鼠标右键松开，
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y)
            time.sleep(0.05)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y)
            # 设置休眠方便切换页面，结束程序
            time.sleep(2)
            logger.info("点击次数{}".format(i))
        logger.info("点击完成！")
