from configparser import ConfigParser

config = ConfigParser()

config.read("config.ini")

empties = ['[""]', '["", ""]', '[]', "none"]

class Creds:
    TOKEN = config.get("auth", "token")
    WHITELIST = config.get("auth", "admin_users_whitelist").split(",")
    TRIGGER = config.get("trigger", "custom_trigger_word")
    ON_MENTION = config.getboolean("trigger", "respond_on_mention")
    IGNORE_CASE = config.getboolean("trigger", "ignore_case")


def check_creds():
    if not Creds.TOKEN:
        raise Exception("\033[31mPlease set TOKEN in the config.ini file!")
    if Creds.WHITELIST in empties:
        Creds.WHITELIST = []


    print("\033[39m")


check_creds()
