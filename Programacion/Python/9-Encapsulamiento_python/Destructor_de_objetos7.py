# En ocasiones cuando creamos nuestros objetos, es necesario liberar recursos

from Encapsulamiento_de_todos_los_atributos4 import *

print(' Creacion Objetos '.center(100, '='))

persona1 = Persona('Pepito', 'Grillo', 56)

persona1.mostrar_detalle()

print(' Eliminacion de Objetos '.center(100,'='))

# Para eliminar un objeto utilizamos 'del'

del persona1

# Creamos el destructor en la clase persona

# Ahora vemos la informacion de el objeto eliminado