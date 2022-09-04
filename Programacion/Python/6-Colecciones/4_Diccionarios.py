"""
    Los diccionarios estar organizados de la siguiente manera:

        "OOP"(llave):Valor asocionado
"""

diccionario = {
    'IDE':'Integrated Developmen Environment',
    'OOP':'Object Oriented Programing',
    'DBMS':'Database Managment System'
}

print(diccionario)

#largo
print(len(diccionario))

# acceder a un elemento (key)
print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('OOP'))

# Modificando elementos
diccionario['IDE'] = 'Hola que tal estas'
print(diccionario['IDE'])

# Recorrer los elementos de un diccionario

for termino in diccionario:
    print(termino)

# Recorrer un diccionario con IDE y su valor

for terminos, valor in diccionario.items():
    print(termino, valor)

# Para solo recorrer las llaves

for termino in diccionario.keys():
    print(termino)

# Solo recuperar los valores

for valor in diccionario.values():
    print(valor)

# Comprobar existencia de algun elemento

print('IDE' in diccionario)

# agregar un elemento

diccionario['PK'] = 'Primary Key'
print(diccionario)

# remover un elemento

diccionario.pop('PK')
print(diccionario)

# limpiar diccionario

diccionario.clear()
print(diccionario)

# eliminar por completo

del diccionario
print(diccionario)