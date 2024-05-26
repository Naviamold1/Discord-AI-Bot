from configparser import ConfigParser

config = ConfigParser()

config.read("config.ini")


class Creds:
    TOKEN = config.get("main", "token")
    TRIGGER = config.get("main", "trigger")
    PROMPT = config.get("main", "prompt")
print(Creds.PROMPT)

def check_creds():
    if not Creds.TOKEN:
        raise Exception("\033[31mPlease set TOKEN in the .env file!")
    if not Creds.TRIGGER:
        raise Exception("\033[31mPlease set TRIGGER in the .env file!")
    if not Creds.PROMPT:
        raise Exception("\033[31mPlease set PROMPT in the .env file!")
    print("\033[39m")


check_creds()
