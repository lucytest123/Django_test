import logging
import logging.handlers
import os.path
from pathlib import Path


class Logs(object):
    """
    日志类，日志分流
    """

    def __init__(self):
        file_path = os.path.abspath("./report/")
        log_dir = Path(file_path+'log')
        if not log_dir.is_dir():
            log_dir.mkdir(parents=True)

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        logfilename = 'login.log'
        logfilepath = str(log_dir / logfilename)

        console = logging.StreamHandler()
        console.setLevel(logging.INFO)

        rotatfile = logging.handlers.RotatingFileHandler(logfilepath, 'a', 20971520, 2, 'utf-8')
        rotatfile.setLevel(logging.DEBUG)

        if not self.logger.handlers:
            self.logger.addHandler(console)
            self.logger.addHandler(rotatfile)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console.setFormatter(formatter)
        rotatfile.setFormatter(formatter)

    def warning(self, log_message):
        self.logger.warning(log_message)

    def info(self, log_message):
        self.logger.info(log_message)

    def critical(self, log_message):
        self.logger.critical(log_message)

    def error(self, log_message):
        self.logger.error(log_message)

    def debug(self, log_message):
        self.logger.debug(log_message)

LOGS = Logs()
