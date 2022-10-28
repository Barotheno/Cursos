precio = input("Introduzca un precio con dos decimales: ")
entero = precio[:precio.find('.')]
decimales = precio[precio.find('.')+2]

print(f'El precio es de {entero} euros con {decimales} centimos.')