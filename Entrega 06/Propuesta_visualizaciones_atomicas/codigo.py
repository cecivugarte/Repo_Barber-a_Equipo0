import pandas as pd
import plotly.express as px
import random

def Grafico1():
    ####Cambio en criminalidad en comunas y densidad poblacional##### GRAFICO1
    # Leer el archivo CSV con el separador adecuado
    data_path = r'C:\Users\karti\Desktop\PaginaCecy\Graficos\Grafico1-3.csv'
    df = pd.read_csv(data_path, sep=',', engine='python')  # Usar ';' como separador si es necesario

    # Generar una paleta más amplia de colores usando colores RGB aleatorios
    def generate_distinct_colors(num_colors):
        random.seed(42)  # Para reproducir los colores siempre iguales
        colors = []
        for _ in range(num_colors):
            # Generar un color aleatorio en formato RGB
            color = f'rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})'
            colors.append(color)
        return colors
    
    # Obtener colores únicos para cada comuna
    comunas_unicas = df['Comuna'].unique()
    colores = generate_distinct_colors(len(comunas_unicas))  # Generar tantos colores como comunas

    # Crear un diccionario para asignar cada comuna a un color distinto
    color_map = {comuna: colores[i] for i, comuna in enumerate(comunas_unicas)}

    # Seleccionar las columnas relevantes (años y comuna)
    columns_to_melt = [
        'Cant Casos Policiales 2019', 'Cant Casos Policiales 2020', 
        'Cant Casos Policiales 2021', 'Cant Casos Policiales 2022', 
        'Cant Casos Policiales 2023', 'Cant Casos Policiales 2024'
    ]

    # Convertir las columnas de años a formato largo
    df_long = pd.melt(
        df,
        id_vars=['Comuna'],  # Columna que se mantiene fija
        value_vars=columns_to_melt,  # Columnas a descomponer
        var_name='Año',  # Nueva columna para los años
        value_name='Casos Policiales'  # Nueva columna para los valores
    )

    # Limpiar los nombres de los años
    df_long['Año'] = df_long['Año'].str.extract('(\d+)')  # Extraer solo el año como texto
    df_long['Año'] = df_long['Año'].astype(int)  # Convertir el año a número

    # Verificar data
    #print("Datos transformados:")
    #print(df_long.head())

    # Generar el gráfico interactivo con Plotly
    fig1 = px.bar(
        df_long,
        x="Año",
        y="Casos Policiales",
        color="Comuna",
        title="Casos Policiales por Comuna y Año",
        labels={"Casos Policiales": "Casos Policiales", "Año": "Año", "Comuna": "Comuna"},
        color_discrete_map=color_map 
    )

    fig1.update_layout(
    title=dict(
        text="Casos Policiales por Comuna y Año",
        font=dict(size=24, color='#824C2F', family='Bebas Neue, sans-serif', weight='bold'),
        x=0.5
    ),
    xaxis_title=dict(
        text="Año",
        font=dict(size=16, color='#824C2F', family='Bebas Neue, sans-serif', weight='bold')
    ),
    yaxis_title=dict(
        text="Casos Policiales",
        font=dict(size=16, color='#824C2F', family='Bebas Neue, sans-serif', weight='bold')
    ),
    legend=dict(
        title=dict(
            text="Comuna",
            font=dict(size=14, color='#824C2F', family='Bebas Neue, sans-serif', weight='bold')
        ),
        font=dict(color='#824C2F', family='Bebas Neue, sans-serif', weight='bold')
    ),
    font=dict(
        family='Bebas Neue, sans-serif'  # Cambiar la tipografía global a Bebas Neue
    ),
    yaxis=dict(
        tickformat='.0f'  # Mostrar números completos sin "k"
    ),
    template="plotly",
    plot_bgcolor="rgba(0, 0, 0, 0)",
    paper_bgcolor="rgba(0, 0, 0, 0)"
)
    # Mostrar el gráfico
    fig1.show()

    # Guardar el gráfico en un archivo HTML
    output_path = r'C:\Users\karti\Desktop\PaginaCecy\static\Grafico1.html'
    fig1.write_html(output_path)
    print(f"Gráfico guardado como archivo HTML en: {output_path}")
#Grafico1()

