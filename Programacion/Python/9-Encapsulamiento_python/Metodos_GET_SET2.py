
# Los métodos de tipo GET nos permiten obtener los atributos de nuestra clase
# Los atributos de tipo set nos permiten modificar los atributos de nuestra clase



class Persona:
    def __init__(self, nombre, apellido, edad) -> None:
        self._nombre = nombre 
        self._apellido = apellido
        self._edad = edad


    # Generamos el metodo get de el atributo _nombre
    # Utilizamos un decorador, que modificará el comportamiento de nuestro método

    @property # Indicamos que este metodo recupera el atributo _nombre, encapsulando el atributo y solo podemos acceder a el a través del método
    def nombre(self):
        return self._nombre

    # Generamos el método GET para _nombre

    # Colocamos un decorador con el nombre de el atributo sin barra baja seguido de .setter

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self.apellido} {self.edad}')


persona1 = Persona('Ruben', 'Pedroche Ranz', 35)