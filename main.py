import discord
import os
import requests
import json

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

def get_dog():
  response = requests.get("https://dog.ceo/api/breeds/image/random")
  json_data = json.loads(response.text)
  image = json_data['message']
  return image


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

client.run(os.getenv('TOKEN'))