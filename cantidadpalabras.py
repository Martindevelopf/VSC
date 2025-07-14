"""
Escriba un programa que lea una letra y una oraci´on y despliegue la cantidad de palabras de la oraci´on
 que terminan con la letra dada. Se asume que la oraci´on es una secuencia de palabras separadas solo
 por espacios, y que terminan con el car´acter punto (.). La oraci´on siempre tiene al menos una palabra.



frases = []
frases = []
char= input("escribi un caracter")
frase = input("Escribí una frase: ")
cantidadcaracteres=0

frases.append(frase)


def cantidad_P(frase):
    for i in frase:
        if i ==char and (frase[i+1]==" "):
            cantidadcaracteres+=1


print(cantidadcaracteres)"""

"""Ejercicio 1 – Crear una lista desde una oración


frase = input("Escribí una frase: ")

frases=list(frase)

print(frases)asi me lo saca en letras indivudalees"""

"""para que me lo separe por espacios es split

frase = input("ingresa una frase: ")
char= input("ingresa un caracter: ")
contador=0
palabras = frase.split()

for palabra in frase:
    if palabra.endswith(char):
        contador+=1
    #  (b) Escriba un programa que despliegue la cantidad de palabras que comienzan con la letra leida
    #  en este caso debo poner starwhith(char)
   


print(f"la frase tiene {contador} palabras que terminan con {char}")
    # print(i, end="")"""
#(c) Escriba un programa que despliegue la cantidad de palabras que contienen la letra una sola vez.

char= input("ingresa un caracter: ")
contador=0
while True:
    frase = input("Ingresa una frase (terminá con punto para salir): ")
    
    if frase.endswith("."):
        break
palabras = frase.split()
for palabra in palabras:
    if palabra.count(char) == 1: 
         contador+=1
    


print(f"la frase tiene {contador} palabras  {char}")