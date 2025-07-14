#esto es un comentario se hace con shift 3
#creacion de variables desde cero en pyhton
"""
Esto parece un comentario multilínea,
pero en realidad es un string multilínea

x = 5              # variable entera (int)
nombre = "Ana"     # variable texto (str)
precio = 0.0     # variable decimal (float)
es_mayor = True    # variable booleana (bool)
print(precio)

#10altura =base=area =float()

# creacion de variables tipo INT , INTEGER
edad = 25
cantidad = -10

# creacion de variables tipo REALES DECIMALES , FLOAT
precio = 3.14
altura = 1.75

# creacion de variables tipo STRINGS , STR
nombre = "Ana"
mensaje = 'Hola mundo'

# creacion de variables tipo STRINGS , STR
activo = True
terminado = False


a = 6
b = "hola"
#c= a+b
print(type(b))"""

"""1. Crear variables de tipo int (enteros)
Crea una variable llamada edad y asígnale tu edad (por ejemplo, 25).

Luego, crea una variable llamada numero_de_hijos y asigna un número de hijos (por ejemplo, 2).

Imprime ambos valores con un mensaje claro.
numer_de_hijos = 0
print( "mi edad es ", edad , "y mi numero de hijos es :", numer_de_hijos)
print(f"Mi edad es {edad} y mi número de hijos es: {numer_de_hijos}")

nombrepadre = "pepe"
edad_padre = 58

print(f"el nombre de mi padre es : {nombrepadre} y su edad es :{edad_padre}")
a = 4
b = 6.0
c = a+b

#CONSTANTE = 40  asi se representa una constante en payton porque no existens las constantes esto es una convencion
print((c))"""

#creacion de una varible tipo int
"""
mi_entero = 10
print(mi_entero)
#regunta para ti: ¿Puedes cambiar el valor de mi_entero a otro número entero y volver a imprimirlo? se actualiza la variable a 11
# si no pongo un nuevo print muesta 10



mi_entero =11 
print(mi_entero)
"""
"""

#CREACION DE UN FLOAT

mi_decimal= 3.14
print(mi_decimal)
mi_decimal = 4.15
print(mi_decimal)
#Pregunta para ti: ¿Qué pasa si intentas hacer una operación de suma entre un int y un float? ¿Qué tipo de variable obtienes como resultado?
mi_entero = 10
suma = mi_decimal + mi_entero

print(f"la suma de {mi_decimal}+ {mi_entero}= {suma} y el tipo es {type(suma)}")
# si sumo un float a un entero me lo deja float

#CREACION DE UN STRING STR

mi_decimal= 3.14
mi_entero =11 
mi_nombre = "Martin" # se puede usar "" o tambien comillas simple ' con alt 39   
# str + numeeral al lado del enter comenta toda esa linea 
print(mi_nombre)
mi_apellido = " fernandez "

print(" mi nombre y apellido es", mi_nombre + mi_apellido)
print(f" mi nombre y apellido es:  {mi_nombre + mi_apellido}")

print(f" sumo un int con un str:  {mi_nombre + mi_decimal}")

#no puedo me tira un error de tipo que no puedo concatenar un int con un str con float es igual TypeError: can only concatenate str (not "float") to str
# Pregunta para ti: ¿Qué sucede si intentas concatenar (sumar) dos cadenas de texto? ¿Puedes hacer esto con otras variables como int o float?

#CREACION DE UN STRING BOOLEANO 

es_Mayor = True
mi_decimal= 3.14
mi_entero =10 

resultado = mi_decimal > mi_entero
print(resultado)

 
prendido = True
apagado = False

print(f" si aplico la negacion a prendido da {not prendido}")
"""
#  Ejercicio 5: Sumar los números del 1 al 4
