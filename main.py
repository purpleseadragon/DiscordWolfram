import discord
import os
import random

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

    elif message.content.startswith('$hello'):
        await message.channel.send('Hello!')

with open('token.txt') as token:
    TOKEN = token.readlines()[0]

meme_location = 'D:\meme_folder'

client.run(TOKEN)

print('hellow word')