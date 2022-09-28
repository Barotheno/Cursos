print('Podras ir al picnic?')

vacaciones = input('Dime con un "si" o un "no" si tienes vacaciones: ')
diaDescanso = input('Dime con un "si" o un "no" si tienes dia de descanso: ')

if vacaciones == 'si':
    vacacionesTotal = True
else:
    vacacionesTotal = False 

if diaDescanso == 'si':
    diaDescansoTotal = True 
else:
    diaDescansoTotal = False 

if vacacionesTotal or diaDescansoTotal:
    print('Puedes venir')
else:
    print('No puedes venir')