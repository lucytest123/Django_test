import logging
import logging.handlers
import os, time
from pathlib import Path

from Django_test import config

file_path = config.conlog("log_path")

log_dir = Path(file_path)
if not log_dir.is_dir():
    log_dir.mkdir(parents=True)


class Logger():

    def __init__(self):
        self.logname = os.path.join(log_dir, "{}.log".format(time.strftime("%Y%m%d-%H%M%S")))
        self.logger = logging.getLogger("log")
        self.logger.setLevel(logging.DEBUG)
        self.formater = logging.Formatter(
            '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')
        self.filelogger = logging.FileHandler(self.logname, mode='a', encoding="UTF-8")
        self.console = logging.StreamHandler()
        self.console.setLevel(logging.DEBUG)
        self.filelogger.setLevel(logging.DEBUG)
        self.filelogger.setFormatter(self.formater)
        self.console.setFormatter(self.formater)
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)


logger = Logger().logger
