# Ficha Técnica: Base de datos Barberías en Región Metropolitana
*Cecilia Vidal*




### 1. Características de los datos:
- **Tamaño del dataset:** Tiene 22 columnas y 53 filas.
- **Tipos de datos:**
  - **Numéricos:** Variales representadas por números enteros, son la Superficie en kilómetros cuadrados de cada comuna, Densidad poblacional comunal, la cantidad de barberías por comuna, la cantidad de casos policiales y el índice de criminalidad. Todos estos datos medidos desde el año 2019, prepandemia, hasta los últimos datos publicados, 2022 (En el caso de la cantidad de casos policiales es hasta el 2024). Esto con el fin de evidenciar el aumento considerando el deceso que la pandemia provocó.
  - **Categóricos:** Las variables en formato texto - objeto - son las Comunas que componen la Región Metropolitana y también las provincias.
- **Fuente y calidad de los datos:** No hay valores faltantes en el conjunto de datos, pero hay posibles errores en la columna Densidad poblacional dada la antigüedad de los datos publicados por INE respecto a los últimos Censos.




### 2. Alcance metodológico:
- **Metodología de recopilación:** Los datos recopilados vienen de INE, Censo, registros policiales rescatados de la página Cead, Biblioteca del Congreso Nacional y registros administrativos sobre la cantidad de barberías en sus respectivas comunas.
- **Posibles enfoques de análisis:**
  - **Análisis descriptivo:** A simple vista, se aprecian datos sobre la densidad poblacional, índice delictual, cantidad de barberías y superficie que cubre cada comuna. Todo esto sobre la Región Metropolitana y en un rango desde el 2019 al 2023.
  - **Regresiones o correlaciones:** Estos datos servirán para comparar la densidad poblacional e índice de criminalidad con la cantidad de barberías por comuna. Además, se puede evidenciar los aumentos de barberías prepandemia y pospandemia, pudiendo calcular la relación del número de barberías versus la cantidad poblacional.
  - **Segmentación:** Estos análisis nos derivarán a conclusiones que comprueben o refuten nuestra hipótesis.




Los datos mencionados fueron obtenidos, en su mayoría, por medio de la técnica webscraping. La información sobre la superficie y la cantidad de habitantes fueron encontradas en la Biblioteca del Congreso Nacional. También el índice criminal fue obtenido desde la página Cead de Carabineros, ahí conseguí la cantidad de casos policiales para luego llegar al índice de criminalidad comunal por medio de una fórmula (cantidad de casos policiales sobre la cantidad de habitantes, todo por año). Finalmente, la densidad poblacional se consiguió por medio de otra fórmula (cantidad de habitantes sobre los kilómetros cuadrados que cubre la comuna). Dado que estos últimos datos no son exactos, los consideramos como una aproximación para nuestro análisis final.




Por otra parte, la cantidad de barberías por comuna fue obtenida de una base de datos ya estipulada en Servicio de Impuestos Internos SII, esta base habla sobre las Estadísticas de Empresa. Esto considera el número de empresas, montos de venta, número de trabajadores, zona geográfica, entre otras variables.




### 3. Variables incorporadas: 
Las variables utilizadas son:
- **Comuna (Categórico):** Refiere a la comuna que refieren los siguientes datos, es por eso que esta variable, en la base de datos, se encuentra en las filas.
- **Provincia (Categórico):** Da cuenta de las provincias a las que corresponde cada comuna con el fin de poder conseguir conclusiones más amplias si necesitamos.
- **Superficie (Numérico):** Da cuenta de la cantidad de terreno demográfico que la comuna cubre.
- **Cantidad de Habitantes (Numérico):** Es el número de habitantes según el último Censo publicado en el 2017.
- **Densidad Poblacional (Numérico):** Se calcula por medio de la fórmula cantidad de habitantes sobre kilómetro cuadrado.
- **Cantidad de Barberías (Numérico):** La suma de barberías que hay en la zona con relación al año analizado.
- **Variación entre años por barbería:** Es cuánto ha variado en porcentaje entre años la cantidad de barberías por comuna.
- **Cantidad de casos policiales:** Son los casos policiales anuales de cada comuna.
- **Índice de Criminalidad (Numérico):** Se obtiene por medio de la fórmula casos policiales sobre cada 100.000 habitantes.




Recordemos que estos datos son desde el año 2019 hasta los últimos publicados, 2023. Además, todos son sobre las comunas que componen la Región Metropolitana.




