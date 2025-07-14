"""# 🔹 1. Mostrar los números del 1 al 10

for i in range(1,11):
    print(f" la iteracion numero {i} es {i}")
 2. Mostrar los números del 10 al 1 (en reversa)

for i in range (10, 0, -1):
    print(f" la iteracion numero {i} es {i}")

Mostrar los números pares del 1 al 20    
    
    
for i in range(1,21):
    if i%2==0:
        print(f"el numero {i} es par")
    # else:
                # print(f"el numero {i} NO es par")
                # 
    4. Mostrar los números impares del 1 al 20

for i in range(1,21):
    if i%2!=0:
        print(f"el numero {i} es impar")
        
5. Mostrar la tabla del 5 (del 5 al 50)


num = int(input("ingrese el numero de la tabla que desea calcular:"))
for i in range(1,11):
    print(f" {i}X 5 = {i*num}")
    
🔹 6. Sumar los números del 1 al 10


suma=0 # para ir guardando suma mientras itera

for i in range (1,11):
    suma=suma+i
    print(suma)  
print(suma)


🔹 7. Contar cuántos múltiplos de 3 hay entre 1 y 100


contador=0

for i in range (1,101):
    if i%3==0:
        print(f"el numero {i} es multiplo de 3")
        contador+=1
    # else:
    #     print(f"{i} no es multipplo de 3")
print(f"la cantidad de multiplos de 3 es: {contador}")

🔹 8. Mostrar todos los cuadrados del 1 al 10

for i in range (1,11):
    print(f" el cuadrado de {i} es {i*i}")
9. Pedir al usuario 5 números y mostrarlos al revés

numeros = []
for i in range(5):
    n = int(input("Ingrese un número: "))
    numeros.append(n)

for i in reversed(numeros):
    print(i)
Pide un número y muestra todos los números desde 1 hasta ese número usando while.

n = int(input("Ingrese un número: "))
contador = 1

while contador <= n:
    print(contador)
    contador += 1


Ejercicio 2: Sumar números hasta que el usuario ingrese 0



suma = 0
num = int(input("Ingrese un número (0 para terminar): "))

while num != 0:
    suma += num
    num = int(input("Ingrese otro número (0 para terminar): "))

print(f"La suma total es: {suma}")



Ejercicio 4: Mostrar números pares hasta n

num = int(input("Ingrese un número :")) 

contador =0

while contador <=num:
    if contador%2==0:
        print(contador)
    contador+=1
🔁 Ejercicio 1: Contar hasta un número
num = int(input("Ingrese un número :")) 

contador=1
while contador <= num:
    print(contador)
    contador+=1
    
🔢 Ejercicio 2: Contar de 10 a 1


contador=10
while contador>=1:
    print(contador)
    contador-=1
    
    
 Usando un while, sumá todos los números del 1 al 100 y mostrale al usuario el resultado.

  
contador=1
suma=0
while contador <=100:
    suma+=contador
    contador+=1
print(f"la suma del 1 al 100 es : {suma}")

🔄 Ejercicio 4: Pedir números hasta que el usuario escriba 0 

num=int(input("ingrese un numero : si desea cancelar 0:"))

while num !=0:
    num=int(input("ingrese un numero : si desea cancelar 0"))

    
    
 Ejercicio 5: Contar cuántos números positivos ingresa el usuario
Pedile números al usuario hasta que escriba un número negativo. Al final, mostrá cuántos números positivos ingresó.  

num=int(input("ingrese un numero : si desea cancelar 0:"))
contador=0
while num >=0:
    num=int(input("ingrese un numero : si desea cancelar ingrese negativo"))
    contador+=1

print(f"la cantidad de numeros positivos ingresados es : {contador}")



Seguir pidiendo hasta que se ingrese un número par
Pedir números hasta que el usuario escriba un número par. Al final mostrale cuántos intentos hizo.

num=int(input("ingrese un numero : "))
contador=0
while num %2 !=0:
    num=int(input("ingrese un numero :"))
    contador+=1
print(contador)

💯 Ejercicio 5: Mostrar los múltiplos de 5 entre 1 y 100

Usá while para mostrar los múltiplos de 5 desde 1 hasta 100.

contador =1

while contador <=100:
    if contador %5 ==0:
        print(f"{contador} es multiplo de 5 ")
    contador+=1
    
    
Ejercicio 6: Calcular el factorial de un número
El factorial de un número n (por ejemplo 5) es:
5! = 5 × 4 × 3 × 2 × 1 = 120

Pedí un número y usá while para calcular su factorial.

num=int(input("ingrese un numero : "))
resultado=1
while num >=1:
    resultado = resultado *num
    num = num-1
print(resultado)

Pedí un número y usá while para calcular su factorial.

5! = 1 × 2 × 3 × 4 × 5 = 120

num = int(input("Ingrese un número: "))
resultado = 1
contador = 1

while contador <= num:
    resultado = resultado*contador
    contador += 1

print(f"El factorial de {num} es {resultado}")
Contar cuántos números positivos se ingresan

# Pedí al usuario que ingrese números.
# Contá cuántos son positivos.
# Terminá cuando se ingrese un número negativo.



num = int(input("Ingrese un número: "))
contador=1

while num >=0:
    num = int(input("Ingrese un número: "))
    if num >0:
        contador+=1
print(contador)
Adivinar el número


# Elegí un número secreto (por ejemplo, 17).
# El usuario tiene que adivinarlo.
# Decile si el número es mayor o menor. Usá while hasta que acierte.



def nummayormenoroigual(num):
    if num ==num_secreto:
        print(f"HAS ADIVINADO EL NUMERO  PAPANATAS!!!!")
    elif num<num_secreto:
        print(f" el numero { num} es menor que el numero secreto , sigue intentando CRACK")
    else:
        print(f" el numero { num} es mayor que el numero secreto , sigue intentando GROSO")
        
num_secreto=10
num = int(input("Ingrese un número: "))
nummayormenoroigual(num)
while num !=num_secreto:
    num = int(input("Ingrese un número: "))
    nummayormenoroigual(num)

*********************Validar contraseña


# Mientras el usuario no escriba la contraseña correcta ("python123"), pedí que la reingrese.



contraseña ="python123"
contraseña_ingresada= input("Ingrese su contraseña: ")

while contraseña_ingresada !=contraseña:
    contraseña_ingresada= input(" error contraseña incorrecta , Ingrese su contraseña :")
    

print("ACCESO CORRECTO")

# Calculá el factorial de un número usando while.
#5! = 5 × 4 × 3 × 2 × 1 = 120

num = int(input("Ingrese un número: "))
resultado=1
guardar= num
while num>=1:
    resultado= resultado*num
    num-=1

print(f"el factorial de {guardar}! = {resultado}")

# El usuario ingresa notas una por una. Terminá con -1.
# Calculá y mostrale el promedio de las notas.
nota = int(input("Ingrese su nota!!!!!!!: "))
resultado = 0
divisor = 0

while nota != -1:
    resultado += nota
    divisor += 1
    nota = int(input("Ingrese su nota: "))

if divisor > 0:
    promedio = resultado / divisor
    print(f"El promedio de tus {divisor} notas es: {promedio}")
else:
    print("No ingresaste ninguna nota.")

    
    
    
# Pedir una edad al usuario hasta que sea válida (entre 0 y 120).

edad= int(input("INGRESE SU EDA: "))

while edad >0 and edad <=120:
# Pedir números al usuario hasta que ingrese -1.
# Contar cuántos fueron pares y cuántos impares.

num = int(input("INGRESE UN NÚMERO: "))
cantpares = 0
cantimpares = 0

while num != -1:
    if num % 2 == 0:
        cantpares += 1
    else:
        cantimpares += 1
    num = int(input("INGRESE UN NÚMERO: "))

print(f"Cantidad de números pares ingresados: {cantpares}")
print(f"Cantidad de números impares ingresados: {cantimpares}")
# El usuario ingresa números (termina con -1)
# Mostrar cuál fue el número más grande ingresado
num = int(input("INGRESE UN NÚMERO: "))
mayor=num
while num != -1:
    if num>mayor:
        mayor=num
    num = int(input("INGRESE UN NÚMERO: "))

print(f"el numero mayor es {mayor}")
---------------------------------------------------
num = int(input("INGRESE UN NÚMERO: "))

if num == -1:
    print("No se ingresaron números válidos.")
else:
    mayor = num
    num = int(input("INGRESE UN NÚMERO: "))
    while num != -1:
        if num > mayor:
            mayor = num
        num = int(input("INGRESE UN NÚMERO: "))

    print(f"El número mayor es {mayor}")
    
    Menú con opciones (simulación)
Mostrá un menú como este:


1 - Ver saldo
2 - Ingresar dinero
3 - Retirar dinero
4 - Salir
El usuario elige una opción y el programa responde.
Se repite hasta que elige 4.


numeros = []

for i in range(5):
    num = int(input(f"Ingresá el número {i + 1}: "))
    numeros.append(num)

print("Lista de números:", numeros)"""

for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
