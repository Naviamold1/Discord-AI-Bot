import discord
import ollama
from dotenv import load_dotenv

from selfbot.creds import Creds

load_dotenv()

modelfile = f"""
FROM llama3
SYSTEM {Creds.PROMPT}
"""
ollama.create(model="custom", modelfile=modelfile)


class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith(Creds.TRIGGER):
            response = ollama.chat(
                model="custom",
                messages=[
                    {
                        "role": "user",
                        "content": message.content.replace(Creds.TRIGGER, ""),
                    },
                ],
            )
            await message.reply(response["message"]["content"], mention_author=True)


client = MyClient()
client.run(Creds.TOKEN)
