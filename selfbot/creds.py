from configparser import ConfigParser

config = ConfigParser()

config.read("config.ini")


class Creds:
    TOKEN = config.get("auth", "token")
    TRIGGER = config.get("trigger", "custom_trigger_word")
    ON_MENTION = config.getboolean("trigger", "respond_on_mention")
    MODEL = config.get("ai", "model")
    PROMPT = config.get("ai", "prompt")
    if config.getboolean("ai", "use_external_file_for_prompt"):
        with open("prompt.txt") as f:
            PROMPT = f.read()


def check_creds():
    if not Creds.TOKEN:
        raise Exception("\033[31mPlease set TOKEN in the .env file!")
    if not Creds.TRIGGER:
        raise Exception("\033[31mPlease set TRIGGER in the .env file!")
    if not Creds.PROMPT:
        raise Exception("\033[31mPlease set PROMPT in the .env file!")
    print("\033[39m")


check_creds()
