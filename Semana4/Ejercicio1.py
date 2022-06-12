#Conversion de cadena
#Conversion a lista
Cadena="Hola mundo"
Cadena2="Que se dice"
lista= list(Cadena)
#print(lista)
#Conversion a tupla
Tupla = tuple(Cadena)
tuplaG = (Tupla,15,tuple(Cadena2))
#print(tuplaG)
#Conversion a conjunto
Conjunto=set(Cadena)
#print(Conjunto)

#Conversion de lista
#Conversion a cadena
lista=['h','o','l','a']
Cadena += ' '+''.join(lista)
#print(Cadena)
#Conversion a tupla
lista2=[1,2,3,'h','o']
tupla=tuple(lista2)
#print(tupla)
#Conversion a conjuntos
conj=set(lista2)
print(conj)


