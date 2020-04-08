import discord
import rankmodule
import masterymodule
from discord.ext import commands
import youtube_dl
import os

client = discord.Client()

client = commands.Bot(command_prefix='$')

players = {}


@client.event
async def on_ready():
    print("The bot is online")
    await client.change_presence(activity=discord.Game(name="Flaming SoloQ"))


@client.command()
async def ping(ctx):
    await ctx.send('pong')


@client.command()
async def connect(ctx):
    channel = ctx.author.voice.channel
    await discord.VoiceChannel.connect(channel)
    await ctx.send('Connected!')


@client.command()
async def disconnect(ctx):
    await client.voice_clients[0].disconnect()
    await ctx.send('Disconnected!')


@client.command()
async def anthem(ctx):
    await ctx.send('!play https://www.youtube.com/watch?v=X3wBsZfHRy4&t=3s')


@client.command()
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()


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
