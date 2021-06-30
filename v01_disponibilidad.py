"""
Calculo de disponibilidad de datos estaciones REM
v01- 24/06/2021
"""

import pandas as pd
from datetime import datetime
import numpy as np

# importo datos de estacion
datos = pd.DataFrame()
datos = pd.read_csv("Aparicio Saravia.txt",usecols = [0] , sep="\t")

# limpio dataframe para que unicamente traiga las fechas 
datos['Fecha_hora'] = pd.to_datetime(datos['Fecha_hora'],errors='coerce')
datos = datos.dropna()
# ordeno valores
datos = datos.sort_values(by='Fecha_hora')

# creo rango de datos para comparar con datos existentes
rango_datos=pd.date_range(start=datos.iloc[0][0], end=datos.iloc[-1][0], freq="10min")

# creo array para conocer la disponibilidad de los datos 
disponibilidad = np.where(rango_datos.isin(datos['Fecha_hora']),1,0)

# paso array a pandas
disponibilidad = pd.DataFrame({'Disponibilidad':disponibilidad})

# datos no disponibles
resumen_total = disponibilidad.groupby(['Disponibilidad'])['Disponibilidad'].count()
print(resumen_total)

# calculos de disponibilidad total de datos
disponibilidad_total = resumen_total[1]/len(disponibilidad)
print("Disponibilidad total de los datos:",round(disponibilidad_total*100,2),'%')

resumen_trimestral = []

def disponibilidad_trimestral():
    global disponibilidad, resumen_trimestral
    
    # defino inicio de la ventana y cantidad de dias 
    diezminutalXdia = 144
    inicio = 0
    trimestre = 90 * diezminutalXdia
    
    # array para almacenar el resumen de las disponibilidades trimestrales
    resumen_trimestral = []
    
    for i in range(0,round(len(disponibilidad)/90)): # revisar for, la iteracion no es esta
        
        # agrupo datos
        disponibilidad_trimestre = disponibilidad[inicio:trimestre].groupby(['Disponibilidad'])['Disponibilidad'].count()
        print(disponibilidad_trimestre[1])
        # incremento ventana de tiempo
        incio = trimestre
        trimestre = trimestre + (90*diezminutalXdia)
        
        resumen_trimestral.append(disponibilidad_trimestre[1]/diezminutalXdia*90) 
        
    return resumen_trimestral    


disponibilidad_trimestral()


# Caracoles 25/6
# Mc meekan 21/6
# Rosendo mendoza 23/6
# Jose ignacio 28/6
# Punta del tigre 22/6








