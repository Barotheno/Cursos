peso = 0
estatura = 0
total = 0

print("\n\t\t[*] Indice de masa corporal [*]")

print("\n\tB==D Le pediremos su peso y su estatura.")
peso = float(input("\t * Por favor indique su peso: "))
estatura = float(input("\t * Por favor inque su estatura: "))

total = peso / estatura**2

print(f'\nf Bien, ya lo tenemos. Su IMC es de: {total}')

if total <= 18.5:
    print("\n\tTienes un peso insuficiente, empieza a comer mejor")
elif total <= 25:
    print("\n\tEstas perfecto")
elif total <= 30:
    print("\n\tTienes sobrepeso, haz deporte y construye una dieta")
else:
    print("\n\tEstas jodido mi bro, ves a un médico, cambia y mejora los habitos")
