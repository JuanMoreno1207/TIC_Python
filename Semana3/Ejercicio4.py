#Listas paralelas
nombres=[]
edades=[]

#Ejercicio, ingresar 3 nombres e imprimir unicamente los que tengan mayor o igual a 18 años
for x in range(3):
    nom=input('Ingrese nombre de la persona: ')
    nombres.append(nom)
    edad=int(input('Ingrese edad de la persona: '))
    edades.append(edad)    
for y in range(len(edades)):    
    if edades[y] >=18:
        print(" ", nombres[y])
