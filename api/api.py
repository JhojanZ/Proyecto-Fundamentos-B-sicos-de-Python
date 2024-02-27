import pandas as pd
from sodapy import Socrata

def obtain_api(limits, department):
    client = Socrata("www.datos.gov.co", None)

    results = client.get("gt2j-8ykr", limit=limits, departamento_nom=department, select="ciudad_municipio_nom, edad, tipo_recuperacion, fuente_tipo_contagio, estado, pais_viajo_1_nom")

    results_df = pd.DataFrame.from_records(results)
    #print(results_df)

    return results_df


# , "ciudad_municipio_nom", "edad", "fuente_tipo_contagio", "estado", "pais_viajo_1_nom"