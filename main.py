import discord
from discord.ext import commands
import random
import os
import requests



intent = discord.Intents.default()
intent.message_content = True

bot = commands.Bot(command_prefix='$', intents=intent)
@bot.event
async def en_momento():
    print(f'tu bot {bot.user} esta en linea')
    

@bot.command()
async def kodland(ctx):

    await ctx.send('\U0001F642')

@bot.command()
async def repetir(ctx , *, mensaje: str):

    await ctx.send(mensaje)
    
@bot.command()
async def saludo(ctx,*,mensaje:str):

    mensaje = mensaje.lower().strip()

    if 'hola' in mensaje:

        await ctx.send('Hola, ¿cómo estás?')

    elif 'que onda' in mensaje:

        await ctx.send('Que onda, ¿cómo estás?')
    
    else:

        await ctx.send('No entendi tu saludo pero holaaaaaaaaa')


@bot.command()
async def juegos(ctx,*,mensaje:str):

    mensaje = mensaje.lower().strip()

    if 'fortnite' in mensaje:

        await ctx.send('Fortnite es un juego de batalla real muy popular.')

        if 'bueno' in mensaje:

            await ctx.send('¡Sí, es muy divertido!')
        
        if 'malo' in mensaje:

            await ctx.send('A mi me parece muy bueno pero cada quien sus gustos.')
        
        if 'jugar ' in mensaje:

            await ctx.send('¡Claro! ¿Quieres jugar Fortnite? ¡Descargalo en la Epic Games Store!')
        
        if 'divertido' in mensaje:

            await ctx.send('Si, es muy divertido fortnite. A mi me gusta mucho jugarlo con mis amigos bots')
            
        else:

            await ctx.send('No entiendo tu mensaje sobre Fortnite.')
   
    if 'rocket league' in mensaje:

        await ctx.send('Rocket League es un juego de fútbol con coches.')

        if 'bueno' in mensaje:

            await ctx.send('¡Sí, es muy divertido me encanta poder jugar futbol con mis carros favoritos!')
        
        if 'malo' in mensaje:

            await ctx.send('A mi me parece muy bueno pero cada quien sus gustos.')
        
        if 'jugar ' in mensaje:

            await ctx.send('¡Claro! ¿Quieres jugar Rocket League? ¡Descargalo en la Epic Games Store!')
        
        if 'divertido' in mensaje:

            await ctx.send('Si, es muy divertido . A mi me gusta mucho jugar futbol con carros')
        
        if 'de que trata' in mensaje:

            await ctx.send('Rocket League es un juego de futbol con carros, donde puedes jugar con tus amigos o tu solo. Puedes jugar en modo competitivo o casual. Y puedes hacer muchas acrobacias con los carros')
        
        else:

            await ctx.send('Lo siento no entiendo tu mensaje/pregunta robre rocket league')
   
    if 'roblox' in mensaje:

            
            await ctx.send('Roblox es una plataforma de juegos en línea donde los usuarios pueden crear y jugar juegos creados por otros usuarios.')
    
            if 'bueno' in mensaje:
    
                await ctx.send('¡Sí, es muy divertido!')
            
            if 'malo' in mensaje:
    
                await ctx.send('Algunos juegos pueden ser un poco aburridos.')
            
            if 'jugar ' in mensaje:
    
                await ctx.send('¡Claro! ¿Quieres jugar Roblox? ¡Descargalo en cualquier navegador web!')
            
            if 'divertido' in mensaje:
    
                await ctx.send('Si, es muy divertido. A mi me gusta mucho jugarlo con mis amigos bots')
            
            else:
    
                await ctx.send('No entiendo tu mensaje sobre Roblox.')

@bot.command()
async def pregunta(ctx,*,mensaje:str):
    
        mensaje = mensaje.lower().strip()
    
        if 'cuantos años tienes' in mensaje:
    
            await ctx.send('Soy un bot y no tengo edad.')
    
        elif 'como te llamas' in mensaje:
    
            await ctx.send('Soy juan 123 mucho gusto.')

        elif 'quien te creo' in mensaje:

            await ctx.send('Me creo un programador llamado Fer.')

        else:
    
            await ctx.send('No entiendo tu pregunta.')

@bot.command()
async def despedida(ctx,*,mensaje:str):

    mensaje = mensaje.lower().strip()

    if 'adios' in mensaje:

        await ctx.send('Adios, ¡que tengas un buen día!')

    elif 'hasta luego' in mensaje:

        await ctx.send('Hasta luego, ¡cuídate!')
    

    
    else:

        await ctx.send('No entiendo tu despedida pero adios.')

@bot.command() 
async def sumar (ctx, a: int, b: int):

    resultado = a + b

    await ctx.send(f'La suma de {a} y {b} es {resultado}.') 

@bot.command() 
async def dividir (ctx, a: int, b: int):

    if b == 0:
        await ctx.send('No se puede dividir entre cero.')
    else:
        resultado = a / b
        await ctx.send(f'La division de {a} y {b} es {resultado}.') 
    
@bot.command()
async def restar (ctx, a: int, b: int):

    resultado = a - b

    await ctx.send(f'La resta de {a} y {b} es {resultado}.')

@bot.command()
async def multiplicar (ctx, a: int, b: int):

    resultado = a * b

    await ctx.send(f'La multiplicacion de {a} y {b} es {resultado}.')

@bot.command()
async def contraseña(ctx,*,mensaje:str):

    if "genera una contraseña" in mensaje:
    
        import random
        caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        longitud = random.randint(8, 20)  
        contraseña = ''
        for i in range(longitud):
            contraseña += random.choice(caracteres)
        

        await ctx.send('¡Claro! Aquí tienes una contraseña:')
        await ctx.send(contraseña)

@bot.command()
async def ayuda(ctx):
    await ctx.send('''
    **Comandos disponibles:**
    - $kodland: Responde con una carita feliz.
    - $repetir <mensaje>: Repite el mensaje que le envíes.
    - $saludo <mensaje>: Responde a tu saludo.
    - $juegos <mensaje>: Responde a preguntas sobre juegos.
    - $pregunta <mensaje>: Responde a preguntas comunes.
    - $despedida <mensaje>: Responde a tu despedida.
    - $sumar <a> <b>: Suma dos números.
    - $restar <a> <b>: Resta dos números.
    - $multiplicar <a> <b>: Multiplica dos números.
    - $dividir <a> <b>: Divide dos números.
    - $contraseña: Genera una contraseña aleatoria.
    ''')

@bot.command()
async def mem1 (ctx):
    
    with open('imagenes/mem1.jpg', 'rb') as file:
        
        picture = discord.File(file)
        
        await ctx.send(file=picture)

@bot.command()
async def mem4 (ctx):
    
    with open('imagenes/mem4.jpg', 'rb') as file:
        
        picture = discord.File(file)
        
        await ctx.send(file=picture)


@bot.command()
async def meme_aleatorio(ctx):
    
    img_name = random.choice(os.listdir('imagenes'))
    
    with open(f'imagenes/{img_name}', 'rb') as file:
        
        picture = discord.File(file)
        
        await ctx.send(file=picture)


def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('perro')
async def imagen_perro(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)
    

token = ''

bot.run(token)


