
"""RAICES DESDE 1 AL NUMERO INGRESADO 
num = int(input("INGRESE UN NUMERO :"))

raiz=0

for i in range(1,num +1):
     raiz = i ** 0.5
     print(f"La raíz cuadrada de {i} es {raiz:.3f}")"""
    
"""Escriba un programa que lea un entero positivo n y despliegue la ra´ız cuadrada de los n primeros naturales
 primos.

num = int(input("INGRESE UN NUMERO : "))
es_primo = True
raiz=0
if num < 2:
    es_primo = False
else:
    for i in range(2, int(num + 1):
        if num % i == 0:
            es_primo = False
            break
        else:
            raiz= i**0.5
            print(raiz)

if es_primo:
    print("es primo")
else:
    print(f"{num} no es primo")

num = int(input("Ingrese un número: "))

print("Números primos hasta", num, ":")

for i in range(2, num + 1):
    es_primo = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            es_primo = False
            break
    if es_primo:
        print(f"el número primo es: {i} y su raíz cuadrada es: {i ** 0.5:.2f}")

 Escriba un programa que lea un entero positivo n y despliegue la raız cuadrada de los n primeros naturales
 primos."""
"""
si pongo 4 tiene que darme los primeros 4 primos y su raiz
pido un numero : 4
tengo qeu fijarme cuales son los primeros 4 primos , osea voy sacando primos hasta que
un contador de primos de 4 , cuando llego break y me tiene que hacer la operacion de las raices
pero no entiendo si la operacion la hago al final o en cada iteracion cuando encontre un primo?

num = int(input("Ingrese un número: "))
contnumprimo=None
if num<=1:
    print("no es primo")

else:
    for i in range(2,contnumprimo):


# Mostrar los números del 1 al 10

for i in range (1,11):
    print(i)
   
    
     
       Ejercicio 2: ¿Es primo o no? 
num = int(input("Ingrese un número: "))
es_primo = True

if num < 2:
    es_primo = False
else:
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break

if es_primo:
    print(f"El número {num} es primo")
else:
    print(f"El número {num} NO es primo")
    
    
🧱 Paso 3: Sacar raíz cuadrada

import math

num = int(input("Ingrese un número: "))
raiz = math.sqrt(num)
print(f"La raíz cuadrada de {num} es {raiz:.2f}")

n = int(input("Ingrese un número: "))
for i in range(n):
    print(i)
✅ Ejercicio 5: Mostrar la raíz cuadrada de cada número del 1 al n
n = int(input("Ingrese un número: "))

for i in range (1, n+1):
    print(f"la raiz cuadrada de {i} es: {i**0.5:.2f}")
# Leer un entero positivo n y mostrar la raíz cuadrada de los primeros n números primos.
numero = int(input("¿Cuántos primos querés ver? "))

contador = 0
num = 2  # Empezamos probando desde el número 2

while contador != numero:
    esprimo = True

    for i in range(2, num):  # PROBAMOS si num es divisible por algún número entre 2 y num-1 ( porque el mismo numero no me voy a fijar )
        if num % i == 0:
            esprimo = False
            break

    if esprimo:
        print(f"La raíz cuadrada de {num} es: {num**0.5:.2f}")
        contador += 1  # Solo aumentamos si encontramos un primo

    num += 1  # SIEMPRE pasamos al siguiente número, primo o no

numero =  int(input("Ingrese un numero:"))

esprimo=True

if numero <2:
     esprimo=False
        
else:
     for i in range (2,numero):  #aca recorro desde 2 a un numero antes que el numero para ver si es primo
        if numero%i ==0: # si es divisilbe entre dos no es primo , ahi no debo buscar mas
            esprimo=False
            break

        if esprimo :
            print(f"el numero {numero} es primo ")

        else:
            print(f"el numero {numero}  NO es primo ")
# jercicio 2: Mostrar todos los primos del 1 al n"""


numero =  int(input("Ingrese un numero:"))


for i in range(1, numero+1):
       esprimo=True
       if i<2:
              esprimo:False
              break
       else:
            for j in range (2, i):
                if i%j ==0: # si es divisilbe entre dos no es primo , ahi no debo buscar mas
                    esprimo=False
                    break
if esprimo:
    print(f"el numero {i} es primo")         