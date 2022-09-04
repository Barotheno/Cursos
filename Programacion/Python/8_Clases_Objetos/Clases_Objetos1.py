# La sintaxis básica es:

class Persona:
    # Para agregar caracteristicas o atributos necesitamos el método init, es un método inicializador (constructor)
    # El parámetro por defecto el self
    def __init__(self):
        self.nombre = 'Juan'
        self.apellido = 'Perez'
        self.edad = 28


# Preguntamos de que tipo es el tipo persona
print(type(Persona))

# Para crear un objeto sobre una clase

persona1 = Persona()
# Para acceder a un atributo lo hacemos con nombre_objeto.atributo
print(persona1.nombre) 
print(persona1.nombre, persona1.apellido)

