#Listas, son mutables (se pueden modificar), permite diferentes tipos de datos, siempre comienza en 0

Listas = [1,2.5,'DevCode',[5,6],4]
'''
print(Listas[0])
print(Listas[2])
print(Listas[3])
print(Listas[3][0])
print(Listas[3][1])
print(Listas[0:2])
print(Listas[1:3]) #Desde que ubicacion comienzo y donde paro , el segundo comienza en 1 desde el primer objeto de la lista
'''

#Metodo append, para agregar elementos

Listas.append('Juan Moreno')
#print(Listas)

#Metodo Count, para contar la cantidad de veces que se repite dicho valor

#print(Listas.count('Juan Moreno'))

#Metodo extend() extiende una lista agregando un iterable al final

Listas.extend([4])
#print(Listas)
Listas.extend(range(4,10))
#print(Listas)

#Metodo index(), recibe argumento como parametro y devuelve el indice de la primera aparicion en la lista
#print(Listas.index('Juan Moreno'))
#Se le puede agregar como segundo parametro desde donde comenzar a buscar
#print(Listas.index(4,5))
#print(Listas)

#Metodo Insert() nos permite insertar un elemento x en el indice i, sin eliminar los que ya esten en dicha ubicacion
Listas.insert(2,'Juan Moreno')
#print(Listas)

#Metodo Pop(), devuelve el ultimo elemento de la lista,
#posteriormente lo elimina puesto que por defecto tiene el valor -1, sin embargo se puede eliminar la ubicacion que se requiera
#print(Listas)
#print(Listas.pop(6))
#print(Listas)

#Metodo remove (), remueve la primera apareicion del elemento en la lista
#print(Listas)
#Listas.remove('Juan Moreno')
#print(Listas)

#Metodos para ordenar ascendente y descendentemente, deben ser de un tipo unico de datos
Lista1=[0.1,1.1,2.0,4,1.1]
#print(Lista1)
Lista1.sort()
#print(Lista1)
Lista1.sort(reverse=True)
#print(Lista1)

Lista2=['Juan', 'Andres', 'Sebastian']
#print(Lista2)
Lista2.sort()
#print(Lista2)
Lista2.sort(reverse=True)
#print(Lista2)