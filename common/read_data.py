from configparser import ConfigParser
import json
import os.path

import yaml
import xlrd
from Django_test.common.loggin import logger


class MyConfigParser(ConfigParser):
    def __init__(self, dafaults=None):
        ConfigParser.__init__(self, defaults=dafaults)

    def optionxform(self, optionstr):
        return optionstr


def load_json(file_path):
    logger.info("加载{}文件.....".format(file_path))
    with open(file_path) as f:
        date = json.load(file_path)
    logger.info("读取数据内容：{}".format(date))
    return date


class readFileData():
    def __init__(self):
        pass

    # 读取yaml
    def load_yaml(self, file_path):
        logger.info("加载{}文件....".format(file_path))
        with open(file_path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        logger.info("读取数据==》 {}".format(data))
        return data

    #    读取ini配置文件
    def load_ini(self, file_path):
        try:
            if (os.path.exists(file_path)):
                logger.info("加载{}文件....".format(file_path))
                config = MyConfigParser()
                config.read(file_path, encoding="UTF-8")
                data = dict(config._sections)
                if data is None:
                    data = ""
                return data
            else:
                logger.debug("{}文件路径不存在")
                assert FileNotFoundError
        except Exception as e:
            logger.debug("文件读取失败" + str(e))

    # 读取xls文件 输出行数据
    def load_xls_norws(self, file_path):
        if os.path.exists(file_path):
            logger.info("加载{}文件........".format(file_path))
            config = xlrd.open_workbook(filename=file_path)
            sheet = config.sheet_by_index(0)
            nrows = sheet.nrows  # 获取行数
            logger.info("{}文件行数为：{}".format(file_path, nrows))
            ncols = sheet.ncols  # 获取列数
            logger.info("{}文件列数为：{}".format(file_path, ncols))
            for i in range(0, nrows):
                books = sheet.row_values(i)
                return books

        else:
            logger.debug("{}文件不存在".format(file_path))
            return FileNotFoundError

        # 读取xls文件中的列

    def load_xls_ncols(self, file_path):
        if os.path.exists(file_path):
            logger.info("加载{}文件......".format(file_path))
            config = xlrd.open_workbook(filename=file_path)
            sheet = config.sheet_by_index(0)
            nrows = sheet.nrows  # 获取行数
            logger.info("{}文件行数为：{}".format(file_path, nrows))
            ncols = sheet.ncols  # 获取列数
            logger.info("{}文件列数为：{}".format(file_path, ncols))
            for i in range(0, ncols):
                books = sheet.col_slice(i)
                return books

        else:
            logger.debug("{}文件不存在".format(file_path))
            return FileNotFoundError


data = readFileData()
