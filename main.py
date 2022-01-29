import os
import discord
from webserver import keep_alive
from discord.ext import commands
import json


def load():
    with open("database/prefix.json", "r") as file:
        return json.load(file)



data = load()
intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=data["prefix"],help_command=None,intents=intents)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=f'Prefix '+data["prefix"]+' help'))
    print(f'---------------------------\n{client.user} is Online!!\n---------------------------')


for filename in os.listdir("./cogs"):
  if filename.endswith('.py'):
    client.load_extension(f"cogs.{filename[:-3]}")

keep_alive()
client.run(os.environ['TOKEN'])