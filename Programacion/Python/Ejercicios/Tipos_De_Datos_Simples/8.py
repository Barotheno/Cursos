"""
    Escribir un programa que pregunte al usuario una cantidad a invertir,
    el interes anual y el número de años y muestre por pantalla el capital obtenido
    en la inversion
"""
# Variables
cantidadInvertir = 0
interesAnual = 0
interesAnualTotal = 0
años = 0
interesTotal = 0

# Cuerpo

print("\t\t\n[*] SIMULADOR DE INVERSIÓN [*]")

cantidadInvertir =  int(input("\t\nPor favor indique cuanto quiere invertir: "))
interesAnual =      int(input("\tCual es el interés anual: "))
años =              int(input("\tCuantos años quiere añadir al simulador: "))

interesAnualTotal = (cantidadInvertir / 100)  * interesAnual
total = (interesAnualTotal * años) + cantidadInvertir

print(f'\n\tEl total acumulado seria de {total}')
