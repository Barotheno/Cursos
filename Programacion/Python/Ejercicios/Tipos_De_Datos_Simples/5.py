print("[*] CALCULADORA DE HORAS LABORALES [*] ")

horas = int(input("\n\tCuantas horas has trabajado: "))
coste = int(input("\tCual es el coste por hora: "))
total = horas * coste 

print(f'\n\tEn total deben abonarte una cantidad de: {total} euros')