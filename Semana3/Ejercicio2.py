#Ciclo for
'''
for x in range(0,4):
    print('Estamos en la iteracion: ', str(x))
'''

#Ejemplo split() con for
'''
oracion='Juan entiende muy bien python'
frases = oracion.split(); #Convierte la cadena en una lista, para posteriormente recorerla en un for
print(frases)
for palabra in range(len(frases)):
    print('Palabra {0}, en la frase tiene la ubicacion {1}'.format(frases[palabra], palabra))
'''
#For con diccionario

datos_basicos = {
    "nombres":"Leonardo Jose",
    "apellidos":"Caballero Garcia",
    "cedula":"26938401",
    "fecha_nacimiento":"03/12/1980",
    "lugar_nacimiento":"Maracaibo, Zulia, Venezuela", "nacionalidad":"Venezolana",
    "estado_civil":"Soltero"
}
print(datos_basicos,"\n")
cantidad_datos = datos_basicos.items()
print(cantidad_datos,"\n")

for clave, valor in cantidad_datos: 
    print(clave + ": " + valor)
