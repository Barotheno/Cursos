
def listarTerminos(**terminos):#De esta forma creamos un diccionario
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')
        
listarTerminos(DC='Batman',MARVEL='Spider Man')