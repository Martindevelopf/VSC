import math


PI = 3.14  #creo dos constantes una para pi otra para gravedad
G = 9.8



l = float  (input("ingrese longitud del pendulo:"))

t = 2 * PI * math.sqrt(l/G)

print(f"el periodo del pendulo es : {t}")
