'''
hora_dia=10

if hora_dia>=12:
    print ("pm");
else:
    print ("am")
'''
'''
# Validar longitud de un numero y mediante el try y except, controlar los errores generados
num = int(input('Por favor ingrese el numero: '))
try:    
    if num < 0:
        num = num * (-1)
    if ((num>0) and (num<10)):
        print("El numero es de un digito")
    elif ((num>=10) and (num<100)):
        print("El numero es de dos digitos")
    elif ((num>=100) and (num<1000)):
        print("el numero es de tres digitos")
    elif ((num>=1000) and (num<9999)):
        print("el numero es de cuatro digitos")
    else:
        print("El numero tiene mas de 4 digitos")    
except ValueError as e:
    print(e)
'''
# Leer un numero entero y determinar si es positivo o negativo, si es positivo determinar si tiene dos digitos,
# si es negativo determinar si tiene tres digitos, asumir que no puede entrar numero 0

num = int(input('Digite un numero entero: '))
if(num==0):
    print('El numero no puede ser cero')
elif(num>0):
    if(num<=99 and num>=10):
        print('El numero es positivo y tiene dos digitos')
    else:
        print('El numero es positivo y no tiene dos digitos')
else:
    if((num>=-999 and num<=-100)):
        print('El numero es negativo y tiene 3 digitos')
    else:
        print('El numero es negativo y no tiene 3 digitos')
