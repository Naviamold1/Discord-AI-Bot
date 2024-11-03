from configparser import ConfigParser

import colorama
from discord import AuthFailure

config = ConfigParser()

config.read("config.ini")

empties = ['[""]', '["", ""]', "[]", "none"]


class Creds:
    TOKEN = config.get("auth", "token")
    WHITELIST = config.get("auth", "admin_users_whitelist").split(",")
    TRIGGER = config.get("trigger", "custom_trigger_word", fallback=None)
    ON_MENTION = config.getboolean("trigger", "respond_on_mention", fallback=True)
    IGNORE_CASE = config.getboolean("trigger", "ignore_case", fallback=True)
    DELAY = config.getboolean("misc", "artificial_delay", fallback=True)


def check_creds():
    keys = [config.options(section) for section in config.sections()]

    config.read("config.example.ini")
    keys_example = [config.options(section) for section in config.sections()]

    if keys != keys_example:
        print(
            colorama.Fore.RED + "config.ini file is outdated" + colorama.Style.RESET_ALL
        )

    if Creds.WHITELIST in empties:
        Creds.WHITELIST = []


check_creds()
