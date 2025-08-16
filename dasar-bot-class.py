# test-bot(bot class)
# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
import random
import requests
import os
from discord.ext import commands
from bot_logic import gen_pass 
from logic_poke import Pokemon
from model import get_class
description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
# command prefix 
bot = commands.Bot(command_prefix='$', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})') # type: ignore
    print('------')
# @bot.event # decorator to modify python function for even class
# async def on_message(msg):
#     balasans = [""
              
#         ]
#     balasan = random.choice(balasans)
#     if msg.author == bot.user:
#         return
#     elif msg.content == "$hello" or msg.content == "$pw" or msg.content == "$baca" or msg.content == "$dt" or msg.content == "$dog" or msg.content == "$duck" or msg.content == "$meme" or msg.content == "$coinflip" or msg.content == "$dice" or msg.content == "$load" or msg.content == "$reload" or msg.content == "$go" or msg.content == "$gemini" or msg.content == "$waktu" or msg.content == "$local_drive" or msg.content == "$deteksi" or msg.content == "$daun" or msg.content == "$simpan" or msg.content == "$local_drive" or msg.content == "$klasifikasi":
#         pass # reply for not command of bot
#     elif "$showfile" in msg.content.split() or "$dt" in msg.content.split() or "$showfile" in msg.content.split() or "$add" in msg.content.split() or "$min" in msg.content.split() or "$times" in msg.content.split() or "$div" in msg.content.split() or "$pow" in msg.content.split() or "$repeat" in msg.content.split() or "$baca" in msg.content.split() or "$tulis" in msg.content.split() or "$tambahkan" in msg.content.split() or "$analisis" in msg.content.split() or "$sentiment" in msg.content.split() or "$analysis" in msg.content.split() or "$deteksi" in msg.content.split() or "$klasifikasi" in msg.content.split() or "$daun" in msg.content.split() or "$tictactoe" in msg.content.split() or "$place" in msg.content.split() or "$help" in msg.content.split() or "/play" in msg.content.split() or "$map" in msg.content.split():
#         # Lakukan sesuatu jika ada dalam pesan
#         pass
#     elif "help" in msg.content.split() or "crowded" in msg.content.split() or "traffic" in msg.content.split() or "car":
#         await msg.channel.send(balasan)
#     await bot.process_commands(msg) #process_commands() at the end of your on_message. 
#     # This is because overriding the default on_message forbids commands from running.
# adding two numbers
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

# subtract two numbers
@bot.command()
async def min(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left - right)
    
# times two numbers
@bot.command()
async def times(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left * right)

    
# divide two numbers
@bot.command()
async def div(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left / right)

    
# exponet two numbers
@bot.command()
async def expo(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left ** right)

# spamming word
@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)
        
# password generator        
@bot.command()
async def pw(ctx):
    await ctx.send(f'Kata sandi yang dihasilkan: {gen_pass(10)}')

# coinflip
@bot.command()
async def coinflip(ctx):
    num = random.randint(1,2)
    if num == 1:
        await ctx.send('It is Head!')
    if num == 2:
        await ctx.send('It is Tail!')

# rolling dice
@bot.command()
async def dice(ctx):
    nums = random.randint(1,6)
    if nums == 1:
        await ctx.send('It is 1!')
    elif nums == 2:
        await ctx.send('It is 2!')
    elif nums == 3:
        await ctx.send('It is 3!')
    elif nums == 4:
        await ctx.send('It is 4!')
    elif nums == 5:
        await ctx.send('It is 5!')
    elif nums == 6:
        await ctx.send('It is 6!')

# @bot.command()
# async def mem(ctx):
#     # try by your self 2 min
#     img_name = random.choice(os.listdir('images'))
#     with open(f'images/{img_name}', 'rb') as f:
#         picture = discord.File(f)
 
#     await ctx.send(file=picture)
#overwriting kalimat.txt
@bot.command()
async def tulis(ctx, *, my_string: str):
    with open('kalimat.txt', 'w', encoding='utf-8') as t:
        text = ""
        text += my_string
        t.write(text)
