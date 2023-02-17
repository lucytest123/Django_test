import configparser as configparser
import json
import yaml

from  Django_test.common.loggin import logger

class MyConfigParser(configparser):
    def __int__(self,dafaults = None):
        configparser.ConfigParser.__init__(self,defaults=dafaults)
    def optionxform(self,optionstr):
        return optionstr


def load_json(file_path):
    logger.info("加载{}文件.....".format(file_path))
    with open(file_path)as f:
        date = json.load(file_path)
    logger.info("读取数据内容：{}".format(date))
    return date


class  readFileData():
    def __int__(self):
        pass
    def load_yaml(self,file_path):
        logger.info("加载{}文件....".format(file_path))
        with open(file_path,encoding="utf-8")as  f:
            data = yaml.safe_load(f)
        logger.info("读取数据==》 {}".format(data))
        return data

    def load_ini(self,file_path):
        logger.info("加载{}文件....".format(file_path))
        config = MyConfigParser()
        config.read(file_path,encoding = "utf-8")
        data = dict(config._sections)
        logger.info("读取数据内容：{}..".format(data))
        return data


data = readFileData()