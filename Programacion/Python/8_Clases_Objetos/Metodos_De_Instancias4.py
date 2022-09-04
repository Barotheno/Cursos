# Los métodos son el comportamiento que tendrán nuestros objetos

class Persona:
    def __init__(self, nombre, apellido, edad) -> None:
        self.nombre = nombre 
        self.apellido = apellido 
        self.edad = edad 

    # Creamos un método con una función
    # Agregamos self a todos los métodos de instancias
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')


# Llamamos a un método de nuestra clase

persona1 = Persona('Ruben', 'Pedroche Ranz', 35)
persona1.mostrar_detalle()