from Producto import *

class Orden:
    contador_ordenes = 0

    def __init__(self, productos) -> None:
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes

        self._productos = list(productos)#hacemos una conversion con list() para asegurarnos que es una lista

    # Agregamos un método para agregar un producto de manera independiente

    def agregar_producto(self, producto):
        self._productos.append(producto)# con appen agregamos a nuestra lista

    # Definimos un método para calcular el total, sumando todos los precios que contengan nuestra orden

    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total 

    # Método para convertir a un string

    def __str__(self) -> str:
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__() + '|'

        return f'Orden: {self._id_orden}, Productos: {productos_str}'

if __name__ == '__main__':
    producto1 = Producto('Camisa', 39)
    producto2 = Producto('Chaqueta', 109)