### 4. Observaciones sobre la base de datos:
- Al realizar la investigación y categorización de esta en una base de datos, pudimos evidenciar que hay algunos que no son exactos dada la antigüedad de la última publicación oficial. El Censo, que nos muestra la cantidad de habitantes para luego obtener la densidad poblacional, no es exacto por ende pudiese haber **posibles errores**.
- **Limitaciones:** La pandemia provocó un deceso en todo tipo de negocios, incluyendo las peluquerías, por ende puede nublar el análisis de aumento. Es por eso que incluimos el año previo a su inicio para así comparar, pero aun así no se ha vuelto a la anormalidad previa de la pandemia e incluso quizá jamás se vuelva a ello. A pesar de esto, buscamos ser precisos y transparentes con la obtención de las muestras.
- **Valores faltantes:** No se observan.




### 5. Descripción del propósito de la base de datos:
Con esta base de datos se espera analizar y relacionar el aumento de la cantidad de barberías versus el índice de criminalidad y esto sumado a la superficie que cubre y densidad poblacional que habita, tanto en la Región Metropolitana como en la comuna que veamos alguna irregularidad. Así se espera obtener números aún más precisos, como la cantidad de barberías cada 10 personas por comunas o la cantidad de crímenes cada 10 barberías.




- Nuestra variable principal de interés son tres: densidad poblacional, cantidad de barberías e índice criminal. Además, también nos importa la superficie dado que así veremos la irregularidad de la cantidad de barberías excesiva en algunas comunas.




# Diccionario de datos




### Comuna
- **Descripción:** Comunas que componen la Región Metropolitana.
- **Tipo de dato:** Categórico.
- **Formato esperado:** Nombres de las comunas de la Región Metropolitana.
- **Ejemplo de valor:** San Miguel.


### Provincia
- **Descripción:** Es la Provincia a la que corresponde cada región.
- **Tipo de dato:** Categórico.
- **Formato esperado:** Provincias que subdividen la Región Metropolitana y contienen las comunas.
- **Ejemplo de valor:** Provincia de Talagante.


### Superficie
- **Descripción:** Kilómetros que la comuna cubre dentro de la Región Metropolitana.
- **Tipo de dato:** Numérico.
- **Formato esperado:** Números que representen el terreno que le corresponde a distintas comunas de la Región Metropolitana.
- **Ejemplo de valor:** 80,8.


### Cantidad de habitantes
- **Descripción:** Cantidad de personas de la comuna dentro de la Región Metropolitana según el último Censo publicado en 2017.
- **Tipo de dato:** Numérico.
- **Formato esperado:** Números que representen el terreno que le corresponde a distintas comunas de la Región Metropolitana.
- **Ejemplo de valor:** 90.201.


### Densidad poblacional
- **Descripción:** Densidad de personas que componen la comuna de la Región Metropolitana.
- **Tipo de dato:** Numérico.
- **Formato esperado:** Valores que representen la densidad de habitantes por año.
- **Ejemplo de valor:** 783.




### Número de barberías
- **Descripción:** Cantidad de barberías que hay por comunas de la Región Metropolitana.
- **Tipo de dato:** Numérico.
- **Formato esperado:** Números que representen cuantas barberías hay por año estipulado.
- **Ejemplo de valor:** 16.


### Variación entre cantidad de barberías
- **Descripción:** Se calcula por medio de la fórmula valor inicial menos el valor que se quiere comparar sobre el valor inicial, es decir (x-y)/x.
- **Tipo de dato:** Numérico.
- **Formato esperado:** Es un porcentaje de variación.
- **Ejemplo de valor:** 4%.


### Cantidad de casos policiales
- **Descripción:** Son los casos policiales ocurridos anualmente por comuna de la Región Metropolitana. Se obtuvo por medio del Centro de Estudios y Análisis del Delito CEAD.
- **Tipo de dato:** Numérico.
- **Formato esperado:** Números que corresponden a los casos policiales comunales de la Región Metropolitana.
- **Ejemplo de valor:** 5.108.


### Índice de criminalidad
- **Descripción:** Índice que indica la cantidad de crimen por comuna de la Región Metropolitana del año 2023. También se calcula por medio de una fórmula: casos policiales por cada 100.000 habitantes
- **Tipo de dato:** Numérico.
- **Formato esperado:** Valores que indique dicha tasa por comuna de la Región Metropolitana.
- **Ejemplo de valor:** 6.742.

