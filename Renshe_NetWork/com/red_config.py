import configparser
import os.path

con_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "Django_test/Renshe_NetWork/com",
                        "config.ini")


def zu_config(value):
    comfig = configparser.ConfigParser()
    comfig.read(con_path)
    values = comfig.get("zu", value)
    return values
