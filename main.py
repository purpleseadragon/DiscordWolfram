import discord
import os
import random

from wolfram_scraper import *

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('$meme'):
        # uploads random meme from folder
        random_meme=random.choice(os.listdir("D:\meme_folder"))
        await message.channel.send(file=discord.File(f'D:\meme_folder\{random_meme}'))

    elif message.content.startswith('$wolf '):
        rest_of_message = message.content[6:]
        await message.channel.send(rest_of_message)

    elif message.content.startswith('$hello'):
        await message.channel.send('Hello!')

with open('token.txt') as token:
    TOKEN = token.readlines()[0]

client.run(TOKEN)

print('hellow word')