import discord
import rankmodule
import masterymodule
from discord.ext import commands
import os

client = discord.Client()

client = commands.Bot(command_prefix='$')
game = discord.Game('Flaming Gross')

@client.event
async def on_ready():
    print("The bot is online")
    await client.change_presence(activity=discord.custonActivity(game))

@client.command()
async def ping(ctx):
    await ctx.send('pong')


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
