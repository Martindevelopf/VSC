

"""
suma = 0

for numero in range(2, 51):  # parte 1
    es_primo = True
    for i in range(2, numero):  # parte 2
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        suma += numero
        print(f"{numero} es primo")

print(f"La suma de los primos entre 1 y 50 es: {suma}")

suma = 0 #para ir guardando la suma de cada primo

for numero in range(2, 51):  
    es_primo = False

    for i in range(2, numero):
        if numero % i == 0: #es divisor
            es_primo = False
            break
    else:
        es_primo = True

    if es_primo:
        suma += numero
        print(f"{numero} es primo")

print(f"La suma de los primos de 1 a 50 es: {suma}")


print("Controlador número primo")
num = int(input("Ingrese un número: "))
suma=0 # ir guardando la suma de los primos , donde concha lo pongo  para que vaya guardando
es_primo = True
for i in range(2, num): #miro los divisores
         if num % i == 0:# al dar un divisor ya se cumple que no es primo cambio de t a f
            es_primo = False
            break


if es_primo:
    print(f"{num} es primo")
else:
    print(f"{num} no es primo")"""
"""✅ 1. Imprimir los números del 1 al 10
for i in range(1,11):
    print(i)


2Saber si un número es par o impar

numero= int (input("ingrese un numero:"))

if numero % 2 ==0:
    print(f"el numero {numero}es par")
else:
        print(f"el numero {numero} es impar")
    
3 Imprimir los divisores de un número


numero= int (input("ingrese un numero:"))
#divisores=0
#divisores=[]
esprimo=True
for i in range (1,numero+1):
    if numero%i==0:
        # divisores.append(i)
         print(f"{i} es divisor de {numero}")
         divisores+=1
print(divisores)"""
"""
# SACAR PRIMO ITERANDO HASTA LA MITAR DEL RANGO
numero = int(input("Ingrese un número: "))

esprimo = True

if numero < 2:
    esprimo = False
else:
    for i in range(2, numero//2+1):
        if numero % i == 0:
            esprimo = False
            break 

if esprimo:
    print("Es primo")
else:
    print("No es primo")

# SACAR PRIMO ITERANDO HASTA LA MITAR DEL RANGO
esprimo = True

numero = int(input("Ingrese un número: "))


if numero < 2:
    esprimo = False
else:
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            esprimo = False
            break 

if esprimo:
    print("Es primo")

else:
    print("No es primo")
    
suma = 0 #para ir guardando la suma de cada primo

for numero in range(2, 51):  
    es_primo = False

    for i in range(2, numero):
        if numero % i == 0: #es divisor
            es_primo = False
            break
    else:
        es_primo = True

    if es_primo:
        suma += numero
        print(f"{numero} es primo")

print(f"La suma de los primos de 1 a 50 es: {suma}")"""
def saludar(nombre):
    print("Hola", nombre)

resultado = saludar("Martín")
print("Resultado:", resultado)
