from mimetypes import init


class MiClase:

    variable_clase = 'Valor variable clase'

    def __init__(self, variable_instancia) -> None:
        self.variable_instancia = variable_instancia

print(MiClase.variable_clase)

miClase = MiClase('Valor variable instancia')
print(miClase.variable_instancia)
print(miClase.variable_clase)

# Asociar una nueva variable a nuestra clase

MiClase.varia_clase2 = 'Valor variable clase 2'