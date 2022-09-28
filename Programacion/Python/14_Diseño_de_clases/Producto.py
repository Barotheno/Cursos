class Producto:
    # Definimos nuestra variable de clase
    contador_productos = 0

    def __init__(self, nombre, precio) -> None:
        # Antes de asignar los atributos incrementamos la variable contador_productos
        Producto.contador_productos += 1
        self._id_producto = Producto.contador_productos

        self._nombre = nombre 
        self._precio = precio 

    @property
    def precio(self):
        return self._precio
        

    # Definimos el método STR para poder regresar una representación de este objeto utilizando un string

    def __str__(self) -> str:
        return f'Id Producto: {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio}'

# Debido a que esta clase la utilizaremos en otros métodos si pondremos lo siguiente

if __name__ == '__main__':
    producto1 = Producto('Camisa', 39)
    producto2 = Producto('Chaqueta', 109)

    print(producto1)
    print(producto2)
