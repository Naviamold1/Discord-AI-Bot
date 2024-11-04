import asyncio
import logging

import discord
import ollama
from discord.ext import commands

from selfbot.creds import Creds

handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
formatter = logging.Formatter(
    "{asctime} | {levelname: <8} | {module}:{funcName}:{lineno} - {message}", style="{"
)


bot = commands.Bot(command_prefix="!ai ", user_bot=True)
history = []
lock = asyncio.Lock()


async def is_whitelist(ctx: commands.Context):
    if ctx.author.id in Creds.WHITELIST and Creds.WHITELIST:
        return True
    if Creds.WHITELIST:
        return True
    return False


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")


@bot.command(name="clear")
@commands.check(is_whitelist)
async def clear(ctx: commands.Context):
    history.clear()
    await ctx.send("History cleared!", mention_author=True)


@bot.command(name="history")
@commands.check(is_whitelist)
async def get_history(ctx: commands.Context):
    print(history)
    await ctx.send("Check the terminal!", mention_author=True)


@bot.event
@commands.max_concurrency(1)
async def on_message(message: discord.Message):
    if message.author.id == bot.user.id:
        return

    await bot.process_commands(message)

    mentioned = None
    triggered = None
    if Creds.ON_MENTION:
        mentioned = bot.user.mentioned_in(message)
    if Creds.TRIGGER != "None" and Creds.TRIGGER:
        triggered = message.content.startswith(Creds.TRIGGER)

    if triggered or mentioned:
        mes = {
            "role": "user",
            "content": f"{message.content.replace(f"<@{bot.user.id}>", "")} | User's name: {message.author.name}",
        }

        if not Creds.DELAY:
            return await message.reply(chat(mes), mention_author=True)

        async with message.channel.typing():
            async with lock:
                cont = chat(mes)
                await asyncio.sleep(len(cont) / Creds.DELAY_VALUE)

        await message.reply(cont, mention_author=True)


def chat(message: str) -> str:
    history.append(message)
    response = ollama.chat(model="custom-discord-model", messages=history)
    history.append(response["message"])
    return response["message"]["content"]


bot.run(Creds.TOKEN, log_handler=handler, log_formatter=formatter)
