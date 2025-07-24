""" ¿Qué es una lista?
Una lista es una colección de elementos ordenados y modificables. Puede tener números, textos, o mezclas de todo.

📌 Se define con corchetes [].
mi_lista = [1, 2, 3, 4, 5]
nombres = ["Ana", "Luis", "María"]
mezcla = [1, "hola", True, 3.14]




ACCEDER A LOS ELEMENTOS DE UNA LISTA:
arranca en el 0
print(mi_lista[0])
print(mi_lista[-1])

print(mi_lista[0])  # 1
print(nombres[2])   # "María"


cambiar un valor de una lista

mi_lista[1] = 10
print(mi_lista)  # [1, 10, 3, 4, 5]
# si pones un indice que no esta tira error : IndexError: list assignment index out of range
# for num in mi_lista:
#     print(num)
agregar un elemento a una lista al final es con append

mi_lista.append(6)  # Agrega al final
agregar un elemento a una posicion especifica 

mi_lista.insert(1, 99)  # Inserta 99 en la posición 1

ELIMINACION DE ELEMEMOTOS
mi_lista.remove(3)     # Elimina el número 3
mi_lista.pop()         # Elimina el último elemento
mi_lista.pop(0)        # Elimina el de la posición 0

VER EL LARGO DE UNA LSITA ES CON LEN(LISTA
print(len(mi_lista))  # Muestra la cantidad de elementos

EJERCICIOS BASICOS
# 1. Crear lista con 5 nombres
lista_nombres = ["Pedro", "Anibal", "Jose", "Joaquin", "Laura"]

# 2. Imprimir el segundo nombre
print(lista_nombres[1])

# 3. Cambiar el tercero por otro
lista_nombres[2] = "Raúl"

# 4. Agregar un nombre al final
lista_nombres.append("Concha")

# 5. Recorrer la lista
for nombre in lista_nombres:
    print(nombre, end=" ")
    
    
    
    # 1. Crear una lista con 4 frutas
# 2. Imprimir cada fruta en una línea

lista_frutas =["BANANA", "MANZANA", "SANDIA","PERA"]

for fruta in lista_frutas:
     print(fruta, end=" ")

     
# Dada una lista de animales, imprime el primero y el último
animales = ["perro", "gato", "loro", "pez"]

animales = ["perro", "gato", "loro", "pez"]

print(animales[0], animales[-1])


# Cambia el segundo nombre por "Carlos"
nombres = ["Ana", "Luis", "María"]

nombres = ["Ana", "Luis", "María"]

nombres[1]= "Carlos"


# Crea una lista vacía y agrega 3 colores
# Luego elimina uno y muestra el resultado final

lista=[]
lista.append("azul")
lista.append("verde")
lista.append("amarillo")

print(lista)
lista.pop()
print(lista)

Ejercicio 5: Sumar todos los números de una lista
Objetivo: Usar un bucle for para sumar elementos.
numeros = [1, 2, 3, 4, 5]

# Suma todos los números sin usar sum()


numeros = [1, 2, 3, 4, 5]
resultado=0
for numero in numeros:
    resultado +=numero

print(resultado)

Ejercicio 6: Buscar un valor
Objetivo: Verificar si un nombre está en una lista.

amigos = ["Lucas", "Sofía", "Martín", "Julia"]

# Preguntá al usuario un nombre y decí si está en la lista

amigos = ["Lucas", "Sofía", "Martín", "Julia"]
amigo=input("Ingrese un amigo:")

if amigo in amigos:
        print("esta en la lista")
else:
        print("no esta")
        
       

# Lista de números
numeros = [1, 2, 2, 3, 4, 2, 5]

# Contar cuántas veces aparece el número 2
cantidad = numeros.count(5)

# Mostrar el resultado
print(f"El número 5 aparece {cantidad} veces en la lista.")
 
numeros = [1, 2, 2, 3, 4, 2, 5]
contador=0
for numero in numeros:
    if numero==2:
        contador+=1

print(f"la cantaidad de numeros 5 en la lista es : {contador}")


 Nivel 1: Fundamentos
1. Crear una lista con 5 números y mostrarla



numeros = [4, "hola", True, 9, 3]
print(numeros)

print(type(numeros[2]))
2. Agregar un elemento al final de la lista
numeros = [4, 3, 2, 9, 3]

numeros.append(6)
print(numeros)

3. Insertar un número en la posición 2



numeros = [4, 3, 2, 9, 3]
numeros.insert(2,11)
print(numeros)# al usar insert,es posiuticon que quiero isnertar, ahi desplaza el resto para adelante

# al agregar con los corchetes sobreescribe el valor
numeros[2]=10
print(numeros)

4. Eliminar el último elemento


numeros = [4, 3, 2, 9, 3]
numeros.pop() # borra el utimo , importante meter las () si no no hace nada
print(numeros)

5. Eliminar el número 9 de la lista
numeros = [4, 3, 2, 9, 3,9,9,9]
numeros.remove(9)
print(numeros)
# borra el primer 9 que encuentra no todos 

6. Ordenar la lista de menor a mayor
numeros = [4, 3, 2, 9, 3]

numeros.sort() #con el sort lo ordena de menor a mayor
print(numeros)
letras= ["h", "a", "b", "o"]
letras.sort() #con el sort lo ordena de menor a mayor incluso letras seugn asccii
print(letras)
🔹 Nivel 2: Acceso y lógica
7. Imprimir el primer y último elemento de una lista

numeros = [4, 3, 2, 9, 3]
print(f"el primer elemento de la lista numeros es {numeros[0]}")
print(f"el ultimo elemento de la lista numeros es {numeros[-1]}")

# 8. Mostrar solo los números mayores a 5
una forma es asi directo con el for, si quiero que aparecsancann en la misma
linea uso el , end " "
for num in numeros:
    if num >5:
        print(num)"""

numeros = [4, 3, 2, 9, 3,6,7]
mayores =[]
for num in numeros:
    if num >5:
        mayores.append(num)
print(mayores)