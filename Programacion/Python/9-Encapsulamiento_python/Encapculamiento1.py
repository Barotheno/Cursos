
# Cuando ponemos un guión bajo en un atributo (_nombre) estamos advirtiendo que solo puede ser modificado dentro de la misma clase

class Persona:
    def __init__(self, nombre, apellido, edad) -> None:
        self._nombre = nombre 
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self.apellido} {self.edad}')

persona1 = Persona('Ruben', 'Pedroche Ranz', 35)