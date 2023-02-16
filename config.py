import configparser
import os.path


def conlog(name):
    cf = configparser.ConfigParser()
    con_path = os.path.join(os.getcwd(), "config.ini")
    cf.read(con_path)
    valuer = cf.get("log", name)
    print(valuer)
    return valuer
