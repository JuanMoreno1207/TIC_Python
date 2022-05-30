'''
    Metodo clear ()
    Remueve o elimina los items de un diccionario

'''
dicNotas={
    'estudiante':'Juan Moreno',
    'nota1':3.0,
    'nota2':2.1,
    'nota3':5.0,
    'nota4':4.7
}
#print('\n', dicNotas)
#dicNotas.clear()
#print('\n', dicNotas)

'''
    Metodo copy ()
    devuelve una copia de un diccionario

'''
#print('Diccionario:' , dicNotas)
diccionario2= dicNotas.copy()
#print('Diccionario2:' , diccionario2)

'''
    Metodo fromkeys () 
    crea una copia de un diccionario a partir de sus llaves

'''

lista={
    'nombre',
    'apellido',
    'cedula'
}

nuevalis=dict.fromkeys(lista)

#print('\nNuevo diccionario: %s' %str(nuevalis))

'''
    Metodo get () 
    Devuelve el valor de una llave solicitada, si no existe retorna none

'''

#print(dicNotas.get('estudiante'))
#print(dicNotas.get('apellido'))
#print(dicNotas['apellido']) Con este se totea, por ende es mejor usar el get para que retorne el none

'''
    Metodo items () 
    Devuelve una tupla de un diccionario

'''

#print(dicNotas.items())

'''
    Metodo pop () 
    remueve una clave del diccionario y devuelve el valor de la misma

'''

#print('Diccionario original:', dicNotas)
#valoreli=dicNotas.pop('estudiante')
#print(valoreli)
#print('Diccionario modificado:', dicNotas)

'''
    Metodo update () 
    Actualiza un valor dentro del diccionario

'''
#print(dicNotas)
dicNotas.update({
    'estudiante' : 'Juan Bautista'
})
print(dicNotas)