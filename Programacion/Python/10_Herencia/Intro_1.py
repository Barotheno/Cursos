# Podemos crear clases hijas de una clase Padre que herede sus mismos comportamientos
# Creamos una clase persona

class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre 
        self.edad = edad 

# Definimos una clase hija con el nombre de empleado:
# Entre parentesis indicamos de quien queremos heredad, ( forma simple)
class Empleado(Persona):
    # Es necesario inicializar correctamente los atributos de la clase padre
    def __init__(self, nombre, edad, sueldo) -> None:
        # Mandamos llamar el constructor super
        super().__init__(nombre, edad)
        self.sueldo = sueldo 

empleado1 = Empleado('Ruben', 35, '1240 Euros')
print(empleado1.nombre)