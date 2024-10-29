import discord
import ollama

from selfbot.creds import Creds

modelfile = f"""
FROM {Creds.MODEL}
SYSTEM {Creds.PROMPT}
"""
ollama.create(model="custom", modelfile=modelfile)

print(Creds.PROMPT)


class MyClient(discord.Client):
    def __supper__(self):
        super().__init__(self_bot=True)

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

        if triggered or mentioned:
            response = ollama.chat(
                model="custom",
                messages=[
                    {
                        "role": "user",
                        "content": f"{message.content.replace(f"<@{self.user.id}>", "")} | Person that you are replying to is called {message.author.name}",
                    },
                ],
            )
            await message.reply(response["message"]["content"], mention_author=True)


client = MyClient()
client.run(Creds.TOKEN)
