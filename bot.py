from discord.ext import commands
import random
from math import ceil

bot = commands.Bot(command_prefix='!!')

@bot.command(name="character", help="Get a Cyberpunk 2020 character idea.")
async def idea(ctx):
    roles = ['Rocker', 'Tech', 'Medtech', 'Netrunner', 'Solo', 'Fixer', 'Nomad', 'Corporate', 'Cop']
    personalities = ['shy and secretive', 'rebellious, antisocial, and violent', 'arrogant, proud, and aloof', 'moody, rash, and headstrong', 'picky, fussy, and nervous', 'stable and serious', 'silly and fluffheaded', 'sneaky and deceptive', 'intellectual and detatched', 'friendly and outgoing']
    alliances = ['themself', 'a corporation', 'justice', 'money', 'power', 'fame', 'revenge', 'someone they love']
    idea = f"A {random.choice(roles)} who is {random.choice(personalities)} and lives for {random.choice(alliances)}."
    await ctx.send(idea)

@bot.command(name="printchar", help="Print a Cyberpunk 2020 character. Include name and stats, with spaces between. Spaces in name should be replaced with underscores.")
async def printchar(ctx, name: str, INT: int, REF: int, TECH: int, COOL: int, ATTR: int, LUCK: int, MA: int, BODY: int, EMP: int):
    name_list = name.split('_')
    
    # add name to str
    stat_str = "```"
    for name_part in name_list:
        stat_str += name_part + ' '
    stat_str += '\n'

    # add stats to str
    stat_str += f"INT [{INT}] REF [{REF}] TECH [{TECH}] COOL [{COOL}] ATTR [{ATTR}]\nLUCK [{LUCK}] MA [{MA}] BODY [{BODY}] EMP [{EMP}]\n"

    # get BTM
    BTM = 0
    if (BODY > 2 and BODY <= 4):
        BTM = -1
    elif (BODY <= 7):
        BTM = -2
    elif (BODY <= 9):
        BTM = -3
    elif (BODY == 10):
        BTM = -4
    else:
        BTM = -5
    
    # derived stats
    stat_str += f"Humanity [{EMP * 10}]\nRun [{MA * 3}m] Leap [{(MA * 3) / 4}m]\nLift [{BODY * 40}kgs] Carry [{BODY * 10}kgs]\nSAVE [{BODY}] BTM [{BTM}]"

    # gear - use this? https://stackoverflow.com/questions/62377883/how-can-i-get-user-input-in-a-python-discord-bot
    stat_str += '```'
    await ctx.send(stat_str)

@bot.command(name="printchar_red", help="Print a Cyberpunk Red character. Include name and stats, with spaces between. Spaces in name should be replaced with underscores.")
async def printchar_red(ctx, name: str, INT: int, REF: int, DEX: int, TECH: int, COOL: int, WILL: int, LUCK: int, MOVE: int, BODY: int, EMP: int):
    name_list = name.split('_')
    
    # add name to str
    stat_str = "```"
    for name_part in name_list:
        stat_str += name_part + ' '
    stat_str += '\n'

    # add stats to str 
    stat_str += f"INT [{INT}] REF [{REF}] DEX [{DEX}] TECH [{TECH}] COOL [{COOL}]\nWILL [{WILL}] LUCK [{LUCK}] MOVE [{MOVE}] BODY [{BODY}] EMP [{EMP}]\n"
    
    # derived stats
    hp = 10 + (5 * ceil((BODY + WILL) / 2))
    stat_str += f"HP [{hp}] Humanity [{EMP * 10}]"

    # gear

    stat_str += '```'
    await ctx.send(stat_str)


with open("BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    bot.run(TOKEN)