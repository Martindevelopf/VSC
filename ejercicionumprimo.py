num = int(input("INGRESE UN NUMERO: "))
esprimo = True

if num <= 1:
    esprimo = False
else:
    for i in range(2, num):
        if num % i == 0:
            esprimo = False
            break

if esprimo:
    print(f"El número {num} es primo")
else:
    print(f"El número {num} no es primo")
