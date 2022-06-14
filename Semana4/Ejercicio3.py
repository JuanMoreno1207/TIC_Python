#Funciones lambda
#Sin nombre
#nombre de funcion Sumar
#parametros de funcion val1, val2
#proceso de funcion val1+val2

#Ejemplo1
Sumar = lambda val1, val2 : val1 + val2
#print(Sumar(5,10))

#Ejemplo2
#nombre de funcion Operacion
#parametros de funcion OperReal, val1, val2
#proceso de funcion, segun lo que la funcion que se reciba en el parametro OperReal realice

Operacion = lambda OperReal, val1, val2 : OperReal(val1, val2)
ResultadoOper=Operacion(Sumar, 10, 50)
#print(ResultadoOper)

#Ejemplo3 Funcion anonima sin parametros
#Nombre de funcion OperacionBool
#parametros, sin parametros
#proceso de la funcion, retornar siempre True

OperacionBool = lambda : True
#Retorna True porque OperacionBool retorna siempre True
print(OperacionBool() == True)
