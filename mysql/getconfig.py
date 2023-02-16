import configparser
import os.path


def get_config_mysql(name):
    cf = configparser.ConfigParser()
    cf.read(os.path.abspath("config.ini"))
    value = cf.get("mysql", name)
    return value


def get_config_log(name):
    cf = configparser.ConfigParser()
    cf.read(os.path.abspath("config.ini"))
    value = cf.get("log", name)
    return value
