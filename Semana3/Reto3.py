# Crear y retornar diccionario segun la lista de tuplas
def AutoPartes(ventas: list) -> list:
    # Declarar diccionario que se va a retornar
    respuesta = {}
    # Recorrer lista de entrada [], cada campo se refiere a cada ubicacion de la lista en la iteracion del for
    for IdProducto, dProducto, pnProducto, cvProducto, sProducto, nComprador, cComprador, fVenta in ventas:
        #Se valida si la llave (isproducto) no existe, si no existe se crea si existe se agregan valores a lo que ya tiene
        if respuesta.get(IdProducto) == None:
            #Creacion nueva llave dentro del diccionario con el primer valor de la lista ingresada
            respuesta[IdProducto]=[]
        #else        
        #Registro de nueva lista de tuplas en el diccionario
        respuesta[IdProducto].append((dProducto, pnProducto, cvProducto, sProducto, nComprador, cComprador, fVenta))
    #Retorna diccionario de listas en sus valores
    return(respuesta)

# Consumir diccionario y retornar informacion segun idproducto del diccionario
def consultaRegistro(ventas, idProducto):    
    if idProducto in ventas:        
        for dProducto, pnProducto, cvProducto, sProducto, nComprador, cComprador, fVenta in ventas[idProducto]:
            print(f"Producto consultado : {idProducto}  Descripción  {dProducto}  #Parte  {pnProducto}  Cantidad vendida  {cvProducto}  Stock  {sProducto}  Comprador {nComprador}  Documento  {cComprador}  Fecha Venta  {fVenta}")
    else:
        print("No hay registro de venta de ese producto")
    


consultaRegistro(AutoPartes([
 (9852,'Culata', 'XC9875',2,165,'Luis Molero',3455846,'14/06/2020'),
 (9852,'Culata', 'XC9875',2,165,'Jose Mejia',1355846,'14/06/2020'),
 (2564,'Cárter', 'PT29872',2,32,'Peter Cerezo',8545436,'14/06/2020'),
 (5412,'válvula', 'AZ8798',2,11,'Juan Peña',568975,'14/06/2020')]), 9852)

