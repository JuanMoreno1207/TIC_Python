# declarar variable float
var1 = 1.35
# print(var1)
# castear valores de float a int
var1 = int(var1)
# print(var1)

var1 = "100"
var1 = int(var1)+100
# print(var1)

'''
    -- ERRORES AL DECLARAR VARIABLES

    var 1 = 80 (Espacios en la variable)
    @var1 = 10 (Caracteres especiaes)
    1Var = 10 (No puede iniciar en numero)
    var-4 = 10 (Guion dentro del nombre)
    
'''

# Asignacion variables

num1 = num2 = num3 = 300
# print(num1,"\n",num2,"\n",num3)

num_1, num_2, num_3 = 34, 12, 2.17
# print(num_1)
# print(num_2)
# print(num_3)

# Jerarquia de operaciones (PEMDAS)

x = 2 * (5-1)
#print (x)

x = (1+1) ** (5-2)
# print(x)

x = 2 ** 1 + 1
#print (x)

y = 3 * 1 ** 3
# print(y)

var1 = 1.0
var2 = 4.5
var3 = 5.5
var4 = 2.5
promedio = (var1+var2+var3+var4)/4

print("El promedio de los numeros es : "+str(promedio))
print("El promedio de los numeros es :", round(promedio))
print("El promedio de los numeros es :", round(promedio, 2))
