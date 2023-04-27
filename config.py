import configparser
import os.path

Base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(Base_path, "Django_test\config", "config.ini")


def conlog(name):
    cf = configparser.ConfigParser()
    cf.read(data_file_path)
    print("路径：" + data_file_path)
    valuer = cf.get("log", name)
    return valuer


def get_config_mysql(name):
    cf = configparser.ConfigParser()
    cf.read(data_file_path)
    value = cf.get("mysql", name)
    return value


def get_config_log(name):
    cf = configparser.ConfigParser()
    cf.read(data_file_path)
    value = cf.get("log", name)
    return value


def get_ecding_mysql(name):
    cf = configparser.ConfigParser()
    parser.ConfigParser()
    cf.read(data_file_path)
    valuer = cf.get("edcmsql", name)
    return valuer
