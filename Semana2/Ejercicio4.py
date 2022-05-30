# declarar diccionario
diccionario = {}  # sin constructor
diccionario1 = dict()  # Con constructor
# print(type(diccionario))

# Si necesitamos agregar nuevos valores, solo es necesario agregarlos con (,)

diccionario1 = {
    "total": 40,
    "descuento": True,
    "subtotal": 12.59434,
    "cliente": "Marcos"
}

# print(diccionario1)

diccionario2 = dict({
    "total": 40,
    "descuento": True,
    "subtotal": 12.59434,
    "cliente": "Marcos"
})

#print(diccionario2['total'])

# Declarar funcion con parametro tipo diccionario
def prueba(diccionario:dict):
    print(diccionario)
#prueba(diccionario2)

# Imprimir todas las llaves (keys) o values de un arreglo

#print(diccionario2.keys())
#print(diccionario2.values())

# Recorrer el diccionario mediante sus respectivas llaves
for k in diccionario2.keys():
    print(f"{k} = {diccionario2[k]}")