from discord.ext import commands
import random

bot = commands.Bot(command_prefix='!!')

@bot.command(name="character", help="Get a Cyberpunk 2020 character idea.")
async def idea(ctx):
    await ctx.send("You want a new character?")
    roles = ['Rocker', 'Tech', 'Medtech', 'Netrunner', 'Solo', 'Fixer', 'Nomad', 'Corporate', 'Cop']
    personalities = ['shy and secretive', 'rebellious, antisocial, and violent', 'arrogant, proud, and aloof', 'moody, rash, and headstrong', 'picky, fussy, and nervous', 'stable and serious', 'silly and fluffheaded', 'sneaky and deceptive', 'intellectual and detatched', 'friendly and outgoing']
    alliances = ['themself', 'a corporation', 'justice', 'money', 'power', 'fame', 'revenge', 'someone they love']
    idea = f"How about a {random.choice(roles)} who is {random.choice(personalities)} and lives for {random.choice(alliances)}?"
    await ctx.send(idea)

@bot.command(name="calc", help="Basic calculator supporting +, -, *, /, and **.")
async def calc(ctx, x: float, fn: str, y: float):
    if fn == '+':
        await ctx.send(f"{x} + {y} = {x + y}")
    elif fn == '-':
        await ctx.send(f"{x} - {y} = {x - y}")
    elif fn == '*':
        await ctx.send(f"{x} * {y} = {x * y}")
    elif fn == '/':
        await ctx.send(f"{x} / {y} = {x / y}")
    elif fn == '**':
        await ctx.send(f"{x} ** {y} = {x ** y}")
    else:
        await ctx.send("Only four functions available, + - * /")

with open("BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    bot.run(TOKEN)