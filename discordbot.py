import discord
import rankmodule
import masterymodule
from discord.ext import commands
import youtube_dl
import random
import os
import wikipedia

version = input("stable, gez or gross?\n")
if version == "stable":
    build = "**"
    prefix = "$"
elif version == "gez":
    build = '**'
    prefix = "%"
elif version == "gross":
    build = '**'
    prefix = "@"

Try = discord.Client()
client = commands.Bot(command_prefix=prefix)
client.remove_command('help')
players = {}

@client.event
async def on_ready():
    print("The bot is online")
    await client.change_presence(activity=discord.Game(name="Flaming SoloQ - $help"))


@client.event
async def on_member_join(member):
    channel = client.get_channel(692336046876262464)
    x = str(member)
    await channel.send('Hi there ' f'{x.translate({ord(i): None for i in "#0123456789"})} & Welcome to the Shoe store !\nhere you can buy some good shoes or just play for fun !\nhave a good visit :smile:')

@client.command()
async def custom4(ctx, a1, b1, c1, d1, a2, b2, c2, d2):
     custom = []
     custom.append(a1), custom.append(b1), custom.append(c1), custom.append(d1), custom.append(a2), custom.append(b2), custom.append(c2), custom.append(d2)
     aa1=random.choice(custom)
     custom.remove(aa1)
     bb1 = random.choice(custom)
     custom.remove(bb1)
     cc1 = random.choice(custom)
     custom.remove(cc1)
     dd1 = random.choice(custom)
     custom.remove(dd1)
     aa2 = random.choice(custom)
     custom.remove(aa2)
     bb2 = random.choice(custom)
     custom.remove(bb2)
     cc2 = random.choice(custom)
     custom.remove(cc2)
     dd2 = random.choice(custom)
     custom.remove(dd2)
     await ctx.send('Team 1: '+aa1+' '+bb1+' '+cc1+' '+dd1+'\nTeam 2: '+aa2+' '+bb2+' '+cc2+' '+dd2)

@client.command()
async def custom5(ctx, a1, b1, c1, d1, e1, a2, b2, c2, d2, e2):
     custom = []
     custom.append(a1), custom.append(b1), custom.append(c1), custom.append(d1), custom.append(e1), custom.append(a2), custom.append(b2), custom.append(c2), custom.append(d2), custom.append(e2)
     aa1=random.choice(custom)
     custom.remove(aa1)
     bb1 = random.choice(custom)
     custom.remove(bb1)
     cc1 = random.choice(custom)
     custom.remove(cc1)
     dd1 = random.choice(custom)
     custom.remove(dd1)
     ee1 = random.choice(custom)
     custom.remove(ee1)
     aa2 = random.choice(custom)
     custom.remove(aa2)
     bb2 = random.choice(custom)
     custom.remove(bb2)
     cc2 = random.choice(custom)
     custom.remove(cc2)
     dd2 = random.choice(custom)
     custom.remove(dd2)
     ee2 = random.choice(custom)
     custom.remove(ee2)
     await ctx.send('Team 1: '+aa1+' '+bb1+' '+cc1+' '+dd1+' '+ee1+'\nTeam 2: '+aa2+' '+bb2+' '+cc2+' '+dd2+' '+ee2)

@client.command()
async def ping(ctx):
    await ctx.send('pong')
    await ctx.send('yes, im working')

@client.command()
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        colour=discord.Colour.orange()
    )
    embed.add_field(name='$help', value='opens this window....', inline=False)
    embed.add_field(name='$ping', value='returns pong', inline=False)
    embed.add_field(name='$connect', value='makes the bot join your voice channel')
    embed.add_field(name='$disconnect', value='makes the bot disconnect the voice chat', inline=False)
    embed.add_field(name='$play (link)', value='plays youtube link in voice chat', inline=False)
    embed.add_field(name='$rank (summoner name)', value='checks the summoners solo queue rank', inline=False)
    embed.add_field(name='$mastery (summoner name)', value='checks the summoners total mastery score for all champions', inline=False)
    embed.add_field(name='$word', value='write a random word', inline=False)
    embed.add_field(name='$custom4(name1, name2, name3, name4, name5, name6, name7, name8)', value='randomizes 2 teams of 4', inline=False)
    embed.add_field(name='$custom5(name1, name2, name3, name4, name5, name6, name7, name8, name9, name10)', value='randomizes 2 teams of 5', inline=False)

    await author.send(embed=embed)


@client.command()
async def connect(ctx):
    channel = ctx.author.voice.channel
    await discord.VoiceChannel.connect(channel)
    await ctx.send('Connected!')


@client.command()
async def disconnect(ctx):
    await client.voice_clients[0].disconnect()
    await ctx.send('Disconnected!')
    song_there = os.path.isfile('song.mp3')
    if song_there:
        os.remove('song.mp3')
        print('deleted song')


@client.command()
async def word(ctx):
    wikipedia.set_lang('he')
    page = wikipedia.random(pages=1)
    await ctx.send(page)


@client.command()
async def play(ctx, url: str):
    song_there = os.path.isfile('song.mp3')
    try:
        if song_there:
            os.remove('song.mp3')
            print('deleted song')
    except PermissionError:
        print('trying to delete songfile but it is being used')
        await ctx.send('Music is playing')
        return
    await ctx.send("prepping the music")

    voice = client.voice_clients[0]

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print('downloading audio')
        ydl.download([url])
    for file in os.listdir('./'):
        if file.endswith('.mp3'):
            name = file
            print(f'Renamed File: {file}')
            os.rename(file, 'song.mp3')

    voice.play(discord.FFmpegPCMAudio('song.mp3'), after=lambda e: print(f'{name} has finished playing'))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.2

    nname = name.rsplit('-', 2)
    await ctx.send(f'Playing {nname}')
    print('Playing')


@client.command()
async def rank(ctx, name):
    if name == "gross":
        await ctx.send("you dont wanna know...")
    else:
        await ctx.send("your rank is " + rankmodule.rankcheck(name))


@client.command()
async def mastery(ctx, name):
    await ctx.send("your total mastery score is " + format(masterymodule.masterycheck(name)))


client.run(build)