# append kalimat.txt
@bot.command()
async def tambahkan(ctx, *, my_string: str):
    with open('kalimat.txt', 'a', encoding='utf-8') as t:
        text = "\n"
        text += my_string
        t.write(text)
# reading kalimat.txt
@bot.command()
async def baca(ctx):
    with open('kalimat.txt', 'r', encoding='utf-8') as t:
        document = t.read()
        await ctx.send(document)



# random local meme image
@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('meme'))
    with open(f'meme/{img_name}', 'rb') as f:
    # with open(f'meme/enemies-meme.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
    await ctx.send(file=picture)

# API to get random dog and duck image 
def get_dog_image_url():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('dog')
async def dog(ctx):
    '''Setiap kali permintaan dog (anjing) dipanggil, program memanggil fungsi get_dog_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)
def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('duck')
async def duck(ctx):
    '''Setiap kali permintaan duck (bebek) dipanggil, program memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

    # The '$go' command
@bot.command()
async def go(ctx):
    author = ctx.author.name  # Getting the name of the message's author
    # Check whether the user already has a Pokémon. If not, then...
    # if author not in Pokemon.pokemons.keys():
    pokemon = Pokemon(author)  # Creating a new Pokémon
    await ctx.send(await pokemon.info())  # Sending information about the Pokémon
    image_url = await pokemon.show_img()  # Getting the URL of the Pokémon image
    if image_url:
        embed = discord.Embed()  # Creating an embed message
        embed.set_image(url=image_url)  # Setting up the Pokémon's image
        await ctx.send(embed=embed)  # Sending an embedded message with an image
    else:
        await ctx.send("Failed to upload an image of the pokémon.")

#show local drive    
@bot.command()
async def local_drive(ctx):
    try:
      folder_path = "./files"  # Replace with the actual folder path
      files = os.listdir(folder_path)
      file_list = "\n".join(files)
      await ctx.send(f"Files in the folder:\n{file_list}")
    except FileNotFoundError:
      await ctx.send("Folder not found.") 
#show local file
@bot.command()
async def showfile(ctx, filename):
  """Sends a file as an attachment."""
  folder_path = "./files/"
  file_path = os.path.join(folder_path, filename)
  try:
    await ctx.send(file=discord.File(file_path))
  except FileNotFoundError:
    await ctx.send(f"File '{filename}' not found.")
# upload file to local computer
@bot.command()
async def simpan(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            # file_url = attachment.url  IF URL
            await attachment.save(f"./files/{file_name}")
            await ctx.send(f"Menyimpan {file_name}")
    else:
        await ctx.send("Anda lupa mengunggah :(")

# welcome message
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}') # type: ignore
    # provide what you can help here