def Grafico2():
    # Cargar los datos reorganizados
    file_path = file_path = r'C:\Users\karti\Desktop\PaginaCecy\Graficos\Grafico2.csv'  # Cambia por la ruta de tu archivo
    data = pd.read_csv(file_path, engine="python", sep=";")

    # Generar una paleta más amplia de colores usando colores RGB aleatorios
    def generate_distinct_colors(num_colors):
        random.seed(42)  # Para reproducir los colores siempre iguales
        colors = []
        for i in range(num_colors):
            # Generar un color aleatorio en formato RGB
            color = f'rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})'
            colors.append(color)
        return colors

    # Obtener colores únicos para cada comuna
    comunas_unicas = data['Comunas'].unique()
    colores = generate_distinct_colors(len(comunas_unicas))  # Generar tantos colores como comunas

    # Crear un diccionario para asignar cada comuna a un color distinto
    color_map = {comunas: colores[i] for i, comunas in enumerate(comunas_unicas)}
    
    # Transformar los datos al formato largo para Plotly
    data_long = data.melt(
        id_vars=["Comunas"],
        value_vars=["Suma_de_Numero_de_Barberias_2019", "Suma_de_Numero_de_Barberias_2022"],  # Columnas a transformar
        var_name="Año",
        value_name="Número de Barberías"
    )

    # Limpiar la columna "Año" para que contenga solo los años
    data_long["Año"] = data_long["Año"].str.extract("(\d{4})")

    # Crear el gráfico de burbujas
    fig2 = px.scatter(
        data_long,
        x="Comunas",
        y="Número de Barberías",
        size="Número de Barberías",
        color="Comunas",
        animation_frame="Año",
        title="Evolución del número de barberías por comuna (2019-2022)",
        labels={"Número de Barberías": "Número de Barberías", "Comunas": "Comunas", "Año": "Año"},
        template="plotly_white",
        height=600,  # Ajuste opcional de altura
        color_discrete_map=color_map  # Asignar colores únicos
    )

    # Personalizar el diseño
    fig2.update_layout(
        title=dict(
            text="Evolución del número de barberías por comuna (2019-2022)",
            font=dict(size=24, family="Bebas Neue, sans-serif", color="#824C2F", weight="bold"),
            x=0.5  # Centrar el título
        ),
        xaxis_title=dict(
            text="Comunas",
            font=dict(size=16, family="Bebas Neue, sans-serif", color="#824C2F", weight="bold")
        ),
        yaxis_title=dict(
            text="Número de Barberías",
            font=dict(size=16, family="Bebas Neue, sans-serif", color="#824C2F", weight="bold")
        ),
        legend_title=dict(
            text="Comunas",
            font=dict(size=14, family="Bebas Neue, sans-serif", color="#824C2F", weight="bold")
        ),
        legend=dict(
            font=dict(color="#824C2F", size=12, family="Bebas Neue, sans-serif", weight="bold")
        ),
        yaxis=dict(range=[0, data["Suma_de_Numero_de_Barberias_2022"].max() * 1.1]),
        paper_bgcolor='rgba(0,0,0,0)',  # Fondo de la página transparente
        plot_bgcolor='rgba(0,0,0,0)',  # Fondo del gráfico transparente
        showlegend=True  # Mostrar leyendas
    )
    # Personalizar el diseño
    fig2.update_traces(marker=dict(opacity=0.7, line=dict(width=1, color='DarkSlateGrey')))

    fig2.show()
    # Guardar el gráfico interactivo en un archivo HTML
    output_path = r'C:\Users\karti\Desktop\PaginaCecy\static\Grafico2.html'
    fig2.write_html(output_path)

    print(f"Gráfico guardado en: {output_path}")
#Grafico2()

