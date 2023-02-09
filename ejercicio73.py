num=int(input('Dime un número: '))
for i in range(1,num+1):
    if i%7== 0:
        print(i)
    else:
        print('Ninguno es múltiplo de 7')