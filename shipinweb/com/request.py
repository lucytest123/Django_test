import requests
from bs4 import BeautifulSoup
from Django_test.common.loggin import logger


class video(object):
    def __init__(self):
        self.outtimes = 0
        self.i = 0

    def duration(self, url):
        """获取视频总时间
        url: 访问地址"""
        response = requests.get(url)
        sopu = BeautifulSoup(response.text, "html.parser")
        self.outtimes = sopu.find("span", {"id": "video-time"})["date-content"]
        logger.info("获取视频总时长为｛｝".format(self.outtimes))
        return self.outtimes

    def video_clieas(self):
        pass
