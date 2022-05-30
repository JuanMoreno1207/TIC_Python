#Declaramos funcion que recibe como parametro un diccionario
def reportarPromedio(dicReporte):
    return dicReporte['estudiante']+" = "+str(dicReporte['promedio'])

#Declaramos diccionario
dicNotas={
    'estudiante':'Juan Moreno',
    'nota1':3.0,
    'nota2':2.1,
    'nota3':5.0,
    'nota4':4.7
}

#Declaramos funcion que calcula el promedio y retorna un diccionario
def generarReportesNotas(diccionario:dict):
    sumatoria=0
    sumatoria+=diccionario['nota1']
    sumatoria+=diccionario['nota2']
    sumatoria+=diccionario['nota3']
    sumatoria+=diccionario['nota4']
    promedio= round(sumatoria/4,2)
    respuesta={
        'estudiante':diccionario['estudiante'],
        'promedio':promedio
    }
    return respuesta


#Llamamos a la funcion que retorna una cadena que es compuesta por la otra funcion que retorna un diccionario

print(reportarPromedio(generarReportesNotas(dicNotas)))