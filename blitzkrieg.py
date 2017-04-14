#BlitzKrieg v.0.0.1
#Copyright 2017 Maya Pharis

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

#Command: Hello
@my_bot.command()
async def hello(*args):
    return await my_bot.say("What do you want?")

#Command: Ping
@my_bot.command()
async def ping(*args):
	return await my_bot.say("Leave me alone, nerd.")
	#I thought some humor would be good here. Why not give BlitzKrieg his own personality, right?

#Command: Random Operator (Rainbow Six Siege) - Attack
@my_bot.command()
async def attack():
	op = random.randint(1, 84)
	infile = open("data/attackers.txt", "r")
	line = infile.readline()
	c = 1
	while c != op:
		c = c + 1
		line = infile.readline()
	if c == op:
		operator = line
		await my_bot.say("You will be playing " + operator)
	infile.close()

#Command: Random Operator (Rainbow Six Siege) - Defense
@my_bot.command()
async def defense():
	op = random.randint(1,76)
	infile = open("data/defenders.txt", "r")
	line = infile.readline()
	c = 1
	while c != op:
		c = c + 1
		line = infile.readline()
	if c == op:
		operator = line
		await my_bot.say("You will be playing " + operator)
	infile.close()
	#There must be a more efficent way to randomly select an operator..God knows I'm too lazy too find it, though.

#Command: Random Hero (Overwatch)
@my_bot.command()
async def hero():
	hero = random.randint(1,25)
	infile = open("data/heroes.txt", "r")
	line = infile.readline()
	c = 1
	while c != hero:
		c = c +1
		line = infile.readline()
	if c == hero:
		herochoice = line
		await my_bot.say("You will be playing " + herochoice)
	infile.close

#Command: Magic 8-Ball
@my_bot.command
async def 8ball():
	fortune = random.randint(1,21)
	infile = open("data/8ball.txt", "r")
	line = infile.readline()
	c = 1
	while c != fortune:
		c = c + 1
		line = infile.readline()
	if c == fortune:
		fort = line
		await my_bot.say(fort)
	infile.close

#Command: Random CS:GO Weapon
@my_bot.command
async def go():
	weapon = random.randint(1,23)
	infile = open("data/goweps.txt", "r")
	c = 1
	while c != weapon:
		c = c + 1
		line = infile.readline()
	if c == line:
		wep = weapon
		await my_bot.say("You will be using the " + wep)
	infile.close

#TODO: I should probably install TeamViewer at home. Maybe I can mess with it directly from school.
my_bot.run(token)
