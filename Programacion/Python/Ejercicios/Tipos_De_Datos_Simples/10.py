"""
    Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
    Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros.
    Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario.
    Despues el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años.
    Redondear cada cantidad a dos decimales.
"""

print("\t\t[*] AHORROS ANUALES [*]")

dineroDepositado = int(input("\f\nPor favor igrese el dinero que desea depositar: "))
interesAnual = (dineroDepositado / 100) * 4
primerAno = dineroDepositado + interesAnual
tercerAno = (interesAnual * 3) + dineroDepositado
segundoAno = (interesAnual * 2) + dineroDepositado

print(f'\fEl dinero depositado por usted es de {dineroDepositado}€ con un interes en euros anual de {interesAnual}€')
print(f'\fEl primer año tendra un total de {primerAno}€')
print(f'\fEl segundo año tendra un total de {segundoAno}€')
print(f'\fEl tercer año tendra un total de {tercerAno}€')

