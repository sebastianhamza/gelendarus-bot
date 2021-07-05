import discord
import os
import requests
import json
import random
from discord.ext import commands
from keep_alive import keep_alive

#client = discord.Client()

bot = commands.Bot(command_prefix= '>')



@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Game(name="Use >info for commands"))
  print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def info(ctx):
    embedVar = discord.Embed(title="Commands", description="", color=0x00ff00)
    embedVar.add_field(name="dictionary", value="Provides the definition of the argument", inline=False)
    embedVar.add_field(name="meme", value="Posts a meme", inline=False)
    await ctx.send(embed=embedVar)

@bot.command()    
async def dictionary(ctx, arg):
    await ctx.send(get_dictionary(arg))

@bot.command()    
async def meme(ctx):
    await ctx.send(get_meme())



def get_dictionary(word):
  response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en_US/{}".format(word))
  json_data = json.loads(response.text)
  meaning = json_data[0]['meanings'][0]['definitions'][0]['definition']
  return(meaning)

def get_joke():
  response = requests.get("https://v2.jokeapi.dev/joke/Any")
  json_data = json.loads(response.text)
  if(json_data['type']=='twopart'):
    joke = json_data['setup'] + json_data['delivery']
  else:
    joke = json_data['joke']
  return(joke)

def get_meme():
  response = requests.get("https://meme-api.herokuapp.com/gimme")
  json_data = json.loads(response.text)
  arr = json_data['preview']
  image = arr[len(arr)-1]
  return image

def get_meme_dark():
  response = requests.get("https://meme-api.herokuapp.com/gimme/torridmemes")
  json_data = json.loads(response.text)
  arr = json_data['preview']
  image = arr[len(arr)-1]
  return image

def get_dog():
  response = requests.get("https://dog.ceo/api/breeds/image/random")
  json_data = json.loads(response.text)
  image = json_data['message']
  return image

def roll_dice():
  number = random.randint(1, 6)
  return number

# @client.event
# async def on_message(message):
#   if message.author == client.user:
#     return
  
#   if message.content.startswith('>joke'):
#     joke = get_joke()
#     await message.channel.send(joke, tts='true')
  
#   if message.content.startswith('>dog'):
#     image = get_dog()
#     await message.channel.send(image)

#   if message.content.startswith('>meme'):
#     image = get_meme()
#     await message.channel.send(image)

#   if message.content.startswith('>dark'):
#     image = get_meme_dark()
#     await message.channel.send(image)

#   if message.content.startswith('>dice'):
#     dice = roll_dice()
#     await message.channel.send(dice)

#   if message.content.startswith('>help'):
#     await message.channel.send(">meme, >dark, >dice")



keep_alive()

bot.run(os.getenv('TOKEN'))