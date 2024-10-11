# Limpieza de datos Región Metropolitana

### Descripción del proyecto
Este proyecto se centra en la limpieza de datos de un conjunto de información, en específico sobre la comparación población, cantidad de barberías e índice criminal de cada comuna que compone la Región Metropolitana en un margen de 5 años - del 2019 a los últimos datos publicados -.


El objetivo de esta recopilación y limpieza de datos es poder conseguir una base de datos limpia para facilitar nuestro análisis. Poder comparar los números y sacar conclusiones que respalden nuestra hipótesis, para así ser lo más preciso y transparentes con la información. 


### Proceso de limpieza de datos
La presente base de datos se completó recopilando información - webscraping - por medio de INE, SII y CEAD.


Como los datos no fueron recopilados desde una base previa deben ser limpiados, eso se realizó según los siguientes pasos.


1. **Buscar la información:** En informes anuales de INE, SII y CEAD para rescatar los datos de la densidad poblacional, cantidad de barberías por comuna y la tasa de criminalidad anual - esta última con el fin de transformarla en un índice de criminalidad.


2. **Exploración inicial y carga de datos:** Analizamos los datos encontrados en dichos informes y los colocamos uno a uno en las filas y columnas correspondientes. 
Basándonos en esto se puede comenzar a ver si se necesita más información o incluso poder sacar pronósticos de conclusiones. 
Se identifica la estructura de los datos para detectar problemas como valores faltantes, formatos incorrectos o inconsistencias para modificarlos y adaptarlos.


3. **Ordenación de datos:**  En este caso, se recopiló información por cada comuna que compone la Región Metropolitana. En las finas se encontrarán los nombres de dichas comunas y en las columnas estarán las variables: Superficie, Densidad Poblacional, Número de barberías e Índice Criminal.
- 
  - **Columna A:** Tiene las comunas de la Región Metropolitana, para ubicarlas en filas.
  - **Columna B:** Contiene la clasificación de las comunas según su provincia para que, al analizar, se pueda comparar según esta.
  - **Columna C:** Agrupa los datos numéricos de superficie de cada comuna.
  - **Columna D:** Tiene la cantidad de población según el último Censo publicado en el 2017.
  - **Columna E:** Contiene la densidad población, dato numérico, de cada comuna. Este dato es incierto por la antigüedad de la publicación de Censo.
  - **Columna F, G, I y J:** Va la cantidad de barberías, estas columnas son muchas dado que se analizará desde el año 2019 hasta la última publicación oficial en SII (2022).
  - **Columna H y K:** Es la variación porcentual de la cantidad de barberías entre el año 2019-2020 (H) y 2021 y 2022 (K).
  - **Columna L, M, O, Q, S y U:** Corresponde a la cantidad de casos policiales desde el año 2019 al año 2024. Este último es una aproximación, por ende no es un dato exacto.
  - **Columna N, P, R y T:** Son las variaciones porcentuales de los casos policiales entre años (2019-2020; 2020-2021; 2021-2022; 2022-2023).
  - **Columna V:** Esta última columna contiene el índice criminal que se obtiene con los casos policiales divididos en la cantidad de habitantes. También podría considerarse imprecisa por el hecho de que el último censo fue en 2017.

4. **Excel y verificación final:** Una vez pasado todos los datos a formato cvs en excel, se revisó el DataFrame limpio para garantizar que todos los datos estuvieran en el formato correcto y que no existieran inconsistencias.


### Herramientas utilizadas:
- **Pandas - Google Colaboratory**: Su uso fue con el objetivo de analizar que los datos estuvieran en un estado puro y adecuado, y también realizar su limpieza si fuese necesario.
- **Excel**: Esta herramienta cumplió con ordenar los datos para visualizarlos de mejor forma y poder sacar conclusiones.


### Fuentes de datos
- [Servicio de Impuestos Internos SII](https://www.sii.cl/sobre_el_sii/estadisticas_de_empresas.html)
Este nos sirvió para recopilar la información de la cantidad de barberías en cada comuna al rededor de los años - 2019 a 2022.

- [Biblioteca del Congreso Nacional de Chile](https://www.bcn.cl/siit/nuestropais/nuestropais/region13/)
Por medio de esta fuente, conseguimos de manera manual los datos de superficie y último Censo.

- [Centro de Estudios y Análisis del Delito](https://cead.spd.gov.cl/estadisticas-delictuales/)
Esta página nos otorgó los casos policiales anuales por comuna.


### Preguntas que se pueden responder con la base de datos


1. Si la pandemia provocó un descenso en la cantidad de barberías, una vez terminada, ¿ya se ve un nuevo aumento?


2. ¿Cuál es la comuna con mayor índice de criminalidad? ¿Calza con la de mayor cantidad de barberías?


3. ¿La comuna con menor densidad poblacional cuantas barberías tiene? Si el número es alto, ¿cuántas barberías hay cada 10 personas?


4. A pesar de la disminución que la pandemia provocó en la cantidad de barberías, ¿hubo alguna anormalidad en ese periodo?


Este Read Me tiene objetivo la comprensión completa del proceso de recopilación de datos para crear la nueva base.