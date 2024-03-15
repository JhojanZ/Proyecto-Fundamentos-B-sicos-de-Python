import pandas as pd
from sodapy import Socrata

department = "CAUCA"
limits = 100000

client = Socrata("www.datos.gov.co", None)

parameters = "ciudad_municipio_nom, edad, tipo_recuperacion, fuente_tipo_contagio, estado, pais_viajo_1_nom, fecha_inicio_sintomas"
results = client.get("gt2j-8ykr", limit=limits, select=parameters)

df = pd.DataFrame.from_records(results)
#print(results_df)

from ui.ui import show_data


df['edad'] = df['edad'].astype(int)
df['pais_viajo_1_nom'].fillna("Colombia", inplace=True)
df['tipo_recuperacion'].fillna("Tiempo", inplace=True) #por moda


def cleanup_column_names(df,rename_dict={},do_inplace=True):
    """This function renames columns of a pandas dataframe
    It converts column names to snake case if rename_dict is not passed.
    Args:
    rename_dict (dict): keys represent old column names and values point to
    newer ones
    do_inplace (bool): flag to update existing dataframe or return a new one
    Returns:
    pandas dataframe if do_inplace is set to False, None otherwise
    """
    if not rename_dict:
        return df.rename(columns={col: col.lower().replace(' ','_')
        for col in df.columns.values.tolist()},
        inplace=do_inplace)
    else:
        return df.rename(columns=rename_dict,inplace=do_inplace)
    
cleanup_column_names(df)

show_data(df)





print("Number of rows::",df.shape[0])
print("Number of columns::",df.shape[1] )
print("Column Names::",df.columns.values.tolist())
print("Column Data Types::\n",df.dtypes)

# Verificar si hay valores NaN

print("Columns with Missing Values:", df.columns[df.isnull().any()].tolist())
print("Number of rows with Missing Values:", len(df[df.isnull().any(axis=1)]))
print("Sample Indices with missing data:", df[df.isnull().any(axis=1)].index.tolist()[0:5])


print("General Stats::")
print(df.info())
print("Summary Stats::" )
print(df.describe())


"""
Number of rows:: 1000000
Number of columns:: 6
Column Names:: ['ciudad_municipio_nom', 'edad', 'tipo_recuperacion', 'fuente_tipo_contagio', 'estado', 'pais_viajo_1_nom']
Column Data Types::
 ciudad_municipio_nom    object
edad                     int64
tipo_recuperacion       object
fuente_tipo_contagio    object
estado                  object
pais_viajo_1_nom        object
dtype: object
Columns with Missing Values: ['tipo_recuperacion', 'pais_viajo_1_nom']
Number of rows with Missing Values: 999760
Sample Indices with missing data: [0, 1, 2, 3, 4]
General Stats::
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000000 entries, 0 to 999999
Data columns (total 6 columns):
 #   Column                Non-Null Count    Dtype 
---  ------                --------------    ----- 
 0   ciudad_municipio_nom  1000000 non-null  object
 1   edad                  1000000 non-null  int64 
 2   tipo_recuperacion     969902 non-null   object
 3   fuente_tipo_contagio  1000000 non-null  object
 4   estado                1000000 non-null  object
 5   pais_viajo_1_nom      250 non-null      object
dtypes: int64(1), object(5)
memory usage: 45.8+ MB
None
Summary Stats::
                 edad
count  1000000.000000
mean        39.602276
std         17.724533
min          1.000000
25%         27.000000
50%         38.000000
75%         52.000000
max        110.000000
"""