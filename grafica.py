from tabulate import tabulate

def show_data(data):
    head = ['N° Dato', 'Ciudad de Ubicación', 'Edad', 'Tipo de Recurperación', 'Fuente de contagio', 'Estado', 'País viaje']
    
    print("\n\n", tabulate(data, headers=head, tablefmt='mixed_grid', showindex=True), sep="")

# heavy_grid, fancy_grid, mixed_grid

import pandas as pd
from sodapy import Socrata
import matplotlib.pyplot as plt  # Modificación en esta línea

department = "CAUCA"
limits = 1000000

client = Socrata("www.datos.gov.co", None)

parameters = "ciudad_municipio_nom, edad, tipo_recuperacion, fuente_tipo_contagio, estado, pais_viajo_1_nom"
results = client.get("gt2j-8ykr", limit=limits, select=parameters)

df = pd.DataFrame.from_records(results)
#print(results_df)

df['edad'] = df['edad'].astype(int)
df['pais_viajo_1_nom'].fillna("Colombia", inplace=True)
df['tipo_recuperacion'].fillna("Tiempo", inplace=True) #por moda

def cleanup_column_names(df,rename_dict={},do_inplace=True):
    if not rename_dict:
        return df.rename(columns={col: col.lower().replace(' ','_')
        for col in df.columns.values.tolist()},
        inplace=do_inplace)
    else:
        return df.rename(columns=rename_dict,inplace=do_inplace)
    
cleanup_column_names(df)

max_edad = df['edad'].max()

df['pais_viajo_1_nom'].hist(color='green')
plt.title('Distribución de Precios')
plt.xlabel('ciudad_municipio_nom')
plt.ylabel('Edad')
plt.show()
plt.show()  # Agregando esta línea para mostrar la gráfica