
# Ahora agregamos todos los atributos con los metodos Get y Set



class Persona:
    def __init__(self, nombre, apellido, edad) -> None:
        self._nombre = nombre 
        self._apellido = apellido
        self._edad = edad



    @property 
    def nombre(self):
        return self._nombre


    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter 
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

    # Metodo destructor

    def __del__(self):
        print(f'Persona: {self.nombre} {self.apellido}')

if __name__ == '__main__':


    persona1 = Persona('Ruben', 'Pedroche Ranz', 35)
    persona1.mostrar_detalle()