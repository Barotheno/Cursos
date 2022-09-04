"""Un "set" no mantiene un orden y tampoco permite elementos duplicados, no es posible modificar los elementos pero si eliminarlos
    o añadirlos """

planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas)

# Un set es aleatorio, no tiene orden

#largo

print(len(planetas))
# revisar si un elemento está presente

print('Marte' in planetas)

# agregar un elemento

planetas.add('Tierra')
print(planetas)

# Eliminar elementos

planetas.remove('Tierra')
print(planetas)

# Eliminar elementos, y en caso de que no se encuentre dicho elemento, no arroje ningun error

planetas.discard('Martes')
print(planetas)