puntuacion = int(input('Indique la nota de rendimiento: '))
dineroFijo = 2400

if puntuacion == 0.0:
    print(f'Solo obtuviste la nomina fija: {dineroFijo}')
elif puntuacion < 0.0 and puntuacion >= 0.4:
    total = dineroFijo * puntuacion
    print(f'Enhorabuena obtuviste {total} euros')
else:
    total = dineroFijo * puntuacion
    print(f'Eres meteorico, ganaste {total}')