
# Cuando no savemos la cantidad de argumentos que va a recibir la funcion anteponemos "*"

def listarNombres(*nombres):#De manera interna, python lo convierte en una tupla
    for nombre in nombres:
        print(nombre)
    
listarNombres('Juan','Ruben','Diana')