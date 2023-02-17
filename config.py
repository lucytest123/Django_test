import configparser
import os.path


def conlog(name):
    cf = configparser.ConfigParser()
    con_path = os.path.join(os.getcwd(), "config.ini")
    cf.read(con_path)
    valuer = cf.get("log", name)
    return valuer


def get_config_mysql(name):
    cf = configparser.ConfigParser()
    cf.read(os.path.join(os.getcwd(), "config.ini"))
    value = cf.get("mysql", name)
    return value


def get_config_log(name):
    cf = configparser.ConfigParser()
    cf.read(os.path.join(os.getcwd(), "config.ini"))
    value = cf.get("log", name)
    return value










