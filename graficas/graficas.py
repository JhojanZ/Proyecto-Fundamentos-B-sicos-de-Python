import matplotlib.pyplot as plt

def graficas(df):
    # pastel
    class_series = df.groupby('tipo_recuperacion').size()
    class_series.plot.pie(autopct='%.2f')
    plt.title('Modo de recuperación')


    # histogramas
    datos_edad = df['edad']
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(datos_edad, bins=100)
    ax.set_xlabel('Edad')
    ax.set_ylabel('Cantidad de infectados')
    ax.set_title('Histograma de Edad')
    plt.xticks(range(0, max(datos_edad)+1, 5))


    # Gráfico de barras
    fig, ax = plt.subplots(figsize=(10, 6))
    conteo_estados = df['estado'].value_counts()
    ax.bar(x=conteo_estados.index, height=conteo_estados.values, color=['#34ff2e', '#da0000', '#000dda'])
    ax.set_xlabel('Estado')
    ax.set_ylabel('Cantidad de Personas')
    ax.set_title('Cantidad de Personas por Gravedad del COVID-19')

    for i, v in enumerate(conteo_estados.values):
        ax.text(i, v + 0.1, str(v), ha='center', va='bottom')




    # Muestra el histograma
    plt.show()

