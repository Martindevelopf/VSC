"""FOR Es una estructura que te permite repetir un bloque de código una cantidad determinada de 
veces o sobre una secuencia (lista, rango, cadena, etc.).
for variable in secuencia:
    # bloque de código

    Resumen rápido:
Código	Qué hace
for i in range(a, b):	Cuenta desde a hasta b-1
for i in range(a, b, s):	Cuenta desde a hasta b-1 con paso s
variable	Cambia en cada iteración




#  Ejercicio 1: Contar del 1 al 10   ( con control c corto un for alto)

for i in range(1,11):
    print(f"numero :{i}")
# Ejercicio 2: Imprimir tu nombre 3 veces


nombre = input("Ingresa tu nombre :")
for i in range(1,4):
    print(f"nombre :{nombre}")


# Ejercicio 3: Imprimir los números pares del 2 al 10

for i in range (2,11,2):
    print(f"numero par:{i}")
#otra forma de hacerlo es : 
for i in range (2,11):
    if i%2==0:
        print(f"el numero {i} es par")
#  Ejercicio 4: Contar hacia atrás desde 5 hasta 1

for i in range (5,0,-1):
    print(f"{i}")
#  Ejercicio 5: Sumar los números del 1 al 4
suma=0
for i in range(1,5):
    suma = suma+i
#    print(f"suma {suma}")
print(f"suma {suma}")

#  Ejercicio 5: Sumar los números del 5 al 10
guardando=0
for i in range ( 5,11):
    guardando= guardando+i

print(f"la suma es {guardando}")
# Imprimir números del 1 al 10
# ej1: Muestra en pantalla los números del 1 al 10, uno por línea.

for iteracion in range(1,11):
    print(f" la iteracion {iteracion} es: {iteracion}")
ej2: Imprimir números pares del 2 al 20
Usa el parámetro de paso (step) para mostrar solo los números pares.
print("Los numeros pares del 2 al 20 son:")
for iteracion in range( 2,20,2):
    print(f" {iteracion}")
Imprimir la tabla de multiplicar del 5
Muestra la tabla del 5 (del 5x1 al 5x10).
print("la tabla del 5 es :")
for iteracion in range(1,11): # itero de 1 al 11 para que sea del 1 al 10
    print(f" 5x{iteracion}={iteracion*5}")
# ahora muestro 5x iteracion para ir sumando 1 2 3 4 hasta el 10 , y depsues pongo = a esea it x 5 entonces me va a quedar la tabla
#del 5
Sumar los números del 1 al 10
Calcula y muestra la suma total de los números del 1 al 10.

guardando = 0
for iteracion in range (1,11):
    guardando = guardando + iteracion
print(f"la suma es {guardando}")


Contar hacia atrás del 10 al 1
Imprime los números del 10 al 1 en orden descendente.

for decremento in range(10, 0, -1):
    print(f" {decremento}")

    Imprimir caracteres de una palabra
Dada una palabra, muestra cada letra en una línea separada.

    
palabrag =""
palabra ="pedro"
for iteracion in (palabra):
    palabrag = palabrag+iteracion
    
#print(palabrag)


Contar cuántas vocales tiene una palabra
Dada una palabra, cuenta y muestra cuántas vocales tiene.
palabra = input("Ingresa una palabra: ").lower()  # Convierte todo a minúscula
contvocales = 0

for p in palabra:
    if p in "aeiou":  # Comprueba si p es una vocal
        contvocales += 1

print(f"La cantidad de vocales en la palabra '{palabra}' es: {contvocales}")


palabra = input("ingreses una palabra:")
contvocales=0

for p in (palabra):
    if p == "a":
        contvocales = contvocales+1
    elif p== "e":
        contvocales = contvocales+1
    elif p== "o":
        contvocales = contvocales+1
    elif p== "u":
        contvocales = contvocales+1
    

print(f"la cantidad de vocales de la palabra {palabra} es : {contvocales}")


Multiplicar todos los números del 1 al 5
Calcula y muestra el producto de los números del 1 al 5.



multiplicacion=1 # arranque con 0 tuve problemas

for iteracion in range (1,6):
    multiplicacion *=iteracion
print(f"el resultado de multiplicar de 1 al 5 es:{multiplicacion}")




Sumar solo los números impares del 1 al 15
Calcula y muestra la suma de los números impares entre 1 y 15.

num_i= 0

for iteracion in range(1,16):
    if iteracion % 2 !=0:
        num_i = num_i+ iteracion

print(f"{num_i}")

Pedir 5 números al usuario y mostrar su suma
Usa un for para pedir 5 números, guardarlos y luego mostrar la suma total.


suma=0
for iteracion in range (1,6):
    numero = int(input("Ingrese 5 numeros por favor"))
    suma= suma + numero
print(f"{suma}")


 obtener la suma de todos los 
 obtener los numeros primos entre 1 y 50
 de 1 a 10 es 2+3+5+7 = 17
n es un nro primo si y solo si, solo es divisible entre si mismo y 1

print("SUMA DE LOS NUMEROS PRIMOS ENTRE 1 Y 50 ")
num = int(input("Ingrese un numero:"))


for i in range(1,num):
    if num%i >0 and num/1==num:
            print("es primo")
           
asterisco ="*"
for i in range (1,10):
    print(f" en la posiscion{i} esta {asterisco}")
          
# ENCONTRAR TODOS LOS NUMEROS MULTIPLOS DE 3 COMPRENDIDOS ENTRE DOS NUMEROS
a = int(input("ingrese el primer numero"))
b = int(input("ingrese el segundo numero"))

for i in range(a,b):
    if a%3==0:
        print(f"el numero {a} es multiplo de 3")
    a=a+1
# se puede hacer asi usando el i directamente , es mas corto y poniento los numeros del rango derecho
for i in range(2,10):
    if i%3==0:
        print(f"el numero {a} es multiplo de 3")
           # CONTAR CUANTOS MULTIPLOS DE 3 HAY ENTRE DOS NUMEROS
contador=0
for i in range ( 2,50):
        if i%3==0:
            contador+=1
print(contador)
        
         
          
            
# Ejercicio 1: Imprimir números del 1 al 10
# Escribe un programa que use un bucle for para imprimir en pantalla los números del 1 al 10, uno por línea.
for i in range(1,11):
    print(f"{i}")"""
