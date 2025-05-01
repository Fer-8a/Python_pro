import discord
from discord.ext import commands
import random
import os
import requests

intent = discord.Intents.default()
intent.message_content = True

bot = commands.Bot(command_prefix='$', intents=intent)

@bot.event
async def on_ready():
    print(f'Tu bot {bot.user} está en línea')

@bot.command()
async def hola(ctx):
    await ctx.send(' Hola soy un bot que te ayudara con todo sobre la contaminacion. \U0001F642')


bot.command("aleatoria")
async def imagen_aleatoria(ctx):
    
    img_name = random.choice(os.listdir('imagenes contaminacion'))
    
    with open(f'imagenes contaminacion/{img_name}', 'rb') as file:
        
        picture = discord.File(file)
        
        await ctx.send(file=picture)
        await ctx.send('Esto es algo muy triste ayuda al planeta.')

@bot.command()
async def con_1 (ctx):
    
    with open('imagenes/con_1.jpg', 'rb') as file:
        
        picture = discord.File(file)
        
        await ctx.send(file=picture)

@bot.command()
async def con_2 (ctx):
    
    with open('imagenes/con_2.jpg', 'rb') as file:
        
        picture = discord.File(file)
        
        await ctx.send(file=picture)
        
@bot.command()
async def con_3 (ctx):
    
    with open('imagenes/con_3.jpg', 'rb') as file:
        
        picture = discord.File(file)
        
        await ctx.send(file=picture)
        

@bot.command()
async def contaminacion(ctx, *, mensaje: str):
    
    mensaje = mensaje.lower().strip()
    
    if 'contaminacion' in mensaje:
        
        await ctx.send('La contaminación es un problema ambiental grave.')
        
        if 'bueno' in mensaje:
            
            await ctx.send('No la contaminacion es un problema muy grave.')
            
        if 'malo' in mensaje:
            
            await ctx.send('¡Sí, es un gran problema!')
            
        if 'solucion' in mensaje:
            
            await ctx.send('La solución es reducir la contaminación.')
            
        if 'causas' in mensaje:
            
            await ctx.send('Las causas son muchas, como el uso excesivo de combustibles fósiles.')

        if "ayudar" in mensaje: 
            
            await ctx.send('Podemos ayudar a reducir la contaminación usando menos plástico y reciclando.')

@bot.command("lugares de contaminacion")
async def lugares_de_contaminacion(ctx, *, mensaje: str):
    
    mensaje = mensaje.lower().strip()
    
    if 'lugares' in mensaje:
        
        await ctx.send('' 
        '1.-Zona Metropolitana del Valle de México CDMX y área conurbada,' 
        ' 2.- Monterrey,Nuevo León,  ' 
        '3.- Toluca, Estado de México, ' 
        '4.- Guadalajara, Jalisco, ' 
        '5.-Tula, Hidalgo')
        
    if "causas" in mensaje: 
        
        await ctx.send('Tráfico vehicular,' 
        ' industria,' 
        ' y condiciones geográficas,' 
        '  Industria pesada,' 
        ' tráfico y refinerías cercanas,' 
        ' Tráfico vehicular,' 
        ' quema de basura,' 
        ' industria local,' 
        ' Refinería de PEMEX,' 
        ' termoeléctrica y otras industrias pesadas,' 
        '  Vientos fuertes que levantan polvo,' 
        ' industria maquiladora y tráfico.')

token = ''

bot.run(token)