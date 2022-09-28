print('\n\tVeremos si tu número está dentro de nuestro rango.\nNuestro rango está entre 1 y 10')

valor = int(input('\nIntroduce tu número entero: '))

valorMaximo = 10

if valor > valorMaximo:
    print(f'EL valor {valor} esta fuera del rango')
else:
    print(f'El valor {valor} esta dentro de el rango')