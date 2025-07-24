# Objetivo: Crear una función llamada saludar() que pida el nombre del usuario y lo salude.
"""def saludar():
    nombre = input("Ingrese su nombre: ")
    print("Hola, ¿cómo estás", nombre, "?")

saludar()


Ejercicio 2: Función que sume dos números
Objetivo: Crear una función sumar() que:

Pida dos números al usuario

Los sume

Muestre el resultado



def sumar(a,b):
    a  =int(input("ingrese un numero: "))
    b =int(input("ingrese un numero: "))
    print(f"la suma de {a} + {b} = {a+b}")


sumar(2,4)


Ejercicio 3: Función que diga si un número es par o impar

def espar():
    num = int(input("Ingrese un numero"))
    if num %2==0:
        print(f"el numero {num} es par")
    else:
        print(f"{num} no es PAR")

espar()


def es_mayor(edad):
     if edad>=18:
        return "es mayor"

print(es_mayor(20))  # Debería decir "Es mayor"



def agregar_elemento(lista):
    lista.append(4)
    print("Dentro:", lista)

mi_lista = [1, 2, 3]
agregar_elemento(mi_lista)
print("Fuera:", mi_lista)  # La lista cambia afuera: [1, 2, 3, 4]


def sumar(a,b):
    suma=a+b
print(sumar(3,4))

------------------------------------------------------------------------------------------------------------------
Descripción:
Crea una función llamada saludo que reciba un nombre como parámetro y muestre por pantalla:
Hola, <nombre>!

def saludo(nombre):
    print("hola ", nombre)


saludo("pedro")

Ejercicio 2: Función que suma dos números
Descripción:
Define una función sumar que reciba dos números y retorne su suma. Prueba llamarla e imprime el resultado.
def sumar(a,b):
    resultado= a+b
    return resultado

print( sumar(23 , 45))

Ejercicio 3: Función con valor por defecto
Descripción:
Haz una función potencia que reciba un número y un exponente, y devuelva el número elevado al exponente. El exponente debe tener un valor por defecto de 2 (cuadrado).
def potencia( num, exponente):
    pot= num**exponente
    return pot

print(potencia(2,3))

Ejercicio 4: Función que verifica si un número es par
Descripción:
Crea una función es_par que reciba un número y retorne True si es par y False si es impar.
def es_par(numero):
    espar=True
    if numero%2==0:
        print(f"{espar}")
    else:
        print(f"{not espar}")

es_par(1)

def potencia( num, exponente):
    pot= num**exponente
    return pot

potencia(2,3)


Ejercicio 5: Función que recibe una lista y devuelve la suma de sus elementos
Descripción:
Define una función sumar_lista que reciba una lista de números y devuelva la suma total.
puedo crera la lista afuera  y ahi se fija la funcion en el scope local no la enceuntra va afuera y esta ahi por eso la muesta si pongo la 
lista adentro : es lo mismo la ecnutra mas rapido en todo caso


def sumar_lista():
    lista=[1,2,3,4,5]
    resultado=0
    for numero in lista:
        resultado=resultado+numero
    return resultado
print(sumar_lista())

Ejercicio 6: Función con argumentos variables
Descripción:
Crea una función suma_todos que pueda recibir cualquier cantidad de números y devuelva la suma total.


def sumar_todos (*args):
    print("los argumentos recibidos son",args)
    return args


print(type(sumar_todos(3,4,6)))


Ejercicio 2: Sumar todos los números
Objetivo: Crear una función que sume todos los números que recibe y devuelva el resultado.

def sumnumeros(*args):
    resultado=0
    for argumentos in args:
        resultado= resultado+argumentos
        
    return resultado
print(sumnumeros(2,2,2))

Ejercicio 3: Contar argumentos recibidos
Objetivo: Crear una función que diga cuántos argumentos recibió.

def contarg(*args): 
    contador=0
    for i in args:
        contador+=1
    return contador


print(contarg(2,3,4,5,6,7,7))

"""
def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Martín", edad=30, ciudad="Montevideo")