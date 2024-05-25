import os

from dotenv import load_dotenv

load_dotenv()


class Creds:
    TOKEN = os.getenv("TOKEN")
    TRIGGER = os.getenv("TRIGGER")
    PROMPT = os.getenv("PROMPT")


def check_creds():
    if not Creds.TOKEN:
        raise Exception("\033[31mPlease set TOKEN in the .env file!")
    if not Creds.TRIGGER:
        raise Exception("\033[31mPlease set TRIGGER in the .env file!")
    if not Creds.PROMPT:
        raise Exception("\033[31mPlease set PROMPT in the .env file!")
    print("\033[39m")


check_creds()
