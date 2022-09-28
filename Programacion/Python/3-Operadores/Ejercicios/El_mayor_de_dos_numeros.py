"""
    Intrucciones de tareas:

    Solicitar al usuario dos valores, y determinar cual número es el mayor
    Solicitar al usuario dos valores:

    numero 1
    numero 2

    Debe imprimir el mayor de los dos números:

    Salida:

        Proporciona el numero1:
        Proporciona el numero2:
        El número mayor es:<numeroMayor>

"""

numero1 = int(input('Proporciona el numero1: '))
numero2 = int(input('Proporciona el numero2: '))

if numero1 > numero2:
    print(f'El numero mayor es: {numero1}')
elif numero1 == numero2:
    print(f'El numero mayor es: Son iguales')
else:
    print(f'El número mayor es: {numero2}')