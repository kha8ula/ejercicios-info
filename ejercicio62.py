usuario=input('Dime el usuario: ')

while usuario!= 'admin':
    usuario=input('Dime el usuario: ')
    if usuario=='admin':
        break
clave=(input('Escriba la clave: '))
while clave!= '0987':
    clave=int(input('Escriba la clave: '))
    if clave== '0987':
        print('¡Bienvenido!')
        break
    