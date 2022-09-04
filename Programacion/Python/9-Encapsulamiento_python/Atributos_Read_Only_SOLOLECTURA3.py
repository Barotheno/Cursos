



class Persona:
    def __init__(self, nombre, apellido, edad) -> None:
        self._nombre = nombre 
        self._apellido = apellido
        self._edad = edad




    @property 
    def nombre(self):
        return self._nombre

# Si queremos que la variable _nombre sea solo de lectura debemos quitar el metodo set de abajo.

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self.apellido} {self.edad}')


persona1 = Persona('Ruben', 'Pedroche Ranz', 35)