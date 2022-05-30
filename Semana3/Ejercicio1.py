# ciclos repetitivos, ciclo while
'''
n = 5
while n > 0:
    # print(n)
    n = n-1
print('Despegue')
'''

# Imprimir los primeros 40 numeros de 100
'''
j = 0
while j <= 40:
    print(j)
    j = j + 1

'''

# continue -> nos permite finalizar (omitir) el recorrido mas no terminar el while, al finalizar el recorrido las instrucciones posteriores no se realzaran

'''
i = 0
while i < 6:
    i += 1
    if i == 4:
        continue
    print(i)
'''

# mostrar los primeros 5 numeros impares saltando el cuarto valor, comenzando en 0

'''
k = 0
while k <=10:
    k += 1
    if k == 7:
        continue
    if k %2 != 0:        
        print(k)      
'''

# break -> nos permite terminar las iteraciones de un ciclo cuando se cumple una condicion

'''
h = 0
while h <=10:
    print(h)
    h += 1    
    if h==3:
        break
'''

# Ejercicio while controlado por evento de input()
promedio, total, contar = 0.0, 0, 0
print("Introduzca la nota de un estudiante (-1 para salir):")
nota = int(input())
while nota != -1:
    total += nota
    contar += 1
    print("Introduzca la nota de un estudiante (-1 para salir):")
    nota = int(input())
promedio = total / contar
print("Promedio de notas del grado escolar es: " + str(promedio))
