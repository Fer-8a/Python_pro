#primero importamos el modulo random
import random
#ponemos todos los caracteres posibles que puede tener la contraseña 
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
#pedimos al usuario que ingrese la longitud de la contraseña
longitud = int(input("¿Cuántos caracteres tendrá la contraseña? "))
#generamos una contraseña aleatoria con el numero de caracteres que quiera el usuario 
contraseña = ''
#usamos un bucle for para crear una contraseña aleatoria pero con la longitud que el usuario haya elegido
for i in range(longitud):
    #usamos random.choice para elegir un caracter al azar de la variable caracteres
    #lo conectamos con la variable de contraseña para que se junten y dar el resultado final
    contraseña += random.choice(caracteres)
#imprimimos la contraseña final 
print(contraseña)
