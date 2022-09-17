import discord
import os
import random

from wolfram_scraper import result_from_WolframAlpha

client = discord.Client()


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    """Function for text commands that require responses"""
    global help
    if message.author == client.user:
        return

    elif message.content.startswith('$meme'):
        # uploads random meme from folder
        random_meme=random.choice(os.listdir("D:\god_folder\meme_folder"))
        await message.channel.send(file=discord.File(f'D:\god_folder\meme_folder\{random_meme}'))
    
    elif message.content.startswith('$leadpipe'):
        random_meme=random.choice(os.listdir("D:\god_folder\lead_pipe"))
        await message.channel.send(file=discord.File(f'D:\god_folder\lead_pipe\{random_meme}'))

    elif message.content.startswith('$wolf '):
        rest_of_message = message.content[6:]
        try:
            await message.channel.send(result_from_WolframAlpha(rest_of_message))
        except StopIteration:
            await message.channel.send('That was not a valid query')

    elif message.content.startswith('$laplace'):
        await message.channel.send(file=discord.File(f'D:\god_folder\laplace\laplace_table.png'))

    elif message.content.startswith('$laplack'):
        await message.channel.send(file=discord.File(f'D:\god_folder\laplace\laplace_table2.png'))

    elif message.content.startswith('$help'):
        await message.channel.send('The bot currently recognises the following commands: \n \
    **$meme** will generate a random meme \n \
    **$wolf** followed by a query will return the answer given by wolfram alpha \n \
    **$hello** will cause the bot to reply with a greeting \n \
    **$leadpipe** will post a meme \n \
    **$help** will print this message.\n \
    **$laplace** and **$laplack** will give laplace transforms.\n\
     **$free** does something\n \
    **$oscarpack** (RIP Bozo)')

    elif message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    elif message.content.startswith('$free'):
        embed = discord.Embed(title="**Free Things**")
        embed.description = "[Click on this for free movies, trust me not sus](https://hdtoday.tv/home)" 
        await message.channel.send(embed=embed)
    elif message.content.startswith('@'):
        await message.add_reaction('🍤')

    elif message.content.startswith("$oscarpack"):
        await message.channel.send(file=discord.File(f'D:\god_folder\laplace\oscar1.jpg'))
        await message.channel.send(file=discord.File(f'D:\god_folder\laplace\oscar2.png'))


with open('token.txt') as token:
    TOKEN = token.readlines()[0]

client.run(TOKEN)
