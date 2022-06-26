import pandas as pd
rutaFileCsv = 'https://raw.githubusercontent.com/luisguillermomolero/MisionTIC2022_2/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv'

def listaPeliculas(rutaFileCsv: str)->str:    
    if rutaFileCsv.split('.')[-1] == 'csv':
        
        try:            
            aCsv = pd.read_csv(rutaFileCsv)            
            subGrupoPeliculas = aCsv[['Country','Language','Gross Earnings']]            
            gananciaPaisLenguaje = subGrupoPeliculas.pivot_table(index=['Country','Language'])
            return gananciaPaisLenguaje.head(10)
        except:
            print('Error al leer el archivo de datos.')
    else:
        print('Extensión inválida.') 

print(listaPeliculas(rutaFileCsv))