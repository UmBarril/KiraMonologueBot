import discord
from queue import Queue
import asyncio 

client = discord.Client()

discord.Intents.members = True

@client.event
async def on_ready():
    print('Onou funcionou :O\nEntrei como {0.user}'.format(client))

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return
    
    # await message.channel.send(message.guild.id) -> 435827920267771905 
    monologepart1 = "My name is Yoshikage Kira. I'm 33 years old. My house is in the northeast section of Morioh, where all the villas are, and I am not married. I work as an employee for the Kame Yu department stores, and I get home every day by 8 PM at the latest. I don’t smoke, but I occasionally drink. I’m in bed by 11 PM, and make sure I get eight hours of sleep, no matter what. After having a glass of warm milk and doing about twenty minutes of stretches before going to bed, I usually have no problems sleeping until morning. Just like a baby, I wake up without any fatigue or stress in the morning."
    monologepart2 = "\nI was told there were no issues at my last check-up. I’m trying to explain that I’m a person who wishes to live a very quiet life. I take care not to trouble myself with any enemies, like winning and losing, that would cause me to lose sleep at night. That is how I deal with society, and I know that is what brings me happiness. Although, if I were to fight I wouldn’t lose to anyone."

    monologebrpart1 = "Meu nome é Yoshikage Kira. Tenho 33 anos. Minha casa fica na parte nordeste de Morioh, onde todas as moradias são, e eu não sou casado. Eu trabalho como funcionário das lojas de departamento Kame Yu, e chego em casa todos os dias às oito da noite, no máximo. Eu não fumo, mas ocasionalmente bebo. Estou na cama às 23h e me certifico de ter oito horas de sono, não importa o que aconteça. Depois de tomar um copo de leite morno e fazer cerca de vinte minutos de alongamentos antes de ir para a cama, geralmente não tenho problemas para dormir até de manhã. Assim como um bebê, eu acordo sem qualquer fadiga ou estresse pela manhã."
    monologebrpart2 = "\nFoi-me dito que não houve problemas no meu último check-up. Estou tentando explicar que sou uma pessoa que deseja viver uma vida muito tranquila. Eu cuido para não me incomodar com quaisquer inimigos, como ganhar e perder, que me faria perder o sono à noite. É assim que eu lido com a sociedade e sei que é isso que me traz felicidade. Embora, se eu fosse lutar, não perderia para ninguém."

    yaoinow = "https://tenor.com/view/katsuki-bakugo-katsuki-bakugo-bakugou-my-hero-academia-gif-16800168"

    if message.content.startswith('$kiraquinbr'): # bits the dust
        await message.channel.send(monologebrpart1 + monologebrpart2)
    elif message.content.startswith('$kiraquin'): # bits the dust
        await message.channel.send(monologepart1 + monologepart2)
    elif message.content.startswith('$yaoinow'): # bits the dust
        await message.channel.send(yaoinow)
    
with open('key.txt', 'r') as f:
    key = f.read()
    client.run(key)
    