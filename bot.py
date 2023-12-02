import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import time
from discord.ext import tasks 
from asana_test import get_completed
load_dotenv()

TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(("prefix"), intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} bot')
    channel = await client.fetch_channel(os.getenv('DISCORD_CHANNEL'))
    await task.start(channel)

@tasks.loop(seconds=360)
async def task(channel):
    completed = get_completed()
    print("task running")
    for task in completed:
        if task["completed"]:
            await channel.send("> Task completed: " + task["name"])
            time.sleep(1)
 


client.run(TOKEN)