"""
Ejercicio 2: Suma de los primeros N números enteros
Pide al usuario que ingrese un número entero N, luego calcula y muestra la suma de los números desde 1 hasta N usando un bucle for.
suma = 0
num = int(input("Ingrese un numero : "))

for i in range(1, num+1 ):
    suma +=i

print(f"{suma}")

Ejercicio 3: Tabla de multiplicar
Solicita un número entero M y muestra la tabla de multiplicar del 1 al 10 para ese número usando un bucle for.
num = int(input("Ingrese un numero : "))
for i in range (1,11):
    print(f" {num} X {i} = {i*num}")"""
"""Ejercicio 4: Factorial de un número
Calcula el factorial de un número entero positivo N (por ejemplo, 5 → 120) usando un bucle for.
FACTORIAL: 3! = 3 × 2 × 1 = 6
num = int(input("Ingrese un numero : "))
producto=1
for i in range (num, 0,-1):
        producto= producto*i
print(f"{producto}")





Ejercicio 5: Imprimir los primeros N números pares
Solicita un número N y muestra los primeros N números pares positivos usando un for.


num = int(input("Ingrese un numero : "))

for i in range (1,num+1):
     print(i*2)



Ejercicio 6: Imprimir los caracteres de una cadena
Dada una cadena de texto (por ejemplo "Hola"), usa un for para imprimir cada carácter en una línea separada.

texto="hola"

for i in texto:
    print(f"{i}")
    
    
    Ejercicio 7: Suma de números pares entre 1 y 100
Usa un bucle for para calcular la suma de todos los números pares del 1 al 100.

acumulador=0

for  i in range(1,101):
    if i%2==0:
        acumulador+=i
       
print(f"{acumulador}")


Ejercicio 8: Contar cuántos números divisibles por 3 hay entre 1 y N
Solicita un número entero N y cuenta cuántos números del 1 al N son divisibles por 3.

num = int(input("Ingrese un numero: "))
contador=0

for i in range (1,num+1):
    if i%3==0:
        contador+=1

print(f"{contador}")


Ejercicio 4: Factorial de un número
Calcula el factorial de un número entero positivo N (por ejemplo, 5 → 120) usando un bucle for.
FACTORIAL: 3! = 3 × 2 × 1 = 6




num = 5

acumulador=1
for i in range(num,0,-1):
    acumulador = acumulador*i


print(f"{acumulador}")
ejercicio 8 p1 : leer un numero por teclado y poner todos los divisores naturales de ese numero

numero =  int(input("Ingrese un numero:"))

for i in range (1,numero+1):
 
 if numero%i==0:
        print(f" {i} ese numero es divisor de {numero}")


        
        Ejercicio 9: Números del 1 al N en una línea
Pedir un número entero N
 y mostrar todos los números del 1 al N en una sola línea, separados por espacio.

numero =  int(input("Ingrese un numero:"))
guardar= 0
for i in range(1,numero+1):
    print(f"{i}",end=" ")


 Ejercicio 10: Mostrar los cuadrados de los primeros N números 

numero =  int(input("Ingrese un numero:"))

for i in range (1,numero+1):
    print(f" el cuadrado de {i} es : {i*i}")
    Ejercicio 11: Cuenta regresiva par
Mostrar los números pares del 20 al 0 (inclusivo), en orden descendente.




for i in range (20,0,-1):
    print(f"{i}")


print("DESPEGUE")

 Ejercicio 12: Sumar múltiplos de 5 entre 1 y 100
Usar un for para sumar todos los múltiplos de 5 entre 1 y 100. Mostrar el resultado.



resultado=0
for i in range(1,101):
    if i%5==0:
        resultado +=i

print(f"{resultado}")

 Ejercicio 13: Contar letras “a” en una palabra
Pedir una palabra al usuario y contar cuántas veces aparece la letra a.

palabra = input("Ingrese una palabra:")
cantp =0
for i in palabra:
    print(f"{i}")
    if i == "a":
        cantp +=1

print(f"La palabra {palabra} tiene {cantp} letras a")


 Ejercicio 14: Mostrar tabla de cuadrados
 
Número | Cuadrado
1      | 1
2      | 4
3      | 9
...


print("TABLA DE CUADRADOS")
numero =  int(input("Ingrese un numero:"))
print("Número | Cuadrado")
for i in range(1,numero):
    print(f" {i}  |  {i*i}")
    

Ejercicio 15: Mostrar solo los dígitos de un número

numero =  int(input("Ingrese un numero:"))

for i in str (numero):
    print(i)

16: Sumar solo los impares hasta N
    
numero =  int(input("Ingrese un numero:"))
sumar=0
for i in range (1,numero+1):
    if i%2 !=0: #si es true es impar
        sumar +=i
print(f"{sumar}")

Ejercicio 1:
Escribe un programa que pida un número entero N e imprima todos los números desde 1 hasta N (incluyendo N).


numero =  int(input("Ingrese un numero:"))
for i in range (1,numero+1):
    print(f" {i} ")
    
Ejercicio 2:
Escribe un programa que pida un número entero N e imprima la suma de todos los números pares desde 1 hasta N.

numero =  int(input("Ingrese un numero:"))
suma=0
for i in range (1,numero+1):
    if i%2==0:
      suma= suma+i
print(f"la suma de todos los numeros pares hasta {numero} es: {suma}")


Ejercicio 3:
Escribe un programa que pida un número entero N e imprima solo los múltiplos de 3 desde 1 hasta N.

numero =  int(input("Ingrese un numero:"))

for i in range (1,numero+1):
    if i%3==0:
        print(i)
 Ejercicio 4: Sumar los dígitos de un número
Pedir al usuario un número entero positivo. Mostrar la suma de sus dígitos. no lo pude hacer solo
        

numero =  int(input("Ingrese un numero:"))
suma=0
for i in str(numero):
    suma += int(i)
print(suma)

5: Verificar si un número es primo
Pedir al usuario un número entero mayor que 1. Mostrar si es primo o no.
📌 Recordá: un número primo solo se divide por 1 y por sí mismo.


numero =  int(input("Ingrese un numero enter:"))


if numero%numero!=0:
    print("es primo")
    


    Indique que se exhibira en la salida estandar al ejecutar cada uno de los siguientes progra
mas. Despues, ver que compilando y ejecutando.
 (a) program Ejercicio1a;
 var aux, n : Integer;
 begin
 aux := 2;
 for n := 1 to 4 do
 begin
 aux := aux * n;
 writeln(n, aux)
 end
 end.
aux =2

for i in range (1,5):
    aux *=i
    print(f"{i}, {aux}")
    
    
    
program Ejercicio1b;
 var a, b : Integer;
 begin
 for b := 1 to 3 do
 begin
 if b <= 1 then
 a := b- 1;
 if b <= 2 then
 a := a- 1
 else
 a := a + 1
 end;
 writeln(a)
 end

for i in range(1,4):
    if i<=1:
        a = i-1
    if i<=2:
        a = a-1
    else:
        a =a+1
print(a)

 Escriba un programa en Pascal que lea de la entrada estandar tres numeros naturales a, b
 y n. El programa debe exhibir en pantalla todos los multiplos de n que haya entre a y b.


a =  int(input("Ingrese primer numero:"))
b =  int(input("Ingrese segundo numero:"))
c =  int(input("Ingrese tercero numero:"))

for i in range(a,b+1 ):# el i va a tomar el valor de a
    if i%c==0:
        print(f"el numero{i} es multplico de {c}")

Escriba un programa en Pascal que 
lea de la entrada estandar un numero natural n. 

 continuacion, el programa debera leer n enteros y luego desplegar en pantalla el mayor y
 el menor de ellos. Incluya mensajes de salida con etiquetas descriptivas para solicitar y
 exhibir los valores.

n = int(input("¿Cuántos números va a ingresar? "))
numero = int(input("ingrese el primer numero? "))
mayor=numero
menor=numero

for  i in range (1,n+1):
    numero = int(input((f"ingrese un numero:")))

    if numero>mayor:
        mayor=numero
    else:
        numero<menor
        menor=numero

print(f"el numero mayor es{mayor}")
print(f"el numero mayor es{menor}")

# Inicializamos mayor y menor como None



cantidad_barras= int(input("Ingrese un valor para n"))


for i in range(cantidad_barras):
    barras= int(input(f"Ingrese {i} enteros positivos"))

    print("*" * barras)

aux =2


for i in range (1,4+1):
    aux = aux*i
    print(i,aux)

 Escriba un programa en Pascal que lea de la entrada estandar un numero natural n y
 despliegue en pantalla todos los divisores naturales de n

num = int(input("ingrese un numero natural n : "))

for i in range( 1,num+1):
    if num%i==0:# preunto si el numero ingresado modulo cada iteracion =0 si se cumple es divisor
        print(i)#muestro ese num osea el iterador

 Escriba un programa en Pascal que lea de la entrada estandar un numero natural n. 
 
 continuacion, el programa debera leer n enteros y luego desplegar en pantalla el mayor y
 el menor de ellos. Incluya mensajes de salida con etiquetas descriptivas para solicitar y
 exhibir los valores.
    

n = int(input("Ingrese la cantidad de números naturales a mostrar: "))
resultado = ""

for i in range(n):
    num = int(input("Ingrese un número natural: "))
    resultado += str(num) + " "

print("\nNúmeros ingresados:", resultado)
 Escriba un programa en Pascal que lea dos numeros naturales x, n de la entrada estandar
 y calcule la potencia de x elevado a la n. Para este ejercicio, solamente se permite utilizar
 las operaciones aritmeticas elementales de Pascal (+,-, *, /, DIV, MOD). Incluya mensajes
 de salida con etiquetas descriptivas para solicitar y exhibir los valores

x = int(input("Ingrese la base: "))
n =int(input("Ingrese la explonente: "))
potencia=1
for i in range (1, n+1):
    potencia=potencia*x

print(potencia)


Escriba un programa en Pascal que lea de la entrada estandar n enteros positivos, todos
 menores que 60 y produzca una gra ca de n barras horizontales formadas por asteriscos
 (similar a la que se muestra en el ejemplo). La k-esima barra debera tener tantos asteriscos
 como indique el k-esimo entero (de entre los n enteros ingresados). Su programa no necesita
 controlar que los enteros ingresados sean menores que 60 (asuma que as sera). Incluya
 mensajes de salida con etiquetas descriptivas para solicitar y exhibir los valores





n = int(input("Ingrese la cantidad de barras: "))

for i in range(n):
    valor = int(input(f"Ingrese el número positivo {i+1}: "))
    print("*" * valor)

# Ejercicio: Sumar n números que ingresa el usuario

n = int(input("Cuantos numeros va a ingresar"))
sumar=0
for i in range (1,n+1):
    num = int(input("Ingrese un numero:"))
    sumar=sumar+num

print(sumar)
# Ejercicio: Crear una pirámide de asteriscos

Mostrar una pirámide así, según un número n ingresado:

n = int(input("Cuanto quiere de la primaide"))
fila="*"
for i in range (1,n+1):
    print(f"{fila*i}")
    
   # Ejercicio: Mostrar la tabla de multiplicar de un número
 
    
n = int(input("Ingrese el numero de la tabla que desar ver:"))

for i in range (1,11):
    print(f" {n}  X {i} = {n*i}")
    
    
Mayor y menor valor
Objetivo: Pedir n números y mostrar cuál fue el mayor y cuál el menor.
   
n = int(input("ingrese n numeros:"))
num1 = int(input("ingrese el primer n"))

mayor=num1
menor=num1
for i in range(2,n+1):
    num = int(input(f"ingrese el {i} numeros:"))
    if num>mayor:
        mayor=num
    if num<menor:
        menor=num
print(f"el numero mayor es: {mayor}")
print(f"el numero menor  es: {menor}")
 """
