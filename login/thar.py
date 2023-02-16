from Django_test.login.log import Logs


class Testlog(object):
    def __int__(self):
        self.log = Logs()

    def test_baili_01(self):
        self.log.error("测试开始")


if __name__ == '__main__':
    test = Testlog()
    test.test_baili_01()
