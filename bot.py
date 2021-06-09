import discord
from discord.ext import commands
import random
from math import ceil
import sqlite3

# gear - use this? https://stackoverflow.com/questions/62377883/how-can-i-get-user-input-in-a-python-discord-bot
connection = sqlite3.connect("characters.db")
print(connection.total_changes) # should be 0, for verifying purposes

cursor = connection.cursor()
# cursor.execute("DROP TABLE characters_2020")
# cursor.execute("DROP TABLE characters_red")
# cursor.execute("CREATE TABLE characters_2020 (client TEXT, handle TEXT, role TEXT, intelligence INTEGER, reflex INTEGER, tech INTEGER, cool INTEGER, attractiveness INTEGER, luck INTEGER, movement_allowance INTEGER, body INTEGER, empathy INTEGER)")
# cursor.execute("CREATE TABLE characters_red (client TEXT, handle TEXT, role TEXT, intelligence INTEGER, reflex INTEGER, dexterity INTEGER, tech INTEGER, cool INTEGER, will INTEGER, luck INTEGER, movement_allowance INTEGER, body INTEGER, empathy INTEGER)")

intents = discord.Intents().default()
intents.members = True

bot = commands.Bot(command_prefix='!!', intents = intents)


@bot.command(name="character", help="Get a Cyberpunk 2020 character idea.")
async def idea(ctx):
    roles = ['Rocker', 'Tech', 'Medtech', 'Netrunner', 'Solo', 'Fixer', 'Nomad', 'Corporate', 'Cop']
    personalities = ['shy and secretive', 'rebellious, antisocial, and violent', 'arrogant, proud, and aloof', 'moody, rash, and headstrong', 'picky, fussy, and nervous', 'stable and serious', 'silly and fluffheaded', 'sneaky and deceptive', 'intellectual and detatched', 'friendly and outgoing']
    motivations = ['themself', 'a corporation', 'justice', 'money', 'power', 'fame', 'revenge', 'someone they love']
    idea = f"A {random.choice(roles)} who is {random.choice(personalities)} whose motivation is {random.choice(motivations)}."
    await ctx.send(idea)


def format_handle(handle: str) -> str:
    handle_list = handle.split('_')
    to_return = ""
    for handle_part in handle_list:
        to_return += handle_part + ' '
    to_return = to_return.rstrip(' ')
    return to_return


@bot.command(name="make2020", help="Add a Cyberpunk 2020 character with the following fields: Character_Name Character_Role INT REF TECH COOL ATTR LUCK MA BODY EMP")
async def make2020(ctx, handle: str, role: str, INT: int, REF: int, TECH: int, COOL: int, ATTR: int, LUCK: int, MA: int, BODY: int, EMP: int):
    # stats remain as integers to ensure that people don't put words in instead
    handle = format_handle(handle)

    # set up strings
    INT = str(INT)
    REF = str(REF)
    TECH = str(TECH)
    COOL = str(COOL)
    ATTR = str(ATTR)
    LUCK = str(LUCK)
    MA = str(MA)
    BODY = str(BODY)
    EMP = str(EMP)
    
    cursor.execute("INSERT INTO characters_2020 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (str(bot.user.id), handle, role, INT, REF, TECH, COOL, ATTR, LUCK, MA, BODY, EMP,))
    await ctx.send("Character created! Printing stats...")
    character_str = stat_str_2020(handle)
    await ctx.send(character_str)


@bot.command(name="makered", help="Add a Cyberpunk Red character with the following fields: Character_Name Role INT REF DEX TECH COOL WILL LUCK MOVE BODY EMP")
async def printred(ctx, name: str, INT: int, REF: int, DEX: int, TECH: int, COOL: int, WILL: int, LUCK: int, MOVE: int, BODY: int, EMP: int):
    # stats remain as integers to ensure that people don't put words in instead
    handle = format_handle(handle)

    # set up strings
    INT = str(INT)
    REF = str(REF)
    DEX = str(DEX)
    TECH = str(TECH)
    COOL = str(COOL)
    WILL = str(WILL)
    LUCK = str(LUCK)
    MOVE = str(MOVE)
    BODY = str(BODY)
    EMP = str(EMP)
    
    cursor.execute("INSERT INTO characters_red VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (str(bot.user.id), handle, role, INT, REF, DEX, TECH, COOL, WILL, LUCK, MOVE, BODY, EMP,))
    await ctx.send("Character created! Printing stats...")
    character_str = print_red(handle)
    await ctx.send(character_str)


# helper function to make a stat block for a 2020 character in the database
def stat_str_2020(handle: str) -> str:
    id = bot.user.id
    retrieved = cursor.execute("SELECT * FROM characters_2020 WHERE client=? AND handle=?", (id,handle)).fetchall()
    character = retrieved[0] # the tuple
    
    role = character[2]
    INT = character[3]
    REF = character[4]
    TECH = character[5]
    COOL = character[6]
    ATTR = character[7]
    LUCK = character[8]
    MA = character[9]
    BODY = character[10]
    EMP = character[11]

    stat_str = f"```Handle: {handle}\nRole: {role}\n"
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
    stat_str += f"Humanity [{EMP * 10}]\nRun [{MA * 3}] Leap [{(MA * 3) / 4}]\nLift [{BODY * 40}] Carry [{BODY * 10}]\nSAVE [{BODY}] BTM [{BTM}]```"

    return stat_str


# helper function to make a stat block for a Red character in the database
def stat_str_red(handle: str) -> str:
    id = bot.user.id
    retrieved = cursor.execute("SELECT * FROM characters_red WHERE client=?", (id,)).fetchall()
    character = retrieved[0] # the tuple

    role = character[2]
    INT = character[3]
    REF = character[4]
    DEX = character[5]
    TECH = character[6]
    COOL = character[7]
    WILL = character[8]
    LUCK = character[9]
    MOVE = character[10]
    BODY = character[11]
    EMP = character[12]

    stat_str = f"```Handle: {handle}\nRole: {role}\n"
    stat_str += f"INT [{INT}] REF [{REF}] DEX [{DEX}] TECH [{TECH}] COOL [{COOL}]\nWILL [{WILL}] LUCK [{LUCK}] MOVE [{MOVE}] BODY [{BODY}] EMP [{EMP}]\n"
    
    hp = 10 + (5 * ceil((BODY + WILL) / 2))
    stat_str += f"HP [{hp}] Humanity [{EMP * 10}]```"

    return stat_str


@bot.command(name="print2020", help="Print a Cyberpunk 2020 character that has already been added using !!make2020. Add the name as a single word with underscores instead of spaces, like My_Character.")
async def print2020(ctx, handle: str):
    handle = format_handle(handle)
    character_str = stat_str_2020(handle)
    await ctx.send(character_str)


@bot.command(name="printred", help="Print a Cyberpunk Red character that has already been added using !!makered. Add the name as a single word with underscores instead of spaces, like My_Character.")
async def printred(ctx, handle: str, INT: int, REF: int, DEX: int, TECH: int, COOL: int, WILL: int, LUCK: int, MOVE: int, BODY: int, EMP: int):
    handle = format_handle(handle)
    character_str = stat_str_red(handle)
    await ctx.send(character_str)




with open("BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    bot.run(TOKEN)