"""crea un programa que imprima por consola todos los numeros comprendidos entre 10 y 55 incluidos pares y que no son el 16 ni multiplos de 3
for i in range(10,56):
    if i %2==0 and i%3 !=0 and i!=16:
        print(i)
4. 
*Escriba un programa en Pascal que lea de la entrada estandar tres numeros naturales a, b
 y n. 
 El programa debe exhibir en pantalla todos los multiplos de n que haya entre a y b.


a = int(input("Ingrese a:"))
b = int(input("Ingrese b:"))
n = int(input("Ingrese n"))

for i in range (a,b+1):
   if i%n==0:
      print(i)

 Escriba un programa en Pascal que lea de la entrada estandar un numero natural n //y
 despliegue en pantalla todos los divisores naturales de n.

n = int(input("Ingrese n:"))

for i in range(1,n+1):
    if n%i==0:
        print(i)
Escriba un programa en Pascal que lea de la entrada estandar un numero natural n. A
 continuacion, el programa debera leer n enteros y luego desplegar en pantalla el mayor y
 el menor de ellos. Incluya mensajes de salida con etiquetas descriptivas para solicitar y
 exhibir los valores

n = int(input("Ingrese la cantidad de números a ingresar: "))
num = int(input("Ingrese el primer número: "))
mayor = num
menor = num

for i in range(2, n + 1):
    num = int(input("Ingrese un número: "))
    if num > mayor:
        mayor = num
    if num < menor:
        menor = num

print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")


 Escriba un programa en Pascal que lea de la entrada estandar n enteros positivos, todos
 menores que 60 y produzca una gra ca de n barras horizontales formadas por asteriscos
 (similar a la que se muestra en el ejemplo). La k-esima barra debera tener tantos asteriscos
 como indique el k-esimo entero (de entre los n enteros ingresados). Su programa no necesita
 controlar que los enteros ingresados sean menores que 60 (asuma que as sera). Incluya
 mensajes de salida con etiquetas descriptivas para solicitar y exhibir los valores

num = int(input("Ingrese un valor para n:"))
asterisco="*"
resultado=""
for i in range (1,num+1):
    valor = int(input(f"Ingrese enteros positivos:"))
    resultado = resultado + (valor * asterisco) + "\n"  # Concateno la barra y un salto de línea


    

print(resultado) 
 Escriba un programa en Pascal que lea de la entrada estandar un caracter c y un natural n.
 El programa debe desplegar un triangulo de n lneas formado por el caracter c (similar al
 que se muestra en el ejemplo). La primera lnea debe tener n ocurrencias de c. La segunda
 lnea debe tener n-1 ocurrencias de c (y as sucesivamente). La ultima lnea debe tener
 1 ocurrencia de c. Incluya mensajes de salida con etiquetas descriptivas para solicitar y
 exhibir los valores.

c = input("Ingrese un caracter: ")
n = int(input("Ingrese un natural n: "))
resultado = ""

for i in range(n, 0, -1):
    resultado += c * i + "\n"  # en cada línea, i veces el caracter c

print(resultado)



Escriba un programa en Pascal que lea dos numeros naturales x, n de la entrada estandar
 y calcule la potencia de x elevado a la n. Para este ejercicio, solamente se permite utilizar
 las operaciones aritmeticas elementales de Pascal (+,-, *, /, DIV, MOD). Incluya mensajes
 de salida con etiquetas descriptivas para solicitar y exhibir los valores

x = int(input("Ingrese un natural x: "))
n = int(input("Ingrese un natural n: "))
potencia=1
for i in range(1,n+1):
    potencia = potencia*x


print(f"El resultado de elevar {x}a la {n} = {potencia}")

Considere la funcion f tal que f(x) = x2 18x+5, donde x es un valor entero en el entorno
 de m a n, siendo m y n dos enteros tales que m n.
 Escriba un programa en Pascal que lea los valores para m y n de la entrada estandar y
 despliegue en la salida estandar el valor maximo de f(x) para x en ese entorno. Incluya
 mensajes de salida con etiquetas descriptivas para solicitar y/o exhibir los valores
m = int(input("Ingrese el valor de m: "))
n = int(input("Ingrese el valor de n: "))

print("Resultados de f(x) = x^2 - 18x + 5:")

for x in range(m, n+1):
    fx = x**2 - 18*x + 5
    print(f"f({x}) = {fx}")
frutas = ['manzana', 'banana', 'pera']

for i, fruta in enumerate(frutas):
    print(i, fruta)
nombres = ['Ana', 'Luis']
edades = [25, 30]
for nombre, edad in zip(nombres, edades):
    print(nombre, edad)"""
