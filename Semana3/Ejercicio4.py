#Listas paralelas
nombres=[]
edades=[]

#Ejercicio, ingresar 3 nombres e imprimir unicamente los que tengan mayor o igual a 18 años

# for x in range(3):
#     nom=input('Ingrese nombre de la persona: ')
#     nombres.append(nom)
#     edad=int(input('Ingrese edad de la persona: '))
#     edades.append(edad)    
# print('Nombres de las personas mayores de edad.')
# for y in range(len(edades)):    
#     if edades[y] >=18:
#         print(" ", nombres[y], " edad: ", edades[y])

#Listas Compuestas
Numeros=[[0,1,2],[3,4,5],[6,7,8],[9,10,11]]

#print(Numeros)
#print(Numeros[0])
#print(Numeros[0][0])

#Recorremos un for segun la longitud de una lista e imprimimos dicha lista en la posicion 0 en el objeto respectivo
# for x in range(len(Numeros)):
#     print(Numeros[0][x])

#print(len(Numeros) , " pruebas")
#Imprimimos cada elemento entero de cada lista contenida en la lista principal
# for x in range(len(Numeros)):    
#     for y in range(len(Numeros[x])):
#         print(Numeros[x][y])

#Imprimir la lista 
#print(Numeros)
#Imprimir los elementos de la lista 
for ubicacion in range(len(Numeros)):
    #print(Numeros[ubicacion])
    pass
#Imprimir solo el primer numero de cada lista de la lista
for ubicacion in range(len(Numeros)):
    #print(Numeros[ubicacion][0])
    pass
#Imprimir cada numero de las listas integradas en la lista principal
for ubicacion1 in range(len(Numeros)):
    for ubicacion2 in range(len(Numeros[ubicacion1])):
        #print(Numeros[ubicacion1][ubicacion2])
        pass
#Calcular la suma de cada lista contenida en la lista principal (2 elementos)
ListaSuma=[[1,2,3,4,5],[2,8,5,9,4]]
for ubicacion in range(len(ListaSuma)):
    suma=0
    for ubicacionelemnto in range(len(ListaSuma[ubicacion])):
        suma += ListaSuma[ubicacion][ubicacionelemnto]
        pass
    #print(suma)


#Ejercicio padres e hijos
Padres= list ()
Hijos= list ()

#hacemos for para que solicite 3 veces el nombre del padre y madre
for x in range(2):
    papa=input("Ingrese el nombre del padre : ")
    mama=input("Ingrese el nombre de la mama : ")   
    #Agregamos una lista dentro de la lista principal con los valores recuperados en el input 
    Padres.append([papa,mama])
    cant=int(input("Ingrese la cantidad de hijos : "))
    #Agregamos una lista vacia que segun el input cant sera rellenada en cierta posicion
    Hijos.append([])
    for y in range(cant):
        hijo=input("Ingrese el nombre de su hijo : ")       
        Hijos[x].append(hijo)
#Imprimimos nombre de padre, madre e hijos
for x in range(len(Padres)):
    print("Padre: " + Padres[x][0])
    print("Madre: " + Padres[x][1])   
    if len(Hijos[x])>0:
        for y in range(len(Hijos[x])):
            print("Hijo: " + Hijos[x][y])
    else:
        print("Sin hijos registrados")
#Imprimimos Solo el nombre del padre con la cantidad de hijos
for x in range(len(Padres)):
    print("Padre: "+ Padres[x][0])
    print("Cantidad de hijos: "+ str(len(Hijos[x])))


