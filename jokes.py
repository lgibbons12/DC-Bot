#imports
import discord
from dotenv import load_dotenv
from discord.ext import commands

import os
import requests
import json


#get token
load_dotenv()
TOKEN = os.getenv("TOKEN")

#create our bot
intents = discord.Intents.default()
intents.message_content = True

prefix = "*"

bot = commands.Bot(command_prefix=commands.when_mentioned_or(prefix), intents=intents)

@bot.event
async def on_message(message):
    print("okay")
    print(bot.user)
    if bot.user.mentioned_in(message):

        await message.channel.send("You can type `!vx help` for more info")

#create our button
class JokeCaller(discord.ui.View):
    async def disable_all_items(self):
        for item in self.children:
            item.disabled = True
        
        await self.message.edit(view=self)
        

    async def on_timeout(self) -> None:
        await self.message.channel.send("Timeout")
        await self.disable_all_items()
    
    #joke variable
    joke = None

    @discord.ui.button(label="Get Joke", style=discord.ButtonStyle.success)
    async def joke_get(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Grabbing joke . . .")

        joke_response = requests.get(
            "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&format=txt&type=single"
            )
        joke = joke_response.text

        with open("jokes.json", "r") as f:
            data = json.load(f)
        
        data['joke'] = joke

        with open("jokes.json", "w") as f:
            json.dump(data, f, indent=2)
        
        #super important!!!
        self.stop()

@bot.command()
async def joke(ctx):
    view = JokeCaller(timeout=30)
    message = await ctx.send("Click the button to get a joke!", view=view)

    view.message = message

    await view.wait()
    await view.disable_all_items()

    with open("jokes.json", "r") as f:
        data = json.load(f)

    await ctx.send("The joke is . . .")
    await ctx.send(data['joke'])


#without button
@bot.command()
async def no_button_joke(ctx):
    await ctx.send("Grabbing joke . . .")
    joke_response = requests.get(
        "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&format=txt&type=single"
    )
    joke = joke_response.text
    await ctx.send("The joke is . . .")
    await ctx.send(joke)

@bot.command()
async def caller(ctx, arg: str):
    await ctx.send(f"You said: {arg}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)
bot.run(TOKEN)