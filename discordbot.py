$ heroku buildpacks:set heroku/python
import discord
import rankmodule
import masterymodule
from discord.ext import commands

client = discord.Client()

client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
    print("The bot is online")


@client.command()
async def ping(ctx):
    await ctx.send('pong')


@client.command()
async def rank(ctx, name):
    await ctx.send("your rank is " + rankmodule.rankcheck(name))


@client.command()
async def mastery(ctx, name):
    await ctx.send("your total mastery score is " + format(masterymodule.masterycheck(name)))


client.run('Njk2NzY4ODc3OTQxNjIwODE3.Xotu7w.uWvk0oS-EdcKvYUaowXBjxzFwAE')
