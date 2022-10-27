"""
    Una jugueteria tiene mucho éxito en dos de sus productos: payasos y muñecas. 
    Suele hacer venta por correo y la empresa de logística les cobra por peso de 
    cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán 
    en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y 
    muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
"""

# Variables

pesoPayaso = 112
pesoMuneca = 75
payasos = 0
munecas = 0

print("\t\t[*] PESO DE PAYASOS Y MUÑECAS [*]")
payasos = int(input("\tPor favor indique cuantos payasos quiere enviar: "))
munecas = int(input("\tPor favor indique cuantas muñecas quiere enviar: "))
pesoTotal = (payasos * pesoPayaso) + (munecas * pesoMuneca)
print(f'\tEl peso total del paquete es de {pesoTotal} gramos')
