import discord
from discord import Embed
import os
import affirmation
import plants
from replit import db

client = discord.Client()
embed = discord.Embed()
@client.event
async def on_ready():
  print("{0.user} is online!".format(client))

@client.event
async def on_message(msg):
  if msg.author == client.user:
    return
  if msg.content.startswith("ping"):
    await msg.channel.send("Test")
    embed.set_image(url='https://i.gyazo.com/11a97964253fcb7f535b78015e8e4f64.png')
    await client.say(embed=embed)
    
  if msg.content.startswith("/waterplant"):
    emoji = "\U00002764"
    await msg.add_reaction(emoji)
    quote = affirmation.random_quote()
    await msg.channel.send(quote)

  if msg.content.startswith("/test"):
    plant = plants.random_plant()
    await msg.channel.send(plant)

client.run(os.getenv("TOKEN"))