def Grafico3():
    import pandas as pd
    import plotly.express as px

    # Cargar los datos
    file_path = r'C:\Users\karti\Desktop\PaginaCecy\Graficos\Grafico1-3.csv'
    data = pd.read_csv(file_path)


    # Transformar datos a formato largo para manejar múltiples años y tipos de datos
    map_data_long = data.melt(
        id_vars=['Comuna', 'Latitud', 'Longitud'],
        value_vars=[
            'Cant Casos Policiales 2019', 'Cant Casos Policiales 2020',
            'Cant Casos Policiales 2021', 'Cant Casos Policiales 2022',
            'Numero de Barberias 2019', 'Numero de Barberias 2020',
            'Numero de Barberias 2021', 'Numero de Barberias 2022'
        ],
        var_name='Indicador',
        value_name='Cantidad'
    )

    # Extraer el año y el tipo de indicador
    map_data_long['Año'] = map_data_long['Indicador'].str.extract(r'(\d{4})')
    map_data_long['Tipo'] = map_data_long['Indicador'].str.extract(r'(Cant Casos Policiales|Numero de Barberias)')

    # Combinar ambas métricas en un único dataframe por año
    combined_data = map_data_long.pivot_table(
        index=["Comuna", "Latitud", "Longitud", "Año"],
        columns="Tipo",
        values="Cantidad",
        aggfunc="sum",
        fill_value=0
    ).reset_index()

    # Crear el gráfico interactivo usando hover_data directamente
    fig = px.scatter_mapbox(
        combined_data,
        lat="Latitud",
        lon="Longitud",
        color="Comuna",  # Color único para cada comuna
        size="Cant Casos Policiales",  # Tamaño de burbuja basado en casos policiales
        hover_name="Comuna",
        hover_data={
            "Año": True,  # Mostrar el año
            "Cant Casos Policiales": True,  # Mostrar casos policiales
            "Numero de Barberias": True,  # Mostrar barberías
        },
        animation_frame="Año",  # Agregar la barra para navegar entre años
        mapbox_style="carto-positron",
        size_max=20,
        title="Casos Policiales y Barberías por Comuna (2019-2022)"
    )

    # Personalizar el diseño para que el fondo sea transparente
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",  # Fondo del área fuera del gráfico
        plot_bgcolor="rgba(0,0,0,0)",    # Fondo del área del gráfico
        title=dict(
            text="Casos Policiales y Barberías por Comuna (2019-2022)",
            font=dict(size=24, family="Bebas Neue, sans-serif", color="#824C2F", weight="bold"),
            x=0.5  # Centrar el título
        ),
        legend_title=dict(
            text="Comuna",
            font=dict(size=16, family="Bebas Neue, sans-serif", color="#824C2F", weight="bold")  # Título de la leyenda en negrita
        ),
        legend=dict(
            font=dict(size=14, family="Bebas Neue, sans-serif", color="#824C2F", weight="bold")  # Etiquetas de la leyenda en negrita
        )
    )

    # Mostrar el gráfico directamente
    fig.show()

    # Guardar el gráfico en un archivo HTML
    output_path = r'C:\Users\karti\Desktop\PaginaCecy\static\Grafico3.html'
    fig.write_html(output_path)
    print(f"Gráfico guardado como archivo HTML en: {output_path}")
#Grafico3()

