"""Ejercicio 2: Calculadora básica
Crea un programa que solicite dos números y una operación matemática (+, -, *, /). 
Según la operación ingresada, 
realiza el cálculo correspondiente. Si el usuario ingresa una operación no válida, muestra un mensaje de error."""



print("CALCULADORA!!!!!!!!!!!!!!!")

num1 = int(input("ingrese el Primer numero:  "))
num2 = int(input("ingrese el Segundo numero:  "))
op = input("ingrese la operacion hacer: (+, -, *, /) ")


if op == "+":
    print(f"la suma de {num1} + {num2}= {num1+num2}")

elif op =="-":
        print(f"la resta de {num1} - {num2}= {num1-num2}")
elif op =="*":
        print(f"la multiplicacion de {num1} * {num2}= {num1*num2}")
elif op =="/":
        print(f"la division de {num1} / {num2}= {num1/num2}")
else:
       print("ERROR NO INGRESO LOS OPERADORES POSIBLES")

