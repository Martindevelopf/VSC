# 1. Contar del 1 al 10 ✅

"""for i in range (1,11):
    print(i)

# Contar del 10 al 1 (en reversa)✅

for i in range (10,0,-1):
    print(i)


Mostrar los números pares del 1 al 20✅

for i in range(1,21):
    if i %2==0:
        print(i)


 Sumar los números del 1 al 100✅
suma=0
for i in range(1,101):
    print(i)  
    suma=suma+i

print(suma)
5. Mostrar la tabla de multiplicar del 5✅
resultado=0
for i in range (1,11):
    resultado= i*5
    print(f" {i} x 5 ={resultado}")

6-Pedir un número al usuario y mostrar su tabla ✅

num = int(input("Ingrese el numero a mostrar su Tabla:"))
resultado=0
for i in range (1,11):
    resultado = i*num
    print(f" {i} x {num} ={resultado}")
    
7- Mostrar los caracteres de una palabra

Palabra = input("Ingrese una palabra: ")

for i in Palabra:
     print(i,end="") # para dejarlo en la misma liena va ese end="" sin eso  salta linea

# 8-Mostrar los números del 1 al 50, pero solo múltiplos de 3

for i in range(1,51):
    if i%3==0:
        print(i)
    NIVEL INTERMEDIO
9 Sumar los dígitos de un número

numero ="1234"
suma =0

for i in numero:
    suma=suma+int(i)
    



print(suma)

 10-Contar cuántos números pares e impares hay entre 1 y 100

pares=0
impares=0
for i in range(1,101):
   if i%2==0:
      pares+=1
   else:
      impares+=1
    
print(f"la cantidad de numeros pares es{pares} y de impares es {impares}")     
 11. Mostrar todos los divisores de un número 

numero = int (input("Ingrese un numero:"))

for i in range(1,numero+1):
    if numero%i==0:
        print(i)

12 :Determinar si un número es primo"""

num = int(input("Ingrese un n: "))
suma = 0 # para ir guardando la suma de los primos

for numero in range(1, num+1): #  para que se fije los primos dentro del rango
    esprimo = True
    if numero == 1:  # control especial para el 1
        esprimo = False

    for i in range(2, numero): 
        if numero % i == 0: #  si resto 0 no es primo 
            esprimo = False #   resto 0 entonces hay un divisible entonces ya no es primo
            break #  corta asi no lo muestra en el print

    if esprimo:
        print(f"{numero} es primo")
        suma += numero

print(f"La suma total de los primos entre 1 y {num} es {suma}")

