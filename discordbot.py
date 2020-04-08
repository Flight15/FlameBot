import discord
import rankmodule
import masterymodule
from discord.ext import commands
import youtube_dl
import os

client = discord.Client()

client = commands.Bot(command_prefix='$')
client.remove_command('help')
players = {}


@client.event
async def on_ready():
    print("The bot is online")
    await client.change_presence(activity=discord.Game(name="Flaming SoloQ"))


@client.command()
async def ping(ctx):
    await ctx.send('pong')
    await ctx.send('yes, im working')


@client.command()
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        colour = discord.Colour.orange()
    )
    embed.set_author(name='help')
    embed.add_field(name= '$ping', value= 'returns pong....', inline=False)
    embed.add_field(name= '$connect', value= 'makes the bot join your voice channel')
    embed.add_field(name= '$play', value= 'plays youtube link in voice chat', inline=False)
    embed.add_field(name= '$disconnect', value= 'makes the bot disconnect the voice chat', inline=False)
    embed.add_field(name= '$rank', value= 'checks the summoners solo queue rank', inline=False)
    embed.add_field(name= '$mastery', value= 'checks the summoners total mastery score for all champions', inline=False)

    await ctx.send(author, embed=embed)

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
async def anthem(ctx):
    await ctx.send('!play https://www.youtube.com/watch?v=X3wBsZfHRy4&t=3s')


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
    voice.source.volume = 0.07

    nname = name.rsplit('-', 2)
    await ctx.send(f'Playing {nname}')
    print('Playing')


@client.command()
async def liberate(ctx):
    await ctx.send("FREEDOM")
    await ctx.send("https://upload.wikimedia.org/wikipedia/commons/5/58/CheHigh.jpg")
    await ctx.send('https://media.dayoftheshirt.com/images/shirts/x2UWu/qwertee_for-the-horde_1535836347.large.png')
    await ctx.send('https://media.giphy.com/media/3DHUG0x7O14tQRfaIo/giphy.gif')
    await ctx.send('https://media.swncdn.com/via/6705-gettyimages-manopjk.jpg')
    await ctx.send('https://media.discordapp.net/attachments/477860330257645569/697021389022035968/images.png')


@client.command()
async def rank(ctx, name):
    if name == "gross":
        await ctx.send("you dont wanna know...")
    else:
        await ctx.send("your rank is " + rankmodule.rankcheck(name))


@client.command()
async def mastery(ctx, name):
    await ctx.send("your total mastery score is " + format(masterymodule.masterycheck(name)))


client.run('Njk2NzY4ODc3OTQxNjIwODE3.Xotu7w.uWvk0oS-EdcKvYUaowXBjxzFwAE')
