# Variables

nombre = input('Por favor introduzca su nombre: ')
sexo = input('Eres hombre o mujer: ')
nombreM = nombre.lower()
sexoM = nombre.lower()
letraNombre = nombreM[0:1]

nombreCa = nombre.capitalize()
sexoCa = sexo.capitalize()

if letraNombre < "m":
    print(f'Hola {nombre.capitalize()} tu grupo esta en el A')
elif letraNombre > "n":
    print(f'Hola {nombre.capitalize()} tu grupo esta en el A')
else:
    print(f'Hola {nombre.capitalize()} tu grupo esta en el B')