def GraficoSantiago():
    import pandas as pd
    import plotly.graph_objects as go

    # Cargar el archivo CSV
    file_path = r'C:\Users\karti\Desktop\PaginaCecy\Graficos\Barberias_casos_policiales_santiago.csv'  # Asegúrate de colocar el archivo en la misma carpeta o ajustar la ruta
    data_santiago = pd.read_csv(file_path)

        # Reorganizar los datos
    años_santiago = ['2019', '2020', '2021', '2022']
    barberias_santiago = data_santiago.iloc[0, 1:5].values
    casos_policiales_santiago = data_santiago.iloc[0, 5:9].values

    # Crear el gráfico con ejes separados
    fig_santiago = go.Figure()

    # Agregar las barras para los casos policiales
    fig_santiago.add_trace(go.Bar(
        x=años_santiago, 
        y=casos_policiales_santiago, 
        name='Casos Policiales',
        marker_color='#EFE095',
        yaxis='y1'
    ))

    # Agregar la línea para las barberías (eje secundario)
    fig_santiago.add_trace(go.Scatter(
        x=años_santiago, 
        y=barberias_santiago, 
        mode='lines+markers', 
        name='Barberías',
        line=dict(color='#824C2F', width=2),
        yaxis='y2'
    ))

    # Personalizar el diseño
    fig_santiago.update_layout(
        title=dict(
            text='Variación de Barberías y Casos Policiales en Santiago (2019-2022)',
            font=dict(size=24, family='Bebas Neue, sans-serif', weight='bold', color='#824C2F'),
            x=0.5  # Centrar el título
            ),
        xaxis=dict(
            title='Año',
            tickfont=dict(size=12, family='Bebas Neue, sans-serif', weight='bold'),  # Números del eje X en negrita
            titlefont=dict(size=14, weight='bold')  # Título del eje X en negrita
            ),
        yaxis=dict(
            title='Casos Policiales',
            titlefont=dict(color='#EFE095', size=14, weight='bold'),  # Título del eje Y en negrita
            tickfont=dict(color='#EFE095', size=12, family='Bebas Neue, sans-serif', weight='bold')  # Números del eje Y en negrita
        ),
        yaxis2=dict(
            title='Barberías',
            titlefont=dict(color='#824C2F', size=14, weight='bold'),  # Título del eje secundario en negrita
            tickfont=dict(color='#824C2F', size=12, family='Bebas Neue, sans-serif', weight='bold'),  # Números del eje secundario en negrita
            overlaying='y',
            side='right'
        ),
        legend=dict(
            title=dict(
                text='Información',
                font=dict(size=14, weight='bold')  # Título de la leyenda en negrita
            ),
            font=dict(size=12, family='Bebas Neue, sans-serif', weight='bold')  # Etiquetas de la leyenda en negrita
            ),
        template='plotly_white',
        paper_bgcolor="rgba(0,0,0,0)",  # Fondo del área fuera del gráfico
        plot_bgcolor="rgba(0,0,0,0)",    # Fondo del área del gráfico
    )

    # Mostrar el gráfico
    fig_santiago.show()
    # Guardar el gráfico en un archivo HTML
    output_path = r'C:\Users\karti\Desktop\PaginaCecy\static\Grafico_Santiago.html'
    fig_santiago.write_html(output_path)
    print(f"Gráfico guardado como archivo HTML en: {output_path}")
#GraficoSantiago()

def  GraficoProvidencia():
    import pandas as pd
    import plotly.graph_objects as go

    # Cargar el archivo CSV de Providencia
    file_path_providencia = r'C:\Users\karti\Desktop\PaginaCecy\Graficos\Barberias_casos_policiales_providencia.csv'
    data_providencia = pd.read_csv(file_path_providencia)

    # Reorganizar los datos
    años_providencia = ['2019', '2020', '2021', '2022']
    barberias_providencia = data_providencia.iloc[0, 1:5].values
    casos_policiales_providencia = data_providencia.iloc[0, 5:9].values

    # Crear el gráfico con ejes separados
    fig_providencia_secondary = go.Figure()

    # Agregar las barras para los casos policiales
    fig_providencia_secondary.add_trace(go.Bar(
        x=años_providencia, 
        y=casos_policiales_providencia, 
        name='Casos Policiales',
        marker_color='#EFE095',
        yaxis='y1'
    ))

    # Agregar la línea para las barberías (eje secundario)
    fig_providencia_secondary.add_trace(go.Scatter(
        x=años_providencia, 
        y=barberias_providencia, 
        mode='lines+markers', 
        name='Barberías',
        line=dict(color='#824C2F', width=2),
        yaxis='y2'
    ))

    # Personalizar el diseño
    fig_providencia_secondary.update_layout(
        title=dict(
            text='Variación de Barberías y Casos Policiales en Providencia (2019-2022)',
            font=dict(size=24, family='Bebas Neue, sans-serif', weight='bold', color='#824C2F'),
            x=0.5  # Centrar el título
            ),
        xaxis=dict(
            title='Año',
            tickfont=dict(size=12, family='Bebas Neue, sans-serif', weight='bold'),  # Números del eje X en negrita
            titlefont=dict(size=14, weight='bold')  # Título del eje X en negrita
        ),
        yaxis=dict(
            title='Casos Policiales',
            titlefont=dict(color='#EFE095', size=14, weight='bold'),  # Título del eje Y en negrita
            tickfont=dict(color='#EFE095', size=12, family='Bebas Neue, sans-serif', weight='bold')  # Números del eje Y en negrita
        ),
        yaxis2=dict(
            title='Barberías',
            titlefont=dict(color='#824C2F', size=14, weight='bold'),  # Título del eje secundario en negrita
            tickfont=dict(color='#824C2F', size=12, family='Bebas Neue, sans-serif', weight='bold'),  # Números del eje secundario en negrita
            overlaying='y',
            side='right'
        ),
        legend=dict(
            title=dict(
                text='Información',
                font=dict(size=14, weight='bold')  # Título de la leyenda en negrita
            ),
            font=dict(size=12, family='Bebas Neue, sans-serif', weight='bold')  # Etiquetas de la leyenda en negrita
            ),
        template='plotly_white',
        paper_bgcolor="rgba(0,0,0,0)",  # Fondo del área fuera del gráfico
        plot_bgcolor="rgba(0,0,0,0)",    # Fondo del área del gráfico
    )

    # Mostrar el gráfico
    fig_providencia_secondary.show()

    # Guardar el gráfico en un archivo HTML
    output_path = r'C:\Users\karti\Desktop\PaginaCecy\static\Grafico_Providencia.html'
    fig_providencia_secondary.write_html(output_path)
    print(f"Gráfico guardado como archivo HTML en: {output_path}")
