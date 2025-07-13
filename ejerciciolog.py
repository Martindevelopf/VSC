"""EscribaunprogramaenPascalque leade laentradaest´andardosenterosnyb, calcule
 yexhibalaparteenteradel logaritmodenenbaseb.Dichoresultadoesunenterokque
 cumplelosiguiente: bk<=n<bk+1.Elalgoritmosolopuederealizardivisionesysumas.
 Asumaquelosvalores ingresadoscumplenquen>0yb>1. Incluyamensajesdesalida
 conetiquetasdescriptivasparasolicitary/oexhibirlosvalores"""

n= int(input("ingrese un numero:"))
b= int(input("ingrese la base:"))

k=0

while n >=b:
    n = n //b
    k +=1

print("El valor entero del logaritmo es:", k)