#Computer Vision Classification 
@bot.command()
async def klasifikasi(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            #file_url = attachment.url IF URL
            await attachment.save(f"./CV/{file_name}")
            await ctx.send(get_class(model_path="keras_model.h5", labels_path="labels.txt", image_path=f"./CV/{file_name}"))
    else:
        await ctx.send("Anda lupa mengunggah gambar :(")

@bot.command()
async def pasta(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            #file_url = attachment.url IF URL
            await attachment.save(f"./CV/{file_name}")
            if get_class(model_path="keras_model3.h5", labels_path="labels3.txt", image_path=f"./CV/{file_name}")=="Amatriciana\n":
                await ctx.send("Pasta Amatriciana")
                await ctx.send("The main ingredients for Amatriciana sauce are guanciale (cured pork cheek), Pecorino Romano cheese, tomatoes, and often white wine, red pepper flakes, and olive oil. Sometimes onion, garlic, black pepper, and salt are also included. The sauce is typically served over bucatini or spaghetti.")
            elif get_class(model_path="keras_model3.h5", labels_path="labels3.txt", image_path=f"./CV/{file_name}")=="Carbonara\n":
                await ctx.send("Pasta Carbonara")
                await ctx.send("Classic Carbonara typically includes spaghetti, guanciale (or pancetta), eggs (including yolks), Pecorino Romano cheese, and black pepper. Some recipes may also include a bit of salt and olive oil.")
            elif get_class(model_path="keras_model3.h5", labels_path="labels3.txt", image_path=f"./CV/{file_name}")=="Pesto":
                await ctx.send("Pasta Pesto")
                await ctx.send("Classic pesto, also known as pesto genovese, typically includes fresh basil, pine nuts, garlic, Parmesan cheese, and olive oil. Some recipes also incorporate Pecorino Romano cheese for a sharper flavor.")
            elif get_class(model_path="keras_model3.h5", labels_path="labels3.txt", image_path=f"./CV/{file_name}")=="Frutti Di Mare\n":
                await ctx.send("Pasta Frutti Di Mare")
                await ctx.send("Frutti di Mare, which means 'fruits of the sea,' typically includes a variety of seafood such as shrimp, mussels, clams, squid, and sometimes fish. The sauce is often made with tomatoes, garlic, olive oil, white wine, and herbs like parsley or basil.")
            elif get_class(model_path="keras_model3.h5", labels_path="labels3.txt", image_path=f"./CV/{file_name}")=="Bolognese\n":
                await ctx.send("Pasta Bolognese")
                await ctx.send("Bolognese sauce, also known as ragù alla Bolognese, typically includes ground meat (beef or a mix of beef and pork), tomatoes, onions, carrots, celery, garlic, red wine, and herbs like bay leaves and thyme. It is often served with tagliatelle or pappardelle pasta.")
            elif get_class(model_path="keras_model3.h5", labels_path="labels3.txt", image_path=f"./CV/{file_name}")=="Spaghetti\n":
                await ctx.send("Pasta Spaghetti")
                await ctx.send("typically contains just a few basic ingredients: spaghetti noodles, water, and salt. The noodles are traditionally made from milled wheat (durum wheat semolina in Italy) and water, sometimes enriched with vitamins and minerals. Other common additions include olive oil, garlic, and tomato sauce, which are used in preparing the sauce that accompanies the pasta.")
            elif get_class(model_path="keras_model3.h5", labels_path="labels3.txt", image_path=f"./CV/{file_name}")=="Cacciatore\n":
                await ctx.send("Pasta Cacciatore")
                await ctx.send("Chicken cacciatore, also known as 'hunter's stew', typically includes chicken, onions, garlic, tomatoes, and herbs. Other common ingredients are mushrooms, bell peppers, and wine (either red or white). Some variations also include capers, olives, anchovies, carrots, or celery. The dish is often served with pasta, rice, or polenta.")
            elif get_class(model_path="keras_model3.h5", labels_path="labels3.txt", image_path=f"./CV/{file_name}")=="Vongole\n":
                await ctx.send("Pasta Vongole")
                await ctx.send("Spaghetti alle Vongole, a classic Italian pasta dish, features clams, pasta, olive oil, garlic, and parsley as key ingredients. Additional ingredients like white wine, chili flakes, lemon, and butter are often included to enhance the flavor profile.")
            elif get_class(model_path="keras_model3.h5", labels_path="labels3.txt", image_path=f"./CV/{file_name}")=="Marinara\n":
                await ctx.send("Pasta Marinara")
                await ctx.send("Marinara sauce typically includes tomatoes, garlic, olive oil, onions, and herbs like basil and oregano. Some recipes also include tomato paste, red pepper flakes, salt, and pepper. Sugar can be added to balance acidity.")
            else:
                await ctx.send("Tidak dapat mengklasifikasikan pasta tersebut.")
    else:
        await ctx.send("Anda lupa mengunggah gambar :(")

# map
@bot.command()
async def map(ctx):    
    await ctx.send(f'Herewith link for transportation map Monitoring: https://www.google.co.id/maps')


bot.run('token')
