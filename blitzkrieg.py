#BlitzKrieg v.0.0.1
#Copyright 2017 Maya Pharis

#GENERAL BOT STUFF

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
logging.basicConfig(level = logging.INFO)

#Definition of "%"
my_bot = Bot(command_prefix = "%")

#Bot Startup
@my_bot.event
async def on_read():
    print(r"Deleting C:\Windows\System32\...")
    #I have a feeling I'm gonna get straight up slugged for this.

#"Playing" game status
await client.change_presence(game=discord.Game(name='GAME NAME GOES HERE'))




#COMMANDS

#Command: Hello
@my_bot.command()
async def hello(*args):
	return await my_bot.say("Go away.")

#Command: Ping
@my_bot.command()
async def ping(*args):
	return await my_bot.say("Heck off.")
	#I thought some humor would be good here. Why not give BlitzKrieg his own personality, right?

#Command: Random Operator (Rainbow Six Siege) - Attack
@my_bot.command()
async def attack():
	operator = random.choice(open('data/attackers.txt').readlines())
	await my_bot.say("You will be playing " + operator)

#Command: Random Operator (Rainbow Six Siege) - Defense
@my_bot.command()
async def defense():
	operator = random.choice(open('data/defenders.txt').readlines())
	await my_bot.say("You will be playing " + operator)

#Command: Random Hero (Overwatch)
@my_bot.command()
async def hero():
	herochoice = random.choice(open('data/heroes.txt').readlines())
	await my_bot.say("You will be playing " + herochoice)

#Command: Magic 8-Ball
@my_bot.command
async def eightball():
	fort = random.choice(open('data/heroes.txt').readlines())
	await my_bot.say(fort)

#Command: Random CS:GO Weapon
@my_bot.command
async def go():
	wep = random.choice(open('data/goweps.txt').readlines())
	await my_bot.say("You will be using the " + wep)

#Command: In a Nutshell quotes
@my_bot.command
#Blake
async def blake():
	await my_bot.say("I'm carrying. I don't care if I'm at the bottom of the leaderboard, I'm carrying.")
@my_bot.command
#Brandon
async def brandon():
	await my_bot.say("WHAT?! HOW DIDN'T I KILL HIM? THAT'S BS.")
@my_bot.command
#Josh
async def josh():
	await my_bot.say("Everyone's so mad. Pls guise, calm down, we're all friends here.")
@my_bot.command
#Jake
async def jake():
	await my_bot.say("That shouldn't be in the game. I don't care if I'm entirely new to the game. I know how games work.")
@my_bot.command
#Nick
async def nick():
	await my_bot.say("(angry silence as Reaper is selected)")
	

my_bot.run(token)
