import discord
from dotenv import load_dotenv
from discord.ext import commands
import os
import requests


import json


load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)


class JokeCaller(discord.ui.View):
    
    async def disable_all_items(self):
        for item in self.children:
            item.disabled = True
        
        await self.message.edit(view=self)
        

    async def on_timeout(self) -> None:
        await self.message.channel.send("Timeout")
        await self.disable_all_items()
    joke = None

    @discord.ui.button(label="Get Joke", style=discord.ButtonStyle.success)
    async def divide(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Grabbing joke. . .")

        joke_response = requests.get(
            "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&format=txt&type=single"
        )
        joke = joke_response.text  # Use self.joke to set the class attribute

        with open("jokes.json", "r") as f:
            data = json.load(f)

        data["joke"] = joke  # Use self.joke to set the joke in the data dictionary

        with open('jokes.json', 'w') as f:
            json.dump(data, f, indent=2)

       
        self.stop()

    


@bot.command()
async def get_joke(ctx):
    view = JokeCaller(timeout=30)
    message = await ctx.send("Click the button to get a joke!", view=view)
    view.message = message
    
    await view.wait()
    await view.disable_all_items()
    
    
    with open("jokes.json", "r") as f:
        data = json.load(f)
    
    await ctx.send("The joke is . . .")
    await ctx.send(data["joke"])


bot.run(TOKEN)
