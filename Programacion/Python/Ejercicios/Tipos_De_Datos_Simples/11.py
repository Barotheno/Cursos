"""
    Una panaderia vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
    Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa 
    debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
"""

precioBarraDePan = 3.49
panDiaAnterior = (precioBarraDePan / 100) * 60
barrasDiaAnterior = int(input("Por favor cuantas barras de el dia anterior se vendieron: "))

print(f'El precio habitual de una barra de pan es de {precioBarraDePan} €')
print(f'El descuento que se le hace por no ser fresca es de {panDiaAnterior} €')
print(f'El coste final serian {precioBarraDePan * barrasDiaAnterior}euros restando el descuento se queda a {panDiaAnterior * barrasDiaAnterior} €')