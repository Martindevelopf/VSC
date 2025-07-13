def divide(a, b):
    return a % b == 0

def es_primo(numero):
    i = 2
    tope = int(numero ** 0.5)
    
    while i <= tope and not divide(numero, i): 
        i += 1

    return i > tope

print(es_primo(2)) #T
print(es_primo(9)) #F
print(es_primo(17)) #T
