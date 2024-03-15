import pandas as pd

def limpiar_datos(df):
    df['edad'] = df['edad'].astype(int)
    df['tipo_recuperacion'].fillna("Tiempo", inplace=True) #por moda

    
    if 'pais_viajo_1_nom' in df.columns:
      df['pais_viajo_1_nom'].fillna("Colombia", inplace=True)
