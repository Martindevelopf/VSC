"""Escriba un programa que pida dos números y muestre cuál es el menor.

numero_1 = int(input("ingrese un numero: "))
numero_2 = int(input("ingrese otr numero: "))


while True:
    if numero_1 <numero_2:
        print(f"el {numero_1} es menor ")
        break
    else:
            print(f"el {numero_2} es menor ")
            break

Escriba un programa que pida dos números y muestre todos sus divisores comunes.

numero_1 = int(input("ingrese un numero: "))
numero_2 = int(input("ingrese otr numero: "))

for i in range (1,numero_1+1):
     if numero_1%i==0 and numero_2%i==0:
        print(i)


Escriba un programa que pida un número entero positivo y calcule la suma de todos los números desde ese número hasta 1.
numero_1 = int(input("ingrese un numero: "))
suma=0
for i in range (numero_1,1,-1): 
    suma+=i

print(f"la suma total desde {numero_1} hasta 1 : {suma}")"""

lista_1 = []
lista_2 = []
listadivisores_comunes = []

numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))

# Obtener divisores de numero_1
for i in range(1, numero_1 + 1):
    if numero_1 % i == 0:
        lista_1.append(i)

# Obtener divisores de numero_2
for i in range(1, numero_2 + 1):
    if numero_2 % i == 0:
        lista_2.append(i)

# Encontrar divisores comunes
for divisor in lista_1:
    if divisor in lista_2:
        listadivisores_comunes.append(divisor)

# Obtener el máximo divisor común
mcd = max(listadivisores_comunes)

print(f"Divisores de {numero_1}: {lista_1}")
print(f"Divisores de {numero_2}: {lista_2}")
print(f"Divisores comunes: {listadivisores_comunes}")
print(f"Máximo común divisor (MCD): {mcd}")
