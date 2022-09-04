class Persona:
    
    def __init__(self, nombre, apellido, edad) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


persona1 = Persona('Ruben', 'Pedroche', 35)

print(persona1.nombre)

# Modificamos atributos de un objeto:

persona1.nombre = 'Juan Carlos'
persona1.apellido = 'Juarez'
persona1.edad = 67

