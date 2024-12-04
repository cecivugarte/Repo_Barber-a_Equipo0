# Documentación del Proceso de Visualización

## 1. ENTREGA 4

Mediante esta visualización se busca entregar una idea acerca de la evolución en las cifras de peluquerías a lo largo de los años .

## 2. Explicación del Proceso de Visualización

### Paso 1: Selección de los Datos

 
- **Fuente de los Datos**: Provienen del Servicio de Impuestos Internos, corresponden a cifras oficiales de empresas registradas.
- **Formato de los Datos**: En este caso, estamos trabajando con un archivo CSV.
- 

### Paso 2: Procesamiento de los Datos

Lo primero que hice fue seleccionar los datos que necesitaba para aportar a la narrativa de la crónica.

- **Limpiar los Datos**: 
Considerando que la base de datos original incluyó todas las empresas de Chile registradas entre los años 2005 y 2021,sí tuve que limpiar los datos, seleccionando las cifras más generales que fueran más útiles, todo ello sumando las columnas. Por lo mismo tuve que colocar esa suma a otro excel para tener una mayor claridad, además el archivo original era tan grande que era imposible trabajar de una manera adecuada.
- **Transformación de Datos**: Tuve que sumar el número de peluquerías según años
- **Selección de Variables**: Sí, decidí mostrar una evolución de registro de empresas a lo largo de los años, por lo mismo, los índices de actividad económica y años fueron claves.
### Paso 3: Creación de la Visualización

Explica cómo creaste la visualización utilizando la librería Altair.

- **Tipo de Visualización**: ¿Qué tipo de gráficos creaste? (gráfico de barras, de líneas, dispersión, etc.)
- **Decisiones de Diseño**: ¿Qué decisiones tomaste respecto al diseño del gráfico (colores, etiquetas, ejes, etc.)?
- **Interactividad**: Si la visualización tiene características interactivas (filtros, leyendas interactivas), explícalo aquí.

### Paso 4: Exportación y Presentación

En formato imagen , de manera complementaria al texto de la crónica

## 3. Descripción de la Base de Datos Utilizada

- **Nombre del Archivo CSV**: [PUB_COMU_ACT(1).csv]
- **Descripción de las Variables**: Mediante .
- **Proceso de Limpieza y Transformación**:Tuve que filtrar año por año, la actividad económica de interés y separar año por año para obtener cifras exclusivas a aquel año.
## 4. Ejemplos de Preguntas que Responde la Visualización
¿Cómo era la tendencia incripción de peluquerías durante la última década?
¿En qué año hubo un mayor aumento? 


## 5. Conclusiones

Durante el 2019 hubo un aumento a lo menos llamativo, durante el 2020, en el período de la pandemia decayeron las cifras, pero como luego veremos, dichos números se recuperarán.

## 6. Ficha Técnica

### Características de los Datos

- **Número de filas**: [1048574]
- **Número de columnas**: [27]
- **Fecha de actualización**: [2021]
- **Fuente**: [Servicios de Impuestos internos]

### Variables Incorporadas

| Variable | Descripción |
|----------|-------------|
| [Actividad Eonómica] | [Sirve para describir a qué se dedica una empresa, en ese sentido ayuda a filtrar la información ] |
| [Número de empresas] | [Ilustra cuantas empresas fueron registradas en un período de tiempo] |
| [Número de trabajadores dependientes informados
] | [Esta variable , luego será importante, dado que existe una discordancia entre lo que supone la cantidad de trabajadores dependientes informados (que últimamente tiende a bajar) y el número de barberías creadas (que tiende a subir)] |
| ...      | ...         |

### Observaciones

Cualquier observación que sea relevante acerca de la base de datos, como problemas encontrados durante el análisis o limitaciones de los datos.

## 7. Archivos Relacionados

A continuación, se listan los archivos incluidos en el proyecto:

- **Archivo CSV**: [PUB_COMU_ACT(1).csv]
- **Visualización Final**: [visualization.pngn]
- **Crónica**: [ENTREGA 4.md o similar]
- **Scripts de Análisis**: [nombre_del_script_notebook.py o .ipynb]

