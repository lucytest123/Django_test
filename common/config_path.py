import os
from Django_test.common.read_data import data


def commfig(name):
    Base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    data_file_path = os.path.join(Base_path, "Django_test\config", "config.ini")
    data_url = data.load_ini(data_file_path)[name]
    data_login = data.load_ini(data_url)[name]
    return data_login
