import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('$georgiana'):
    await message.channel.send('Georgianaa_fr spune: hai noroc', tts=True)

client.run(os.getenv('TOKEN'))