#imports
import discord
from dotenv import load_dotenv
from discord.ext import commands
import os

#loading in the token
load_dotenv()
TOKEN = os.getenv("TOKEN")

#creating our bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)



class SimpleView(discord.ui.View):

    @discord.ui.button(label="Hello", style=discord.ButtonStyle.success)
    async def hello(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Hello world")
        




#calculations
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
        output = "Invalid sign, please try again"
    await ctx.send(output)


@bot.command()
async def button(ctx):
    #a = int(num1)
    #b = int(num2)

    view = SimpleView()
    
    await ctx.send(view=view)




bot.run(TOKEN)

