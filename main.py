import discord
from discord.ext import commands
from replit import db

#Host this bot on replit for optimal execution

'''pls enter the words to be blacklisted in the list below'''
filt = ["PLS ENTER ALL THE WORDS TO BE BLACKLISTED HERE!!!!!!!"]
bot = commands.Bot(command_prefix = ">>>")
Channel_IDS = []
db["Channels"]
Channel_IDS = db["Channels"] 
@bot.event
async def on_ready():
  print("logged in as "+str(bot.user))

@bot.event  
async def on_guild_channel_create(channel):
  #channel = discord.utils.get(channel.guild.channels, name='channel name')
  if channel.name == "global-chat":
    id = channel.id
    Channel_IDS.append(id)
    await channel.send("successfully set <#"+str(id)+"> as global chat")
  id = channel.id
  print (Channel_IDS)

@bot.event
async def on_guild_channel_delete(channel):
  if channel.id in Channel_IDS:
    Channel_IDS.remove(channel.id)
  print(Channel_IDS)
@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
    print("bot msg")
  else:
    if message.channel.id in Channel_IDS:
      print("message received"+str(message.content))
      for chann in Channel_IDS:
        if chann == message.channel.id or filt in message.content or "@everyone" in message.content or "@here" in message.content:
          continue
        await bot.get_channel(chann).send("**"+str(message.author)+"**  :globe_with_meridians: " + str(message.content))
        print("message sent" +str(message.content))

db["Channels"] = Channel_IDS
bot.run("Token")
