# Una función recursiva es una función que se llama a si misma
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)
    
resultado = factorial(5)
print(factorial)