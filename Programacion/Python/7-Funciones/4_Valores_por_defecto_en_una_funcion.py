# Para añadir valores por defecto y que no de error en el caso de que no los introduzcamos

def sumar(a=0,b=0):
    return a + b 

resultado = sumar()

print(f'El resultado es {resultado}')