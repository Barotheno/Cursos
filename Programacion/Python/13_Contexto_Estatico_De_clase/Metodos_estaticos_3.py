"""También podemos tener métodos de clase

        @ Dos tipos de métodos que se pueden asociar con una clase:

            * Metodos estáticos: Se asocian con la clase en si misma igual que una variable de clase, no puede acceder
                                 a las variables de instancia.
            * Métodos de clase:  Si recibe un un contexto de clase





"""

from mimetypes import init


class MiClase:

    variable_clase = 'Valor variable clase'

    def __init__(self, variable_instancia) -> None:
        self.variable_instancia = variable_instancia

    # CREACION DE METODO ESTATICO CON EL DECORADOR: @staticmethod

    @staticmethod
    def metodo_estatico():
        # Acceder a la variable de clase
        print(MiClase.variable_clase)

print(MiClase.variable_clase)

miClase = MiClase('Valor variable instancia')
print(miClase.variable_instancia)
print(miClase.variable_clase)