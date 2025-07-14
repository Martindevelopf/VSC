"""Determinar si un año es biciesto
un año es biciesto si se cumple alguna de las siguientes:

es multiplo de 4 pero no es multiplo de 100
multiplo de 400

no son bisiestos : 1900 1999 2003
son bisiestos : 1976, 2000, 2004




"""

print("ANO BISIESTO:")

anio = int(input("ingrese el año :"))

if anio <0:
    print("debes ingresar un numero positivo ")
elif anio %4 ==0 and anio%100 != 0:
    print("es un año bisiesto")
elif anio %400 ==0:
    print("es un año bisiesto")
else:
    print(" año  no bisiesto")
 