"""SporkBot"""

import discord
import random
import time

random.seed(time.ctime)
client = discord.Client()


secret_key="stuff"
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('SporkBot'):
    parts=message.content.lower().split()
    if len(parts)==1:
        quote="Yes?"
    elif parts[1]=="shuffle":
        if len(parts)==2:
            quote="Shuffle what?"
        else:
            bits=parts[2:]
            random.shuffle(bits)
            quote=" ".join(bits)

    elif parts[1]=="choose":
        if len(parts)==2:
            quote="choose from what?"
        else:
            bits=parts[2:]
            random.shuffle(bits)
            quote=bits[0]
    elif parts[1]=="help":
        quote="""SporkBot. A fair and unbiased random outcome generator. Honestly.
SporkBot help: display this message.
SporkBot shuffle <item 1> <item 2> ... <item n>: return items in random order.
SporkBot choose <item 1> <item 2> ... <item n>: chose one of the items randomly.
SporkBot runcible cannon: DO NOT USE THIS OPTION UNDER ANY CIRCUMSTANCES!"""
    elif message.content.lower().startswith('sporkbot runcible cannon'):
        quote="Bombardment ordered. Enter command password to cancel."
    else:
        quote="I don't know how to "+" ".join(parts[1:])
    
    await message.channel.send(quote)
  else:
    return

client.run(secret_key)
