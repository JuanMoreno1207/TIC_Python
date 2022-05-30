# Como acceder a los caracteres de una cadena string
nombre = 'Juan Moreno'
letra = nombre[5]
# print(letra)

# Conseguir la longitud de una cadena string, siempre comienza en cero cuando se trata de ubicacion
longitud = len(nombre)
# print(longitud-1)

# Obtener un pedazo de la cadena string, siempre comienza en 1
# Se pueden omitir el inicio o final de cadena sin establecer una ubicacion
# print(nombre[:4])
# print(nombre[5:])

# operador in, valida si una cadena esta en otra y retorna valores boolean (true-false)
var1 = 'a'
var2 = 'banana'
#print(var1 in var2)

# Comparar cadenas
'''
if(nombre=='Juan Moreno'):
    print('La palabra es igual')
else:
    print('La palabra es diferente')
'''
# Para encontrar el tipo de variable usamos el metodo type() y para validar los metodos disponibles usamos el metodo dir()
# print(type(nombre))
# print(dir(nombre))

# Encontrar un fragmento de una cadena
data = 'De stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
posicion = data.find('@')
#print(posicion)
posicionespacio = data.find(' ', posicion)
#print(posicionespacio)
nuevapalabra = data[posicion + 1:posicionespacio]
#print(nuevapalabra)

# Operador de formato % (asigna la variable a la cadena concatenada con el simbolo %s o %d)
camellos=42
#print ('He visto %d camellos' %camellos)
#print ('Mi nombre es %s' %nombre)

# Caracter especial (r omite los caracteres)
cadena="hola\nmundo"
#print(cadena)
cadena=r"hola\nmundo"
#print(cadena)

# Contar cuantas veces aparece un cadena en una cadena general
cadena="un uno, un dos, un tres"
print (cadena.count("un")) # Saca 4, hay 4 "un" en cadena.
print (cadena.count("un",10)) # Saca 1, hay 1 "un" a partir de la posición 10 de cadena.
print (cadena.count("un",0,10)) # Saca 3, hay 3 "un" entre la posición 0 y la 10.

