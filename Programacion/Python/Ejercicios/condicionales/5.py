edad = int(input("Cual es su edad: "))
ingresos = int(input("Ingresos mensuales: "))

if edad >= 16 and ingresos >= 1000:
    print(f'Al tener {edad} años y unos ingresos mensuales de {ingresos} euros, debes tributar.')
else:
    print('Aun no debes tributar')