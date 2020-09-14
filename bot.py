# bot.py
import os
import random
import rolador

import discord
#from dotenv import load_dotenv

#load_dotenv()
TOKEN = 'NzU0NDc1OTk4NTk0MjAzNzMy.X11Shw.r4bVHptMlHU7jeiLTqS57EsIgMQ'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!d'):
        resposta = rolador.interpretadorDado(message.content.split(" "))
        await message.channel.send(resposta)

client.run(TOKEN)


