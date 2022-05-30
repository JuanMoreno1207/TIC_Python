def cliente(informacion: dict)->dict:
    respuesta = {
        "nombre": informacion['nombre'],
        "edad": informacion['edad'],
        "atraccion": '',
        "apto": True,
        "primer_ingreso": informacion['primer_ingreso'],
        "total_boleta": 0
    }
    if(informacion['edad'] > 18):        
        respuesta['atraccion'] = 'X-Treme'
        if(informacion['primer_ingreso']==True):            
            respuesta['total_boleta'] = 20000 - (20000*5/100)
            return (respuesta)
        else:
            respuesta['total_boleta'] = 20000
            return (respuesta)
    elif((informacion['edad'] >= 15) and (informacion['edad'] <= 18)):    
        respuesta['atraccion'] = 'Carros chocones'  
        if(informacion['primer_ingreso']==True):            
            respuesta['total_boleta'] = 5000 - (5000*7/100)
            return (respuesta)
        else:
            respuesta['total_boleta'] = 5000
            return (respuesta)          
    elif((informacion['edad'] >= 7) and (informacion['edad'] < 15)):
        respuesta['atraccion'] = 'Sillas voladoras' 
        if(informacion['primer_ingreso']==True):            
            respuesta['total_boleta'] = 10000 - (10000*5/100)
            return (respuesta)
        else:
            respuesta['total_boleta'] = 10000
            return (respuesta)        
    else:
        respuesta['apto'] = False
        respuesta['atraccion'] = 'N/A'
        respuesta['total_boleta'] = 'N/A'        
        return respuesta


prueba = {
    "id_cliente": 1,
    "nombre": "Tatiana Ruiz",
    "edad": 8,
    "primer_ingreso": False
}

print (cliente(prueba))
