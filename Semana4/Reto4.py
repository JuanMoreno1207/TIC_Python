# lista de prueba
from functools import reduce
# Definicion de funcion
def ordenes(rutinaContable):
    montominimo=600000    
    #Funcion map siempre lleva como primer parametro una funcion "lambda", como segundo un iterable "lista"
    #La funcion lambda dice que de cada iteracion va a tomar la posicion [0], creando una lista con las posiciones 0
    #de cada lista
    # x = a cada lista de la lista general, para la nueva lista primero se toma con ayuda de map el valor [0] de x "toda la lista"
    # Despues se le agrega otro elemento a la lista igualmente con map, 
    # donde usamos la funcion lambda para multiplicar los de la posicion [1] de x en adelante ":"
    ListaTotales=list(map(lambda x : [x[0]] + list(map(lambda y : y[1]*y[2], x[1:])), rutinaContable))    
    ListaTotales=list(map(lambda x : [x[0]] + [reduce(lambda a,b : round(a+b,2), x[1:])], ListaTotales))    
    ListaTotales=list(map(lambda x : (x[0],x[1]) if x[1]>=montominimo else (x[0],x[1]+25000), ListaTotales))     
    print('------------------------ Inicio Registro diario ---------------------------------')
    for x in range(len(ListaTotales)):        
        print(f"La factura {ListaTotales[x][0]} tiene un total en pesos de {ListaTotales[x][1]:,.2f}")
    print('-------------------------- Fin Registro diario ----------------------------------')


lista = [
    [1201, ("5464", 4, 25842.99), ("7854", 18, 23254.99), ("8521", 9, 48951.95)],
    [1202, ("8756", 3, 115362.58), ("1112", 18, 2354.99)],
    [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20),("1254", 1, 13645.20), ("9965", 5, 1645.20)],
    [1204, ("9635", 7, 11.99), ("7733", 11, 18.99), ("88112", 5, 390.95)]
]
ordenes(lista)

