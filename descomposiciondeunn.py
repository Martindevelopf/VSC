"""Todo n´umero natural positivo num tiene una descomposici´on ´ unica de la forma num =
 2n ×val, donde val es un n´umero natural impar y n >= 0. Escriba un programa en Pascal
 que lea de la entrada est´ andar un entero positivo num, calcule y exhiba los correspondientes
 valores de val y n. Incluya mensajes de salida con etiquetas descriptivas para solicitar los
 valores.
"""

num = int(input("INGRESE UN NUMERO: "))
n=0
val=0
while num%2==0:
    num = num//2
    n+=1
val=num
print(f"El número se puede escribir como 2 elevado a{n} × {val}")

   
   
