# Creacion de funciones
def ImprimeCosas():
    print("La clase esta genial")
    print("Python es genial")
# Llamar funcion
# ImprimeCosas()

def OperacionSuma():
    a = 17
    b = 3
    suma = a + b
    return "La suma de los numeros "+str(a)+" mas "+str(b)+" es : " + str(suma)
# Almaceno el return de la funcion en una variable
ResultadoFunc = OperacionSuma()
# print(ResultadoFunc)
# Imprimo el return de la funcion directamente
# print(OperacionSuma())

# Declaro funcion con print interno
def OperacionSumaP():
    a = 17
    b = 3
    suma = a+b
    print("La suma de los numeros ", a, " mas ", b, " es : ", suma)
# Llamo funcion con print
# OperacionSumaP()

# Funcion dentro de otra funcion
def RepetirFunciones():
    print("\n")
    OperacionSumaP()
# Llamo funcion
# RepetirFunciones()

#Funcion con parametros
def Suma(a,b):
    return(a+b)
#print(Suma(2,4))

#Funcion con interaccion al usuario (input)
def SumaNumerosInteraccion():
    num1=float(input("Ingrese el primer numero: "))
    num2=float(input("Ingrese el segundo numero: "))
    print("La suma de los numeros", int(num1)," mas ",int(num2), "es de : ", int(num1+num2))

#SumaNumerosInteraccion()

# Funciones anidadas
def FuncionExterna(x):
    def FuncionInterna(y):
        return x*y
    return FuncionInterna

resultado = FuncionExterna(2)
#print(resultado(5))

def PrimeraFuncion():
    x = 2
    def SegundaFuncion(a):
        x = 6
        print (x+a)     
        return x           
    x = SegundaFuncion(10)
    print(x)
PrimeraFuncion()
