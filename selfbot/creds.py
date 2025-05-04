import json
import sys
from configparser import ConfigParser

import colorama
import ollama

config = ConfigParser()

config.read("config.ini")


class Creds:
    TOKEN = config.get("auth", "token")
    WHITELIST = json.loads(config.get("auth", "admin_users_whitelist"))
    TRIGGER = config.get("trigger", "custom_trigger_word", fallback=None)
    ON_MENTION = config.getboolean("trigger", "respond_on_mention", fallback=True)
    IGNORE_CASE = config.getboolean("trigger", "ignore_case", fallback=True)
    DELAY = config.getboolean("misc", "artificial_delay", fallback=True)
    DELAY_VALUE = config.getint("misc", "artificial_delay_value", fallback=20)


def check_creds():
    keys = [config.options(section) for section in config.sections()]

    config.read("config.example.ini")
    keys_example = [config.options(section) for section in config.sections()]

    if keys != keys_example:
        print(
            colorama.Fore.RED + "config.ini file is outdated" + colorama.Style.RESET_ALL
        )

    if not Creds.TOKEN or Creds.TOKEN == "YOUR_DISCORD_TOKEN":
        print(colorama.Fore.RED + "Account token is missing" + colorama.Style.RESET_ALL)
        sys.exit()

    if not Creds.WHITELIST:
        print(
            colorama.Fore.LIGHTYELLOW_EX
            + "No whitelist set; everyone is able to run special commands"
            + colorama.Style.RESET_ALL
        )

    ollama.chat(
        model="custom-discord-model",
        messages=[{"role": "user", "content": "ONLY SAY 1"}],
    )


check_creds()
