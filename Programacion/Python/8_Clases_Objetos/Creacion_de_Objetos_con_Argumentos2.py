# Lo común es que pasemos valores al momento de crear nuestros objetos. Para ello agregaremos parámetros a nuestro metodo init.

class Persona:
    # Asignamos parámetros:
    def __init__(self, nombre, apellido, edad) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

# Ahora al crear un objeto, debemos introducir los parámetros

persona1 = Persona('Ruben', 'Pedroche', 35)

print(persona1.nombre)
