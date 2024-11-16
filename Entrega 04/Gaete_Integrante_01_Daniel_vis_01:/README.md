# Análisis de la Transformación de las Barberías (2019-2022)

## 1. Nombre del Proyecto
**La Transformación de las Barberías (2019-2022)**

## 2. Proceso de Visualización

### Paso 1: Selección del Tema
Elegimos analizar el cambio en el número de barberías entre 2019 y 2022 debido a que las barberías han evolucionado significativamente como negocios locales. Queríamos identificar tendencias en localidades específicas y cuantificar su impacto en el mercado.

### Paso 2: Carga de Datos
La base de datos utilizada se cargó desde un archivo en formato CSV, el cual contenía información sobre el número de barberías en distintas localidades de un país para los años 2019 y 2022. La selección del CSV se basó en la disponibilidad de datos específicos, estructurados y relevantes para analizar el crecimiento del sector.

### Paso 3: Limpieza y Preparación de Datos

- **Identificación de las columnas relevantes**:
  - Extraímos tres columnas principales:
    - **Localidad**: Nombre de la comuna o localidad.
    - **Barberías 2019**: Número total de barberías en 2019.
    - **Barberías 2022**: Número total de barberías en 2022.

- **Conversión de datos**:
  - Convertimos las columnas de valores numéricos (Barberías 2019 y Barberías 2022) al tipo `int`, manejando errores como datos faltantes o no numéricos.

- **Cálculo del cambio porcentual**:
  - Creamos una nueva columna **Cambio (%)** para representar el crecimiento o disminución relativa del número de barberías entre 2019 y 2022:
    
    \[\text{Cambio (%) = } \frac{\text{Barberías 2022} - \text{Barberías 2019}}{\text{Barberías 2019}} \times 100\]

- **Selección de los datos más relevantes**:
  - Ordenamos las localidades por el número de barberías en 2022 y seleccionamos las cinco con mayor cantidad para incluir en la visualización.

### Paso 4: Creación del Gráfico

- **Decisión del tipo de visualización**:
  - Seleccionamos un gráfico de barras vertical porque es intuitivo para comparar datos numéricos entre categorías (localidades) y destacar cambios porcentuales.

- **Generación del gráfico**:
  - Usamos `Matplotlib` para generar el gráfico, ajustando colores y diseño para mejorar la estética y la legibilidad.

- **Guardado del gráfico**:
  - Guardamos el gráfico en formato PNG (`barberias_cambio_porcentual.png`) para integrarlo posteriormente en el diseño HTML.

### Paso 5: Diseño de la Diapositiva de la Historia

- Creamos un archivo HTML para presentar la visualización y agregar una narrativa breve (microhistoria) sobre el crecimiento de las barberías.
- Utilizamos estilos personalizados en CSS para estructurar y estilizar el diseño:
  - Sección izquierda para el gráfico.
  - Sección derecha para el texto explicativo.
- Destacamos datos clave en la narrativa para captar la atención del lector.

## 3. Base de Datos Utilizada

### Descripción del CSV
El archivo utilizado contiene tres columnas principales:

- **Localidad**: Nombres de las comunas o localidades donde se registraron barberías.
- **Barberías 2019**: Cantidad total de barberías en el año 2019.
- **Barberías 2022**: Cantidad total de barberías en el año 2022.

### Procesamiento de los Datos

- **Carga del archivo CSV**:
  - El archivo se cargó utilizando `pandas` y se especificó el delimitador correcto (`;`) y la codificación (`latin1`) para manejar caracteres especiales.

- **Validación y limpieza**:
  - Filtramos las filas que contenían datos inconsistentes o faltantes.
  - Estandarizamos los valores numéricos para garantizar la correcta interpretación.

- **Selección de datos**:
  - Limitamos los datos a las cinco localidades con más barberías en 2022, ya que representan las zonas de mayor interés para la visualización.

### Justificación de la Selección
El CSV fue elegido por su relevancia y claridad. Contenía información específica y numérica que permite un análisis directo del crecimiento del sector de las barberías, un tema que combina economía local y tendencias sociales.

## 4. Preguntas que Responde la Visualización

1. **¿Dónde se ha registrado el mayor crecimiento en el número de barberías entre 2019 y 2022?**
   - La visualización muestra que Las Condes tuvo un crecimiento porcentual destacado del 45.28%.

2. **¿Qué localidades lideran en número total de barberías en 2022?**
   - La visualización revela que Santiago, Providencia y Las Condes tienen la mayor cantidad de barberías.

3. **¿Cuál es la tendencia general del sector?**
   - El gráfico sugiere un crecimiento positivo en la mayoría de las localidades, reflejando una posible tendencia social hacia el cuidado personal y los servicios de barbería.

4. **¿Existen localidades con menor crecimiento relativo?**
   - Sí, por ejemplo, Puente Alto muestra un crecimiento menor (7.64%) en comparación con otras localidades principales.

5. **¿Qué factores podrían explicar el crecimiento de las barberías en ciertas localidades?**
   - La visualización puede ser utilizada para explorar relaciones con factores como densidad poblacional, ingresos promedio o cambios culturales.

## 5. Conclusión
Este proyecto ofrece una visión clara del cambio en el número de barberías entre 2019 y 2022, destacando tendencias clave y estimulando preguntas sobre el impacto de las barberías en la economía local. La narrativa combinada con la visualización busca no solo informar, sino también involucrar al espectador en la historia detrás de los datos.

## Archivos Incluidos

- **barberias_cambio_porcentual.png**: Gráfico de barras generado.
- **barberias_analysis.html**: Archivo HTML con el diseño de la diapositiva.
- **README.md**: Documentación completa del proyecto.

Con este enfoque, el proyecto no solo responde preguntas sobre el crecimiento de las barberías, sino que también sirve como ejemplo para analizar otros sectores en expansi
