class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre 
        self.edad = edad 

    # Definimos el método STR

    def __str__(self) -> str:
        # Regresar un string con los valores de los atributos de nuestra clase
        return f'Persona: {self.nombre} {self.edad}'

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo) -> None:
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self) -> str:
        return f'{super().__str__()} Sueldo: {self.sueldo}'

# Importamos las clases a nuestros nuevo archivo:
    # Cliente_Persona.py