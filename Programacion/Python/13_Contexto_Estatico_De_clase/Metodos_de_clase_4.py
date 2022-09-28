

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

    # CREACION DE UN MÉTODO DE CLASE CON @classmethod

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

print(MiClase.variable_clase)

miClase = MiClase('Valor variable instancia')
print(miClase.variable_instancia)
print(miClase.variable_clase)