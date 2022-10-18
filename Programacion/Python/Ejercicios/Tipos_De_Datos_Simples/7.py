"""
    Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la "n" entre "m"
    de un cociente "c" y un resto "r"
"""

# Variables

n = 0
m = 0
c = 0
r = 0

# Cuerpo

print("\n\tResultado de un cociente y el resto de una división")

n = int(input("Introduzca el primero número: \n"))
m = int(input("Introduzca el segundo número: \n"))

c = n / m 
r = n % m 

print(f'La division de {n} entre {m} da un cociente de {c} y un resto {r}')

