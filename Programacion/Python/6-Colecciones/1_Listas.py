# Cada lista tiene un indice, empieza de 0,1,2,3,4 infinito
# Una lista es modificable
# Creamos una lista
nombres = ["Juan","Karla","Ricardo","María"]
# Imprimimos la lista
print(nombres)
# Acceder a los elementos de manera individual
print(nombres[0])
print(nombres[1])
# Acedder a los elementos de manera inversa
print(nombres[-1])
print(nombres[-2])
# Para recuperar un rango
print(nombres[0:2])
# Ir del inicio de la lista al índice (sin incluirlo)
print(nombres[ :3])
# Desde el indice indicado hasta el final de la lista
print(nombres[1:])
# Cambiar un valor
nombres[3] = "Ivone"
print(nombres)
# Iterar lista
for nombre in nombres:
    print(nombre)
else:
    print("Se terminó la lista")

# Preguntar cuantos elementos tiene

print(len(nombres))

# Agregar un nuevo elemento
nombres.append("Lorenzo")
print(nombres)
# Insertar un elemento en un indice especifico
nombres.insert(1,"Octavio")
print(nombres)
# Eliminar un elemento de la lista
nombres.remove('Octavio')
print(nombres)
# Eliminar ultimo valor agregado
nombres.pop()
print(nombres)
# Eliminar un elemento en un indice indicado
del nombres[0]
print(nombres)
# Limpiar todos los elementos de la lista
nombres.clear()
print(nombres)
# Eliminar lista por completo
del nombres
print(nombres)