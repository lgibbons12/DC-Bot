import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# List of example commands
command_list = ['ping', 'pong', 'helper']
help_list = ['sends pong', 'sends ping', 'sends help']

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith(bot.command_prefix):
        command = message.content[len(bot.command_prefix):].split(' ')[0]

        if command not in command_list:
            
            await message.channel.send("Not a valid input")
            await message.channel.send("Valid Inputs: ")
            for command in command_list:
                await message.channel.send(f"- {command}")
        
        await bot.process_commands(message)


@bot.command()
async def helper(ctx, arg):
    if arg not in command_list:
        await ctx.send("Not a valid command")
        return
    
    idx = command_list.index(arg)

    await ctx.send(f"The command {arg}: {help_list[idx]}")



@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def pong(ctx):
    await ctx.send("Ping!")

bot.run(TOKEN)
