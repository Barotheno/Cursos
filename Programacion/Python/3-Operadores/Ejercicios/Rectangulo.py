"""
    Instrucciones de la tarea:

        * Se soliita calcular el área y el perímetro de un Rectángulo, para ello debemos crear las siguientes variables:

            alto (int)
            ancho (int)

    El usuario debe proporcionar los valores de largo y ancho, y despues se debe imprimir el resultado en el siguiente formato

"""


from operator import mod


print('\n\t[*] Calculo Area y Perimetro de un rectángulo [*]')

alto = int(input('Proporciona el alto: '))
ancho = int(input('Proporciona el ancho: '))

print('... Perfecto estoy calculando un micro segundo....')

area = ancho * alto
perimetro = ancho + ancho + alto + alto 

print(f'El área calculado es: {area} y tiene un perímetro de: {perimetro}')


