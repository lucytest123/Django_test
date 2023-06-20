import re
import time

import paramiko
from common.loggin import logger


class Linux(object):
    """
    @param
    链接linux服务器
    username: 登陆账号名
    password: 登陆密码
    ip： 服务器地址
    cmd :执行cmd 命令
    """

    def __init__(self, username, password, ip, timeout=30):
        self.username = username
        self.password = password
        self.timeout = timeout
        self.ip = ip
        self.t = ""
        self.chan = ""
        self.try_times = 3

    def Linux_connect(self):
        while True:
            try:
                self.t = paramiko.Transport(sock=(self.ip, 22))
                self.t.connect(username=self.username, password=self.password)
                self.chan = self.t.open_session()
                self.chan.settimeout(self.timeout)
                self.chan.get_pty()
                self.chan.invoke_shell()
                logger.info(u"连接{}成功".format(self.ip))
                logger.info(self.chan.recv(65535).decode("utf-8"))
                return
            except Exception as e:
                if self.try_times != 0:
                    logger.info(u"链接｛｝失败，第｛｝重新链接".format(self.ip, self.try_times))
                    self.try_times -= 1
                else:
                    logger.debug(u"重新链接三次失败，请重新确认：｛｝".format(e))

    def Linux_close(self):
        self.chan.close()
        self.t.close()
        logger.info("{}断开链接".format(self.ip))

    def Linux_send(self, cmd):
        cmd += "\r"
        p = re.compile(r"]$")
        resul = ""
        self.chan.send(cmd)
        while True:
            time.sleep(2)
            ret = self.chan.recv(65535).decode("utf-8")
            resul += ret
            if p.search(ret):
                logger.info(ret)
                return

    def Liunx(self, username, password, ip, cmd):
        L = Linux(username=username, password=password, ip=ip)
        L.Linux_connect()
        L.Linux_send(cmd)
        L.Linux_close()
