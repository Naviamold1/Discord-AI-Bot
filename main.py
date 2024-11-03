import asyncio
import logging

import discord
import ollama

from selfbot.creds import Creds

handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
formatter = logging.Formatter(
    "{asctime} | {levelname: <8} | {module}:{funcName}:{lineno} - {message}", style="{"
)


class MyClient(discord.Client):
    def __init__(self, **options):
        super().__init__(self_bot=True, **options)
        self.history = []

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")

    async def on_message(self, message: discord.Message):
        if message.author.id == self.user.id:
            return

        mentioned = None
        triggered = None
        if Creds.ON_MENTION:
            mentioned = self.user.mentioned_in(message)
        if Creds.TRIGGER != "None":
            triggered = message.content.startswith(Creds.TRIGGER)

        if message.content.startswith("!ai clear"):
            if message.author.id in Creds.WHITELIST and Creds.WHITELIST:
                self.history = []
                return await message.reply("History cleared!", mention_author=True)

        if message.content.startswith("!ai history"):
            if message.author.id in Creds.WHITELIST and Creds.WHITELIST:
                print(self.history)
                return await message.reply("Check the terminal!", mention_author=True)

        if triggered or mentioned:
            mes = {
                "role": "user",
                "content": f"{message.content.replace(f"<@{self.user.id}>", "")} | User's name: {message.author.name}",
            }

            if not Creds.DELAY:
                return await message.reply(self.chat(mes), mention_author=True)

            async with message.channel.typing():
                cont = self.chat(mes)
                await asyncio.sleep(len(cont) / 20)

            await message.reply(cont, mention_author=True)

    def chat(self, message: str) -> str:
        self.history.append(message)
        response = ollama.chat(model="custom-discord-model", messages=self.history)
        self.history.append(response["message"])
        return response["message"]["content"]


client = MyClient()
client.run(Creds.TOKEN, log_handler=handler, log_formatter=formatter)
