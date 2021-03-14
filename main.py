import discord
import os
client = discord.Client()
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
a = 2000
b = 2000
@client.event
async def on_message(message):
  if message.author == client.user:
    return
@client.event
async def on_message(message):
  if message.author == client.user:
     return
  if message.content.startswith("n!help"):
    await message.channel.send("nuclear sabka baap h")
  if message.content.startswith("n!profile"):
    await message.channel.send("GHANTA KUCH NAHI UKHADA APNE PEHLI FURSAT MAIN NIKAL")
  if message.content.startswith("n!bal"):
    await message.channel.send("AUKAT DEKHI H APNI")
  
  if message.content.startswith("n!daily"):
    await message.channel.send("You got a Gem💎" + "AND 💸2000💸")
    
  
  if message.content.startswith("n!how is nuclear"):
    await message.channel.send("Nuclear is always OP")
  if message.content.startswith("n!inventory"):
    await message.channel.send(a + b)
     
  


  
 






  





client.run(token)