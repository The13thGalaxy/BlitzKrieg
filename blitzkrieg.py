#BLITZKRIEG v.0.0.1
#Imports and Bot Command definition
import asyncio
import discord
import logging
import math
import os
import random
import sys
from discord import utils
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
logging.basicConfig(level=logging.INFO)

#Definition of "%"
my_bot=Bot(command_prefix="%")

#Bot Startup
@my_bot.event
async def on_read():
    print("Deleting System32....")
    #I have a feeling I'm gonna get straight up slugged for this.

#Command: Hello
@my_bot.command()
async def hello(*args):
    return await my_bot.say("What do you want?")

#Command: Ping
@my_bot.command()
async def ping(*args):
	return await my_boy.say("I'm not saying it.")
	#I thought some humor would be good here. Why not give BlitzKrieg his own personality, right?
	
#Command: Random Operator (Rainbow Six Siege) - Attack
@my_bot.command()
async def attack():
	op = random.randint(1,76)
	infile = open("attackers.txt", "r")
	line = infile.readline()
	c = 1
	while c != op:
		c = c + 1
		line = infile.readline()
	if c == op:
		operator = line
		await my_bot.say("You will be playing " + operator)
	infile.close()

#TODO: Run tests of the written code tonight (4/7). Debug as needed.
my_bot.run("Mjk5NTQ4Mjc2ODEyOTM5MjY2.C8fnWg.WAmImA3L8NufHkCJykCNtyTIdyc")