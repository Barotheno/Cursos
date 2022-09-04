for letra in 'Holanda':
    #Terminamos ciclo for cuando encuentre la primera letra A

    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        break
        #Break rompe todo el ciclo, tampopo imprimira el print de else
        

else:
    print('Fin ciclo For')