import pytest

pytest.main(["-vs",
             r"D:\ProjectLibtary\Django_test\basetest",  # 测试用例地址
             "--report=ecoding.html",
             "--title=ecoding测试报告",
             "--tester=liyunpeng",
             "--desc=测试报告信息",
             "--template=2",
             "reruns=2"
             ])
