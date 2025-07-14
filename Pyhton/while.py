"""¿Qué es un while?
Un bucle while repite una acción mientras una condición sea verdadera.

📌 Se traduce como:
"Mientras esto sea cierto, seguí haciendo esto."

while condición:
    # código que se repite
# Ejemplo 1: contar del 1 al 5

contador=10

while contador>10:
    contador-=3
print(contador)
Contar del 1 al 10

contador=1
while contador <10:
    print(contador)
    contador +=1

     Suma de números hasta que se ingrese 0

suma=0
numero = int(input("ingrese un numero:"))
while  numero !=0:
  suma +=numero
  numero= int(input("Ingresá otro número (0 para terminar): "))

print(suma)
3. 🧱 Leer números hasta que aparezcan 3 negativos

numero = int(input("ingrese un numero:"))
contadornegativos=0
while contadornegativos !=3:
    numero = int(input("ingrese un numero:"))
    if numero<0:
        contadornegativos+=1

print("Se ingresaron 3 números negativos. Fin del programa.")

 Se desea implementar un programa que calcule el saldo final de una cuenta. Suponga que
 los datos son le´ıdos de la entrada est´ andar y que constan de renglones. El primer renglon
 contiene el saldo inicial de la cuenta. Los siguientes renglones contienen una letra y un valor
 real para indicar las transacciones (posiblemente ninguna). La letra puede ser la D para
 efectuar un dep´ osito o la R para efectuar un retiro. El ´ultimo rengl´ on contiene ´ unicamente la
 letra X. Escriba un programa en Pascal que determine el saldo exacto de la cuenta despu´ es
 de procesar las transacciones. Incluya mensajes de salida con etiquetas descriptivas para
 exhibir los valores.



saldo_inicial = float(input("Ingrese su saldo inicial: "))

while True:
    caracter = input("Ingrese D para depósito, R para retiro, o X para salir: ")

    if caracter == "X":
        break  # Salimos del bucle

    elif caracter == "D":
        monto = float(input("Ingrese el monto a depositar: "))
        saldo_inicial += monto

    elif caracter == "R":
        monto = float(input("Ingrese el monto a retirar: "))
        saldo_inicial -= monto

    else:
        print("Opción inválida. Por favor ingrese D, R o X.")

print(f"\nSu saldo final es: {saldo_inicial}")


Dado un fragmento de texto que debe ser le´ ıdo de la entrada est´ andar, todo en una l´ ınea,
 y terminado por el caracter $ (centinela), escriba un programa en Pascal que determine
 y exhiba las consonantes y vocales que aparecen duplicadas en forma contigua. Asuma
 que todas las letras ingresadas son min´ usculas. Incluya mensajes de salida con etiquetas
 descriptivas para solicitar y exhibir los valores 

 
  
   Escriba un programa en Pascal que determine si un n´ umero n es primo o no, siendo n
 un entero positivo le´ ıdo de la entrada est´andar. Exhiba un mensaje de salida indicando el
 resultado. Incluya mensajes de salida con etiquetas descriptivas para solicitar los valores.
 p´ ag. 3 de 5
Ejemplo
 Ingrese un entero positivo: 3
 Es primo 

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

numero = int(input("Ingrese un entero positivo: ")) 

esprimo = True  # Inicialmente suponemos que es primo

for i in range(2, numero):
    if numero % i == 0:
        esprimo = False
        break

if esprimo:
    print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} NO es primo.")
    
    
    Sumar números hasta que se ingrese un cero

suma = 0
numero = int(input("Ingrese un número (0 para terminar): "))

while numero != 0:
    suma += numero
    numero = int(input("Ingrese otro número (0 para terminar): "))

print(f"La suma total de los números ingresados es: {suma}")
. Se desea implementar un programa que realice las funciones de una calculadora simple. Los
 datos de entrada son una secuencia de enteros sin signo y los operadores +, *, / y-, seguida
 de un signo =. Cada entero de la entrada est´a seguido por un operador salvo el ´ ultimo que
 est´ a seguido por el s´ımbolo =. Los operadores se aplican en el orden en que aparecen sin
 importar la precedencia. Si bien se ingresa el operador de la divisi´ on con el s´ ımbolo /, el
 comportamiento debe ser el de DIV. Asuma que se ingresa al menos un n´umero.

print("Calculadora simple (usa +, -, *, / y termina con =)")

resultado = int(input("Ingrese un número: "))  # primer número fuera del ciclo

while True:
    operador = input("Ingrese un operador (+, -, *, /, =): ")

    if operador == "=":
        break

    numero = int(input("Ingrese otro número: "))

    if operador == "+":
        resultado += numero
    elif operador == "-":
        resultado -= numero
    elif operador == "*":
        resultado *= numero
    elif operador == "/":
        if numero == 0:
            print("Error: División por cero")
            break
        resultado //= numero  # división entera
    else:
        print("Operador no válido.")
        break

print("Resultado final:", resultado)

Contar cuántas vocales tiene una palabra ingresada por el usuario.

palabra = input("ingrese una palabra:")
cantvoc=0
for i in palabra:
    if i=="a" or i=="e" or i=="i" or i=="u" or i=="o"  :
        cantvoc +=1

print(f" la palabra {palabra} tiene {cantvoc}")

Pedir 5 números y decir cuál es el mayor. """
mayor=None
for i in range(1,6):
    numero = int(input("ingrese una palabra:"))
    if mayor is None or numero > mayor:
        mayor = numero

print(mayor)