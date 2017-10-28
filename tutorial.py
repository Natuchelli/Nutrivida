def hi(name):
   if name =='Nutrivida':
       print ('Bienvenidos')
       print ('Esto es' + '_' + name + '_' + 'Nutricion en movimiento')
   elif name =='Lilian':
       print ('Hola')
   else:
       print ('¿Quién es?')

hi('Nutrivida')


def hi(girls):
    print ('Hola' + girls + '!')

alumnas = ['Agus', 'Anto', 'Naty', 'Cristina']
for girls in alumnas:
    hi (girls)
    print ('¡¡Sigue así!!')

for i in range(1, 8):
    print(i)
