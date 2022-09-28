valor = int(input('Proporcione un valor de calificacion entre 0 y 10: '))

if 9 == valor <= 10:
    print('A')
elif 8 == valor <= 9:
    print('B')
elif 7 == valor <= 8:
    print('C')
elif 6 == valor <= 7:
    print('D')
elif valor <= 6:
    print('F')
else:
    print('La nota supera el 10 y es erronea')