# No es modificable

# Definir una tupla
frutas = ('Naranja','Platano','Guayaba')

# Saber el largo de una tupla
print(len(frutas))
# Acceder a un elemento
print(frutas[0])
# Navegacion inversa
print(frutas[-1])
# Acceder a un rango de valores
print(frutas[0:2])
# Iterar tupla
for fruta in frutas:
    print(fruta, end=' ')# end para que no alla saltos de linea
else:
    print('Se acabó')

# Comvertir tupla a lista
frutasListas = list(frutas)
frutasListas[0] = 'Pera'
# Convertir lista a tupla
frutas = tuple(frutasListas)
print(frutas)
# Eliminar tupla
del frutas