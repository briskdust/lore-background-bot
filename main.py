import discord
import os

import requests
import json

from dotenv import load_dotenv

load_dotenv()

client = discord.Client()


def get_champ(name):
    req = requests.get(f"https://ddragon.leagueoflegends.com/cdn/12.8.1/data"
                       f"/en_US/champion/{name.title()}.json")
    description = json.loads(req.text)
    return description["data"][name.title()]["lore"]


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    if msg.content.startswith("$//"):
        description = get_champ(msg.content[3:])
        await msg.channel.send(description)


client.run(os.getenv("TOKEN"))
