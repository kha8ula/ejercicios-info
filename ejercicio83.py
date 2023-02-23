meses= ['Enero', 'Febrero', 'Marzo', 'Abril','Mayo','Junio','Julio','Agosto',
'Septiembre', 'Octubre','Noviembre', 'Diciembre']
num= int(input('Dame un número del 1 al 12: '))

while num <1 or num >12:
    num=int(input('Dame un número del 1 al 12: '))  

print (meses[num-1])