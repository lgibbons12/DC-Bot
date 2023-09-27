import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

@bot.command()
async def calculate(ctx, num1, operation, num2):
    a = int(num1)
    b = int(num2)

    if operation == "+":
        output = add(a, b)
    elif operation == "-":
        output = subtract(a, b)
    elif operation == "*":
        output = multiply(a, b)
    elif operation == "/":
        output = divide(a, b)
    else:
        await ctx.send("Invalid operation")
        return
    
    await ctx.send(output)








bot.run(TOKEN)
