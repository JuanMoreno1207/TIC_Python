# Encapsular funciones
def suma(val1=0, val2=0):
    return val1+val2


#print(suma(1, 2))

# Asignar una funcion a una varibale, sin parentesis
FuncionSuma = suma

#Enviar como parametro una funcion
def Operacion(funcion, val1=0, val2=0):
    return funcion(val1,val2)

Resultado=Operacion(suma,10,5)
#print(Resultado)


#Retornar funcion dentro de otra funcion
def CrearFuncion(oper):
    if oper == '+':
        def suma (val1=0, val2=0):
            return val1+val2
        return suma
    elif oper == '-':
        def resta (val1=0, val2=0):
            return val1-val2
        return resta

#Alojamos en variable la funcion CrearFuncion
Adicion = CrearFuncion('-')

Resultado=Operacion(Adicion, 20,30)
print(Resultado)

