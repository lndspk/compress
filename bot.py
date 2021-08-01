import discord
from discord.ext import commands
import asyncio
import random
import uuid
import requests
import urllib.request
from pygifsicle import optimize
from pygifsicle import gifsicle

client = commands.Bot(command_prefix = '~')

@client.event
async def on_ready():
	print('on')

@client.command()
async def ping(ctx):
	await ctx.send(f'{round(client.latency * 1000)}ms')

@client.command()
async def compress(ctx):
	imgurl = ctx.message.content.split()[-1]
	r = requests.get(imgurl, stream=True)
	imageName = str(uuid.uuid4()) + '.gif'
	urllib.request.urlretrieve(imgurl, imageName)
	gifsicle(
		sources=[imageName],
		destination=imageName,
		optimize=True,
		colors=32,
		options=["--verbose", "--conserve-memory", "--lossy=80"]
	)
	channel = client.get_channel("channel id")
	await ctx.channel.send(file=discord.File(imageName))

client.run('token')
