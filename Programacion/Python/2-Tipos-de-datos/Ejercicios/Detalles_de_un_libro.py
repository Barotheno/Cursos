"""
    Se solicita incluir la siguiente información acerca de un libro:

        Titulo
        Autor
    
    Debes imprimir la información en el siguiente formato:

        Proporciona el título:
        Proporciona el autor:

    <titulo> fue escrito por <autor>

"""

print('[*] Bienvenido a la biblioteca sabelotodo [*]')

titulo = input('Proporciona el título: ')
autor = input('Proporciona el autor: ')

print(f'Genial veamos si los datos son correctos...')
print(f'\n\tEl libro {titulo} escrito por el autor {autor} lo tenemos justo para ti.')