from selenium.webdriver.common.action_chains import ActionChains
from common.loggin import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class video_operate(object):
    def __init__(self):
        self.driver = None
        self.video_element = None

    def video_paused(self):
        """
        判断视频是否暂停，如果暂停，则点击播放
        """
        try:
            if self.video_element.get_attribute("paused") == "true":
                ActionChains(driver=self.driver).click().perform()
                self.video_element.wait_until_not_paused()
                logger.info("视频恢复播放")
            else:
                logger.info("视频未检测到暂停")
        except Exception as e:
            logger.debug("异常抛出：{}".format(e))

    def video_time(self):
        """获取页面视频是藏"""
        try:
            # 查找视频元素
            video_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "video")))
            # 获取视频时长
            video_duration = int(self.driver.execute_script("return arguments[0].duration", video_element))
            logger.info(f"视频时长为：{video_duration}秒")
            return video_duration
        except AssertionError as e:
            logger.debug("视频获取失败：{}".format(e))

    def quit(self):
        """浏览器退出成功"""
        self.driver.quit()
