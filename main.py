import discord
import ollama

from selfbot.creds import Creds


class MyClient(discord.Client):
    def __init__(self, **options):
        super().__init__(self_bot=True, **options)
        self.history = []

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        mentioned = None
        triggered = None
        if Creds.ON_MENTION:
            mentioned = self.user.mentioned_in(message)
        if Creds.TRIGGER != "None":
            triggered = message.content.startswith(Creds.TRIGGER)

        if message.content.startswith('!ai clear'):
            if message.author.id not in Creds.WHITELIST and Creds.WHITELIST != ["", ""] and Creds.WHITELIST:
                pass
            self.history = []
            await message.reply("History cleared!", mention_author=True)

        if triggered or mentioned:
            mes = {
                "role": "user",
                "content": f"{message.content.replace(f"<@{self.user.id}>", "")} | User's name: {message.author.name}",
            }

            cont = self.chat(mes)

            await message.reply(cont, mention_author=True)
            print(self.history)

    def chat(self, message):
        self.history.append(message)
        response = ollama.chat(model="custom-discord-model", messages=self.history)
        self.history.append(response["message"])
        return response["message"]["content"]


client = MyClient()
client.run(Creds.TOKEN)
