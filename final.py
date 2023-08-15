import discord 
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="~", intents=intents)

command_list = ['ping', 'pong', 'helper']
help_list = ['Sends pong', 'Sends ping', 'sends help']

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith(bot.command_prefix):
        #~ping 3
        command = message.content[len(bot.command_prefix):]
        #ping 3
        command = command.split(" ")[0]
        #ping

        if command in command_list:
            pass
        else:
            await message.channel.send("Not a valid input")
            await message.channel.send("Valid Inputs: ")

            for command in command_list:
                await message.channel.send(f"- {command}")
        
        await bot.process_commands(message)

@bot.command()
async def helper(ctx, command):
    if command not in command_list:
        await ctx.send("Not a valid command")
        return
    
    idx = command_list.index(command)

    await ctx.send(f"The command {command}: {help_list[idx]}")


@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def pong(ctx):
    await ctx.send("ping")


bot.run(TOKEN)