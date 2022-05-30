cantidad=0 #Dinero ingresado en el CDT
porcentaje_interes= 0.03 # 3%
tiempo=0 #Cantidad de tiempo
porcentajeperder= 0.02 # 2%

# Valor intereses ganados por tiempo mayor a 2 meses
valorintereses=(cantidad*porcentaje_interes*tiempo)/12

#Valor total del dinero
valortotal=valorintereses+cantidad

#tiempo menor o igual a dos meses
valoraperder=cantidad*porcentajeperder

#Valor total del dinero menos a dos meses
valortotal=cantidad-valoraperder

def CDT(usuario: str, capital: int, tiempo:int):
    if tiempo<=2:
        valoraperder=capital*0.02
        valortotal=capital-valoraperder
        return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valortotal}"
    else:
       valorintereses=(capital*0.03*tiempo)/12    
       valortotal=valorintereses+capital    
       return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valortotal}"
        
    
print(CDT('ER3366',650000,2))