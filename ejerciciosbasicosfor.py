# 🟢 Ejercicio 1: Contar del 1 al 10
"""
for i in range (1,11):
    print(i)

Ejercicio 2: Mostrar los números pares del 0 al 20

for i in range(0,21):
    if i%2==0:
        print(i)

Ejercicio 3: Sumar los números del 1 al 100
suma=0
for numero in range( 1,101):
    suma = suma +numero

print(suma)


Escriba un programa en Pascal que calcule el factorial de un numero natural n (leido
 de la entrada estandar). Para este ejercicio, solamente se permite utilizar las operaciones
 aritmeticas elementales de Pascal (+,-, *, /, DIV, MOD). Incluya mensajes de salida con
 etiquetas descriptivas para solicitar y exhibir los valores

 factorial de 4!= 4x3x2x1 =24
numero = int(input("Ingrese el numero al cual le desea calcular el factorial:"))
factorial =1
for i in range(numero, 0,-1):
    factorial= factorial*i

print(f"el factorial de {numero} = {factorial}")


Escriba un programa en Pascal que lea de la entrada estandar n enteros positivos, todos
 menores que 60 y produzca una gra ca de n barras horizontales formadas por asteriscos
 (similar a la que se muestra en el ejemplo). La k-esima barra debera tener tantos asteriscos
 como indique el k-esimo entero (de entre los n enteros ingresados). Su programa no necesita
 controlar que los enteros ingresados sean menores que 60 (asuma que as sera). Incluya
 mensajes de salida con etiquetas descriptivas para solicitar y exhibir los valores.
  Ingrese un valor para n: 5
 Ingrese 5 enteros positivos: 7 12 17 35 8
 *******
 ************
 *****************
 ***********************************
 ********
n = int(input("¿Cuántos números va a ingresar?: "))
resultado =""
for i in range(n):
    valor = int(input("Ingrese un número positivo: "))

    resultado += "*" * valor + "\n"  # sumamos la barra y salto de línea

print("Resultado final:")
print(resultado)
    

 Escriba un programa en Pascal que lea de la entrada estandar un caracter c y un natural n.✔
 
 El programa debe desplegar un triangulo de n lneas formado por el caracter c (similar al
 que se muestra en el ejemplo). La primera lnea debe tener n ocurrencias de c. La segunda
 lnea debe tener n-1 ocurrencias de c (y as sucesivamente). La ultima lnea debe tener
 1 ocurrencia de c. Incluya mensajes de salida con etiquetas descriptivas para solicitar y
 exhibir los valores.
  Ingrese un caracter c: &
 Ingrese un valor para n: 8
 &&&&&&&&
 &&&&&&&
 &&&&&&
 &&&&&
 &&&&
 &&&
 &&
 &
c = input("Ingrese un caracter?: ")
n = int(input("Ingrese un natural n: "))
resultado=""
for i in range(n,0,-1):
    resultado= c*i # "" = & x 8 = se guarda en reslutado y se muestra 
    print(resultado)

    
Considere la funcion f tal que f(x) = x2 18x+5, donde x es un valor entero en el entorno
 de m a n, siendo m y n dos enteros tales que m n.
 Escriba un programa en Pascal que lea los valores para m y n de la entrada estandar y
 despliegue en la salida estandar el valor maximo de f(x) para x en ese entorno. Incluya
 mensajes de salida con etiquetas descriptivas para solicitar y/o exhibir los valores.

print("funcion f tal que f(x) = x2 18x+5!!!!!")
m = int(input("Ingrese m?: "))
n =int( input("Ingrese n?: "))
resultado=1
for i in range (m,n):
    resultado= (m**2) (18*m)+5
print(resultado)
suma = 0

for num in range(2, 51):  # empezamos en 2 porque 1 no es primo
    es_primo = True
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        suma += num

print("La suma de los números primos entre 1 y 50 es:", suma)

Contar cuántos números entre 1 y 500 son divisibles por 7"""

contador=0
for i in range(1,501):
        if i%7==0:
            contador +=1
print(contador)