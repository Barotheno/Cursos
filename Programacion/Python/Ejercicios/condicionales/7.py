rentaAnual = int(input("Cual es tu renta anual: "))
total = 0

if rentaAnual <= 10000:
    total = (rentaAnual / 100) * 5
    print(f'El impositivo correspondiente es un 5%, en total seria: {total} euros')
elif rentaAnual > 10000 and rentaAnual <= 20000:
    total = (rentaAnual / 100) * 15
    print(f'El impositivo correspondiente es un 15%, en total seria: {total} euros')
elif rentaAnual > 20000 and rentaAnual <= 35000:
    total = (rentaAnual / 100) * 20
    print(f'El impositivo correspondiente es un 20%, en total seria: {total} euros')
elif rentaAnual > 35000 and rentaAnual <= 60000:
    total = (rentaAnual / 100) * 30
    print(f'El impositivo correspondiente es un 30%, en total seria: {total} euros')
else:
    total = (rentaAnual / 100) * 45
    print(f'El impositivo correspondiente es un 45%, en total seria: {total} euros')

