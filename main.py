#imports
import discord
import os

#from imports
from keep_alive import keep_alive
from replit import db

#client
client = discord.Client()

#variables, follow directions
db["count"] = 1 #run code then delete this
db["lastCounter"] = None #run code then delete this
countingChannelID = 123 #replace 123 with your channel ID for counting
game = "the counting game!" #replace this with what you want the bot to be playing
token = 123 #replace 123 with your bot's token

#when ready
@client.event
async def on_ready():
  activity = discord.Game(name=game, type=3)
  await client.change_presence(status=discord.Status.online, activity=activity)
  print("We have now logged in as {0.user}.".format(client))

#message deletion
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  author = message.author
  msg = message.content
  msg.lower()
  channel = message.channel
  countingChannel = message.guild.get_channel(919664549983051838)

  if channel == countingChannel:
    count = db["count"]
    last = db["lastCounter"]
    if msg != count:
      await message.delete()
    elif author == last:
      await message.delete()
    else:
      db["lastCounter"] = message.author
      count = int(count)
      count += 1
      count = str(count)
      db["count"] = count
  
#run bot
keep_alive()
client.run(token)
