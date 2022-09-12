"""
    Las variables de clase, se asocian directamente con la clase en si misma y no con los objetos.
    Es decir, dicha variable se compartirá con los demás objetos creados a partir de la clase.

"""

class MiClase:

    # Creamos una variable de clase

    variables_clase = 'Valor variable clase'

    # Despues de establecer la variable clase, establecemos ya nuestro método __init__

    def __init__(self,variable_instancia) -> None:
        self.variable_deInstancia = variable_instancia

# Para acceder a la variable de clase:

print(MiClase.variables_clase)

miClase = MiClase('valor variable de instancia')