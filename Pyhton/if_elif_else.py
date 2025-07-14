""" IF en Pyhton: 
if condición:
    instruccion
    
 puede ser solo asi o tener un else
 elif:

 else:
    instruccion 
    
    
    
   

edad = int(input("Ingrese su edad"))

if edad > 18:
    print("ES MAYOR")
else:
    print("ES MENOR")

print(type(edad))




edad = int(input("Ingrese su edad: "))

if edad <= 18:
   print("eres menor")
elif edad > 18 and edad < 40:
   print("puedes entrar a la disco pero no puedes tomar whisky")
else:
   print("puedes entrar a la disco")
"""
"""
# ejercicio 1 saber si un numeor es positivo
numero = int(input("Ingrese un numero: "))

if numero > 0:
    print(f" el {numero} es positivo. ")"""

#   ejercicio 2 rangos de edades:
""" Ejercicio 2: Clasificación por edad
# Pide al usuario su edad
edad = int(input("Ingresa tu edad: "))

# Escribe condiciones usando if y elif
👉 Objetivo:

Si tiene menos de 13: imprimir "Niño"

Si tiene entre 13 y 17: imprimir "Adolescente"

Si tiene entre 18 y 64: imprimir "Adulto"

No uses else aún, solo if y elif  

edad = int(input("Ingrese un numero: "))

if edad <13:
   print("NIÑO")
elif edad <18:
   print("adolecente")
elif edad >=18 and edad <65:
   print("adulto")"""
""" Ejercicio 3: Verificar tipo de número

# Pide un número al usuario
numero = int(input("Ingresa un número: "))

# Estructura completa: if, elif, else
👉 Objetivo:

Si el número es mayor que 0: imprimir "Positivo"

Si el número es igual a 0: imprimir "Cero"

Si el número es menor que 0: imprimir "Negativo


numero = int(input("Ingresa un número: "))

if numero >0 :
    print("POSITIVO")
elif numero == 0:
    print("CERO")
else:
   print("NEGATIVO")"""


"""4. Extra: Clasificación de nota
python
# Pide una nota del 0 al 100
nota = int(input("Ingresa tu nota (0-100): "))

# Evalúa la nota con if, elif y else
👉 Objetivo:

90–100: "Sobresaliente"

70–89: "Aprobado"

60–69: "Apenas aprobado"

Menos de 60: "Reprobado"""

nota = int(input("Ingresa tu nota (0-100): "))

if nota>89:
    print("sobresaliente")
elif nota >69:
        print("Aprobado")
elif nota> 59:
      print("apenas aprobado")
else:
      print("REPROBADO")
 
prueba = not 4> 5

print(prueba)