#GraficoProvidencia()

def GraficoPuenteAlto():
    import pandas as pd
    import plotly.graph_objects as go

    # Cargar el archivo CSV de Puente Alto
    file_path_puentealto = r'C:\Users\karti\Desktop\PaginaCecy\Graficos\Barberias_casos_policiales_puentealto.csv'
    data_puentealto = pd.read_csv(file_path_puentealto)

        # Reorganizar los datos
    años_puentealto = ['2019', '2020', '2021', '2022']
    barberias_puentealto = data_puentealto.iloc[0, 1:5].values
    casos_policiales_puentealto = data_puentealto.iloc[0, 5:9].values

    # Crear el gráfico con ejes separados
    fig = go.Figure()

    # Agregar las barras para los casos policiales
    fig.add_trace(go.Bar(
        x=años_puentealto, 
        y=casos_policiales_puentealto, 
        name='Casos Policiales',
        marker_color='#EFE095',
        yaxis='y1'
    ))

    # Agregar la línea para las barberías (eje secundario)
    fig.add_trace(go.Scatter(
        x=años_puentealto, 
        y=barberias_puentealto, 
        mode='lines+markers', 
        name='Barberías',
        line=dict(color='#824C2F', width=2),
        yaxis='y2'
    ))

    # Personalizar el diseño
    fig.update_layout(
        title=dict(
            text='Variación de Barberías y Casos Policiales en Puente Alto (2019-2022)',
            font=dict(size=20, family='Bebas Neue, sans-serif', weight='bold', color='#824C2F'),
            x=0.5  # Centrar el título
        ),
        xaxis=dict(
            title='Año',
            tickfont=dict(size=12, family='Bebas Neue, sans-serif', weight='bold'),  # Números del eje X en negrita
            titlefont=dict(size=14, weight='bold')  # Título del eje X en negrita
            ),
        yaxis=dict(
            title='Casos Policiales',
            titlefont=dict(color='#EFE095', size=14, weight='bold'),  # Título del eje Y en negrita
            tickfont=dict(color='#EFE095', size=12, family='Bebas Neue, sans-serif', weight='bold')  # Números del eje Y en negrita
        ),
        yaxis2=dict(
            title='Barberías',
            titlefont=dict(color='#824C2F', size=14, weight='bold'),  # Título del eje secundario en negrita
            tickfont=dict(color='#824C2F', size=12, family='Bebas Neue, sans-serif', weight='bold'),  # Números del eje secundario en negrita
            overlaying='y',
            side='right'
        ),
        legend=dict(
            title=dict(
                text='Información',
                font=dict(size=14, weight='bold')  # Título de la leyenda en negrita
            ),
            font=dict(size=12, family='Bebas Neue, sans-serif', weight='bold')  # Etiquetas de la leyenda en negrita
        ),
        template='plotly_white',
        paper_bgcolor="rgba(0,0,0,0)",  # Fondo del área fuera del gráfico
        plot_bgcolor="rgba(0,0,0,0)",    # Fondo del área del gráfico
    )

    # Mostrar el gráfico
    fig.show()  

    # Guardar el gráfico en un archivo HTML
    output_path = r'C:\Users\karti\Desktop\PaginaCecy\static\Grafico_PuenteAlto.html'
    fig.write_html(output_path)
    print(f"Gráfico guardado como archivo HTML en: {output_path}")
#GraficoPuenteAlto()