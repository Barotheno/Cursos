from Sobreescritura_del_metodo_STR_2 import *


# Si creamos un objeto y lo mandamos a imprimir, nos devolvera el lugar de la meoria en el que esta.
# Lo común esque nos emvíe una representacion en texto de cada uno de los objetos al momento de imprimirlos
# Para eso sobrescribimos un método en la clase padre que se conoce como STR
# Este método lo hacemos en el archivo de clase Persona
persona1 = Persona('Juan', 28)
print(persona1)

empleado1 = Empleado('Karla', 30, 5000)
print(empleado1)