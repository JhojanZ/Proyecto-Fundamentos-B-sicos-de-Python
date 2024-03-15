import matplotlib.pyplot as plt

def graficas(df):
    # pastel
    class_series = df.groupby('tipo_recuperacion').size()
    class_series.plot.pie(autopct='%.2f')
    plt.title('Forma de recuperación del COVID-19')


    # histogramas
    datos_edad = df['edad']
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(datos_edad, bins=100)
    ax.set_xlabel('Edad')
    ax.set_ylabel('Cantidad de infectados')
    ax.set_title('Infectados por CODIV-19 en Edades')
    plt.xticks(range(0, max(datos_edad)+1, 5))


    # Gráfico de barras verticales
    fig, ax = plt.subplots(figsize=(10, 6))
    conteo_estados = df['estado'].value_counts()
    ax.bar(x=conteo_estados.index, height=conteo_estados.values, color=['#34ff2e', '#da0000', '#000dda'])
    ax.set_xlabel('Estado')
    ax.set_ylabel('Cantidad de Personas')
    ax.set_title('Cantidad de Personas por Gravedad del COVID-19')

    for i, v in enumerate(conteo_estados.values):
        ax.text(i, v + 0.1, str(v), ha='center', va='bottom')

    #Grafico de barras horizontales
    x = df['ciudad_municipio_nom'].value_counts().index.tolist() 
    y = df['ciudad_municipio_nom'].value_counts().tolist() 


    fig, ax = plt.subplots(figsize=(10, 8)) 
    bars = ax.barh(x, y, height=0.5, color='black')  # Ajustar grosor y color de las barras
    ax.invert_yaxis()

    for bar, label in zip(bars, y):
        ax.text(bar.get_width(), bar.get_y() + bar.get_height()/2, 
                f'{label}', 
                va='center', ha='left')

    # muestra los graficos
    plt.show()

