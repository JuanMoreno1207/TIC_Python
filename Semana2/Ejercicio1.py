# Condicionales
from email import message


var1 = 5
var2 = 5

'''
print(var1 > var2)
print(var1 < var2)
print(var1 >= var2)
print(var1 <= var2)
print(var1 != var2)
print(var1 == var2)
'''

x = 7

'''
# Vaidar si un numero es positivo
if x > 0:
    print('x es numero positivo')
'''

'''
# Validar si un numero es par o impar segun la funcion modular (%)
if x % 2 == 0:
    print('El numero es par')
else:
    print('El numero es impar')
'''

'''
# Validar cual numero es mayor o si son iguales (if, elif, else)
x = 10
y = 10
if x < y:
    print('X es menor que Y')
elif x > y:
    print('Y es menor que X')
else:
    print('Los numeros son iguales')
'''

# try y except 
'''
1. Recibe un valor digitado con la funcion input
2. Convierte dicho valor a float y lo almacena en la variable fahr
2. Realiza operaciones con la variable fahr (float) y dichas operaciones las almacena en la variable cel
3. Imprime la variable cel
NOTA: Si no ingresa un valor o se presenta alguna novedad en el proceso, activa el try-excepto y retorna un mensaje de validacion


temperatura_fahr =input('Introduzca una temperatura en Fahrenheit:')
try:
    fahr = float(temperatura_fahr)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('No ingreso ningún valor, favor validar.')
'''




