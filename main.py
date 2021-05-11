import discord
import os
import requests
import json
import random

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

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

def get_dog():
  response = requests.get("https://dog.ceo/api/breeds/image/random")
  json_data = json.loads(response.text)
  image = json_data['message']
  return image

def roll_dice():
  number = random.randint(1, 6)
  return number

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('>joke'):
    joke = get_joke()
    await message.channel.send(joke, tts='true')
  
  if message.content.startswith('>dog'):
    image = get_dog()
    await message.channel.send(image)

  if message.content.startswith('>meme'):
    image = get_meme()
    await message.channel.send(image)

  if message.content.startswith('>dice'):
    dice = roll_dice()
    await message.channel.send(dice)



client.run(os.getenv('TOKEN'))