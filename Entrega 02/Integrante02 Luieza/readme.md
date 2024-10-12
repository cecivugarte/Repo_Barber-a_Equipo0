# Limpieza de Datos de Barberías en Estación Central

## Descripción del Proyecto
El objetivo de este paso dentro del proyecto, es preparar los datos para ser analizados y así encontrar tendencias que nos ayuden a comprobar nuestra hipótesis acerca de una causalidad entre los factores expuestos.

## Proceso de Limpieza de Datos
El proceso de limpieza de datos se llevó a cabo siguiendo varios pasos clave:

1. **Carga de datos:** Se cargaron los datos desde un archivo CSV en un DataFrame de Pandas.
2. **Exploración inicial:** Se realizó un análisis exploratorio para identificar la estructura de los datos y detectar problemas como valores faltantes, formatos incorrectos o inconsistencias.
3. **Transformaciones necesarias:**
   - Se convirtieron las columnas con valores numéricos en formato de texto a formato numérico adecuado, utilizando funciones de Pandas como `str.replace()` y `astype()`.
   - Se manejaron los valores faltantes de manera adecuada, ya sea eliminando registros con datos faltantes o rellenando esos valores con promedios u otros criterios.
4. 

### Herramientas Utilizadas
- **Pandas:** Se utilizó la biblioteca Pandas de Python para limpiar los datos.
- **Jupyter Notebook/Google Colaboratory:** 

## Fuentes de Datos Utilizadas
- **Archivo CSV de Barberías:** Los datos fueron extraídos de un archivo CSV que contiene información relevante sobre barberías en Puente Alto, incluyendo nombre, dirección, y datos económicos.

### Justificación de las Fuentes
- **Fiabilidad:** El archivo CSV se obtuvo de una fuente confiable que recopila datos sobre negocios en la región.
- **Relevancia:** La información se acerca a las preocupaciones del conjunto de vecinos del sector, dado que existen múltiples delitos que se asocian a la proliferación de estos puestos.


## Preguntas que se Pueden Responder con la Base de Datos Limpia
1.¿En qué año se crearon más barberías en Estación Central?
2.¿Cuántos trabajadores declaran tener dichas empresas?
3.¿ Se justifica la cantidad de empresas en base a la densidad poblacional de Estación Central?


