# 1 = Iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3

for i in range(300):
    if i % 3:
        print(f'Divisible entre 3: {i}')
    else:
        print(f'No divisible: {i}')


# 2 = Crear un rango de numeros de 2 a 6, e imprimir

for a in range(2,6):
    print(f'Numeros: {a}')

# 3 = Crear un rango de números de 3 a 10, pero con incremento de 2 en 2, en lugar de 1 en 1

for c in range(3,10,2):
    print(c)