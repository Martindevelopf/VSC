"""Crea un programa que muestre un menú con estas opciones:

markdown
Kopieren
Bearbeiten
1. Saludar
2. Sumar dos números
3. Mostrar si un número es par o impar
4. Salir





opcion = int(input("Ingrese una opción : "))

match opcion:
    case 1:
        print("hola salame!")
    
    case 2:
       num1 = int(input("Ingrese el primer numero: "))
       num2= int( input("Ingrese el segundo numero: "))
       print(f"la suma de {num1} y {num2} = {num1+num2}")

    case 3:
       numero= int( input("Ingrese un numero para saber si es par: "))

       if numero %2 ==0:
           print(f"el numero {numero } es par")
       else:
           print( f" el numero {numero}  no es par")

    case 4:
      print("fin del programa")
    
    case _:
       print("no ingreso un numero del 1 al 4 no sea imbecil")"""

"""Todo n´umero natural positivo num tiene una descomposici´on ´ unica de la forma num =
 2n ×val, donde val es un n´umero natural impar y n >= 0. Escriba un programa en Pascal
 que lea de la entrada est´ andar un entero positivo num, calcule y exhiba los correspondientes
 valores de val y n. Incluya mensajes de salida con etiquetas descriptivas para solicitar los
 valores.
"""

numero= int( input("Ingrese un numero para saber si es par: "))
val=0
contador=0

while numero%2==0:
    numero= numero//2
    contador+=1

val= numero
print(f"El número se puede escribir como 2 elevado a{numero} × {val}")
