

"""Ejercicio 1 – Leer números hasta que se ingrese -1 (sin listas)
Este ejercicio te entrena en leer valores usando while. mostrar cantidad de numeros ingresados

num=int(input("INGRESE UN NUMERO:"))
contador=0
while num !=-1:
    contador +=1
    num=int(input("INGRESE UN NUMERO:"))

print(f"la cantidad de numeros ingresados es {contador}")"""


"""Multiplicar todos los valores ingresados (sin listas)
Vamos a multiplicar todos los números ingresados hasta que pongas -1."""

num=int(input("INGRESE UN NUMERO:"))
resultado=1

while num !=-1:
    resultado= resultado*num
    num=int(input("INGRESE UN NUMERO:"))

print(f"el resultado de multplicar todo es :", resultado)

print("Polinomio: ax + b")

a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))
x = float(input("Ingrese el valor de x: "))

resultado = a * x + b
print("El valor del polinomio es:", resultado)
