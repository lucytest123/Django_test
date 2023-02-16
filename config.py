import configparser
import os.path


def conlog(name):
    cf = configparser.ConfigParser()
    path1 = os.getcwd()
    con_path = os.path.join(path1, "config.ini")

    print(con_path)
    cf.read(os.path.relpath("config.ini"))
    valuer = cf.get("log", name)
    print(valuer)
    return valuer
