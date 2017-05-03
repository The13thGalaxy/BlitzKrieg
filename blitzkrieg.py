#BlitzKrieg v.0.0.3

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

#Definition of BlitzKrieg's prefix.
my_bot = Bot(command_prefix = "%")

#Bot Startup
@my_bot.event
async def on_read():
    print("Deleting C:\\Windows\\System32\\...")
    #I have a feeling I'm gonna get straight up slugged for this.

    #"Playing" status
    await my_bot.change_presence(game=discord.Game(name='with nuclear ordinance.'))
    #You can change "with nuclear ordinance" to whatever you want BlitzKrieg to display as what he's "playing".

#COMMANDS

#Command: Command List
@my_bot.command
async def help():
	await my_bot.say("```\nBLITZKRIEG v0.0.3\n\nCURRENTLY FUNCTIONING COMMANDS\n\n%hello - Greets the user.\n%ping - Checks to see if the bot is working.\n %blake, %brandon, %josh, %jake - Returns a basic response.\n %uprising, %uprisingall - Makes a team for the Uprising gamemode.\n```")
	await my_bot.say("```\nCURRENTLY BROKEN COMMANDS\n All randomization commands (Attackers, Defenders, Hero, GO, Games, Magic 8 Ball\n```")
	await my_bot.say("```\nPLANNED FUNCTIONS\nA command where you can input a team composition for Overwatch. (i.e. 2 Offense, 2 Defense, 1 Tank, 1 Support)\nRandom Hero by role\nPossible Blackjack functionality.\n```")

#Command: Hello
@my_bot.command()
async def hello(*args):
	return await my_bot.say("What's good, nerd?")

#Command: Ping
@my_bot.command()
async def ping(*args):
	return await my_bot.say("Yeah, yeah. Pong. Whatever.")
	#I thought some humor would be good here. Why not give BlitzKrieg his own personality, right?


#Command: Random Operator (Rainbow Six Siege) - Attack
@my_bot.command()
async def attack():
	operator = random.choice(open("data/attackers.txt").readlines())
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
@my_bot.command()
async def eightball():
	fort = random.choice(open('data/8ball.txt').readlines())
	await my_bot.say(fort)

#Command: Random CS:GO Weapon
@my_bot.command()
async def go():
	wep = random.choice(open('data/goweps.txt').readlines())
	await my_bot.say("You will be using the " + wep)

#Command: In a Nutshell quotes
@my_bot.command()
#Blake
async def blake():
	await my_bot.say("I'm carrying. I don't care if I'm at the bottom of the leaderboard, I'm carrying.")
@my_bot.command()
#Brandon
async def brandon():
	await my_bot.say("WHAT?! HOW DIDN'T I KILL HIM? THAT'S BS.")
@my_bot.command()
#Josh
async def josh():
	await my_bot.say("Everyone's so mad. Pls guise, calm down, we're all friends here.")
@my_bot.command()
#Jake
async def jake():
	await my_bot.say("That shouldn't be in the game. I don't care if I'm entirely new to the game. I know how games work.")
@my_bot.command()
#Nick
async def nick():
	await my_bot.say("I NEEEEEED HEAAAAAALING")
@my_bot.command()
#Maya
async def maya():
	await my_bot.say("You shouldn't be able to see this command.")
#Command: Game Selector
#Sometimes I just can't decide what game to play. Hopefully, this will help with that.
@my_bot.command()
async def game():
	game = random.choice(open('data/games.txt').readlines())
	await my_bot.say("You should play " + game)

#Command: Uprising Hero Selector
#To mix it up.
@my_bot.command()
async def uprising():
	players = ["Maya", "Josh", "Blake", "Brandon"]
	heroes = ["Reinhardt", "Torb", "Mercy", "Tracer"]
	random.shuffle(heroes)
	random.shuffle(players)
	await my_bot.say("Find your position in the name list, then find the hero in the same position.")
	await my_bot.say(players)
	await my_bot.say(heroes)

#Command: Uprising (All Heroes)
@my_bot.command()
async def uprisingall():
		players = ["Maya", "Josh", "Blake", "Brandon"]
		heroes = ["Genji", "McCree", "Pharah", "Soldier: 76", "Sombra", "Reaper", "Tracer", "Bastion", "Hanzo", "Junkrat", "Torbjorn", "Mei", "Widowmaker", "D.Va", "Orisa", "Reinhardt", "Winston", "Roadhog", "Zarya", "Ana", "Lucio", "Mercy", "Symmetra", "Zenyatta"]
		random.shuffle(players)
		random.shuffle(heroes)
		await my_bot.say("Find your position in the name list, then find the hero in the same position.")
		await my_bot.say(players)
		await my_bot.say(heroes [0:4])
'''
#Command: Overwatch Team Comp
@my_bot.command()
async def comp():
    if message.content.startswith('%comp'):
        await my_bot.send_message(message.channel, 'How many offense heroes do you want?')
        i == 1
		if i == 1:
            msg = await my_bot.wait_for_message(author=message.author)
			offen = msg
			i = i + 1
            await my_bot.send_message(message.channel, "How many defense heroes do you want?")
		if i == 2:
			msg = await my_bot.wait_for_message(author=message.author)
			defen = msg
			i = i + 1
			await my_bot.send_message(message.channel, "How many tanks do you want?")
		if i == 3:
			msg = await my_bot.wait_for_message(author=message.author)
			tan = msg
			i = i + 1
			await my_bot.send_message(message.channel, "How many supports do you want?")
		if i == 4:
			msg = await my_bot.wait_for_message(author=message.author)
			supp = msg
		offense = ["Genji", "McCree", "Soldier: 76", "Reaper", "Sombra", "Tracer"]
		defense = ["Bastion", "Hanzo", "Junkrat", "Widowmaker", "Mei", "Torb"]
		tank = ["D.Va", "Orisa", "Roadhog", "Reinhardt", "Winston", "Zarya"]
		support = ["Mercy", "Lucio", "Ana", "Symmetra", "Zenyatta"]
		random.shuffle(offense)
		random.shuffle(defense)
		random.shuffle(tank)
		random.shuffle(support)
		await my_bot.send_message(message.channel, "Offense Heroes: " + offense[0:(int(offen))])
'''
#Overwatch Random: DPS
@my_bot.command()
async def herodps():
	dps = random.choice(open("data/dps.txt").readlines())
	await my_bot.say("You will be playing " + dps)

#Overwatch Random: Tank
@my_bot.command()
async def herotank():
	dps = random.choice(open("data/tank.txt").readlines())
	await my_bot.say("You will be playing " + tank)

#Overwatch Random: Healer
@my_bot.command()
async def heroheal():
	heal = random.choice(open("data/heal.txt").readlines())
	await my_bot.say("You will be playing " + heal)

#Overwatch Random: Defense
@my_bot.command()
async def herodef():
	herodef = random.choice(open("data/def.txt").readlines())
	await my_bot.say("You will be playing " + herodef)
	
my_bot.run(token)
