import discord
import os
import random
from math import ceil
from numpy import mean

from wolfram_scraper import result_from_WolframAlpha
from update_csv import team_elos, update_elos, print_leaderboard
from elo import elo_updt

client = discord.Client()



@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    """Function for text commands that require responses"""
    global help, team1, team2, team1_av, team2_av, team1_elos, team2_elos
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
    **$oscarpack** (RIP Bozo)\n \
    **$teams** to choose teams')

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

    elif message.content.startswith("$teams"):
        text = message.content[7:]
        texter = text.split(", ")
        if len(texter) == 1:
            texter = text.split(" ")
        len_text = len(texter)
        x = random.sample(texter, k = ceil(len_text/2))
        await message.channel.send(x)

    elif message.content.startswith("$game"):
        text = message.content[6:]
        text = text.split(", ")
        team1 = text[0].split(" ")
        team2 = text[1].split(" ")
        team1_elos, team2_elos = team_elos(team1, team2)
        team1_av, team2_av = mean(team1_elos), mean(team2_elos)
        await message.channel.send(f"Write $win 0 if team 0 {team1} wins or write $win 1 if team 1 {team2} wins")

    elif message.content.startswith("$win"):
        text = message.content[5:]
        try:
            if text == "0":
                print(elo_updt(team1_av, team2_av, 0))
                delta_1, delta_2 = elo_updt(team1_av, team2_av, 0)
                update_elos(team1, team2, delta_1, delta_2)
            else:
                delta_1, delta_2 = elo_updt(team1_av, team2_av, 1)
                update_elos(team2, team1, delta_2, delta_1)
        except:
            print("there isnt a game going on")
            await message.channel.send("there isnt a game going on")
        team1_av, team2_av = False, False

    elif message.content.startswith("$elos"):
        await message.channel.send(print_leaderboard())


with open('token.txt') as token:
    TOKEN = token.readlines()[0]

client.run(TOKEN)
