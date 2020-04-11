import discord
import rankmodule
import masterymodule
from discord.ext import commands
import youtube_dl
import os
import wikipedia

version = input("stable, gez or gross?\n")
if version == "stable":
    build = "Njk2Nzk4MTQ1MzM3NzUzNzEx.Xo9vCg.I7mgdkaSudLrYGzAXj1SDFTmnUw"
    prefix = "$"
elif version == "gez":
    build = 'Njk2NzY4ODc3OTQxNjIwODE3.Xo9zSA.9hWVS3hS2H2psOnt_GgvB1r0MuY'
    prefix = "%"
elif version == "gross":
    build = 'Njk3Nzk2ODQzMDM1Mjk1ODI0.Xo9NPA.VWcIbRAIfgCGcR_LxloAEbaLamA'
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
    general = client.get_channel(692336046876262465)
    x = str(member)
    await general.send('Hi there ' f'{x.translate({ord(i): None for i in "#123456789"})} & Welcome to the Shoe store !\nhere you can buy some good shoes or just play for fun !\nhave a good visit :smile:')


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
    embed.add_field(name='$play', value='plays youtube link in voice chat', inline=False)
    embed.add_field(name='$rank', value='checks the summoners solo queue rank', inline=False)
    embed.add_field(name='$mastery', value='checks the summoners total mastery score for all champions', inline=False)
    embed.add_field(name='$word', value='write a random word', inline=False)

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