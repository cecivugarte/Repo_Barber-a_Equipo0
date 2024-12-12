# Explicación de las Visualizaciones Atómicas

---

## 1. Gráfico General: Casos Policiales por Comuna (Grafico1.html)

**Código:**  
El código utilizado para generar este gráfico está disponible en el archivo `Graficos.py`, en la función `Grafico1`.

**Base de Datos Utilizada:**  
- `Grafico1-3.csv`: Contiene los datos de casos policiales por comuna y año.

**Descripción de la Imagen:**  
Un gráfico de barras apiladas que muestra la evolución de los casos policiales desde 2019 hasta 2024 en comunas como Santiago, Puente Alto y Providencia.

**Explicación de la Elección:**  
Este gráfico permite visualizar de manera clara cómo los índices delictuales han aumentado a lo largo de los años en distintas comunas. La representación apilada facilita la comparación tanto temporal como geográfica.

---

## 2. Gráfico de Barberías: Número de Barberías por Comuna (Grafico2.html)

**Código:**  
El código utilizado para generar este gráfico está disponible en el archivo `Graficos.py`, en la función `Grafico2`.

**Base de Datos Utilizada:**  
- `Grafico2.csv`: Incluye datos del número de barberías registradas por comuna en 2019 y 2022.  
- `Daniel_database_ocupada.csv`: Base complementaria que permitió verificar los registros de barberías.

**Descripción de la Imagen:**  
Un gráfico de burbujas animado que representa el crecimiento del número de barberías en las comunas seleccionadas. Las burbujas cambian de tamaño según el crecimiento de barberías en cada año.

**Explicación de la Elección:**  
Este gráfico fue elegido para destacar visualmente las comunas con mayor incremento en el número de barberías. La animación agrega dinamismo y facilita la comparación temporal.

---

## 3. Gráficos Combinados por Comuna

### a. Santiago (Grafico_Santiago.html)

**Código:**  
El código utilizado para este gráfico está disponible en el archivo `Graficos.py`, en la función `GraficoSantiago`.

**Base de Datos Utilizada:**  
- `Barberias_casos_policiales_santiago.csv`: Contiene datos de casos policiales y número de barberías en Santiago.  
- `202410-sociedades-por-fecha-rut-constitucion_v2.csv`: Base que complementó los datos sobre constitución de sociedades relacionadas con barberías.

**Descripción de la Imagen:**  
Un gráfico combinado con barras que representan los casos policiales y una línea que muestra el número de barberías por año.

**Explicación de la Elección:**  
Este gráfico destaca cómo el aumento de barberías coincide con el incremento de los casos policiales en Santiago, permitiendo observar la relación entre ambas variables.

---

### b. Providencia (Grafico_Providencia.html)

**Código:**  
El código utilizado para este gráfico está disponible en el archivo `Graficos.py`, en la función `GraficoProvidencia`.

**Base de Datos Utilizada:**  
- `Barberias_casos_policiales_providencia.csv`: Incluye datos de criminalidad y barberías en Providencia.  
- `202410-sociedades-por-fecha-rut-constitucion_v2.csv`: Datos complementarios sobre sociedades comerciales.

**Descripción de la Imagen:**  
Un gráfico combinado similar al de Santiago, pero centrado en Providencia.

**Explicación de la Elección:**  
Providencia, una comuna con características atípicas, muestra cómo las barberías y la criminalidad han crecido simultáneamente. Este gráfico destaca esta correlación.

---

### c. Puente Alto (Grafico_PuenteAlto.html)

**Código:**  
El código utilizado para este gráfico está disponible en el archivo `Graficos.py`, en la función `GraficoPuenteAlto`.

**Base de Datos Utilizada:**  
- `Barberias_casos_policiales_puentealto.csv`: Datos de barberías y casos policiales en Puente Alto.  
- `202410-sociedades-por-fecha-rut-constitucion_v2.csv`: Información adicional sobre constitución de sociedades.

**Descripción de la Imagen:**  
Un gráfico combinado que muestra las tendencias de criminalidad y crecimiento de barberías en Puente Alto.

**Explicación de la Elección:**  
Puente Alto, como una de las comunas más densamente pobladas, ofrece una perspectiva única sobre las dinámicas urbanas y su relación con el fenómeno analizado.

---

## Conclusión sobre las Visualizaciones

Cada visualización se diseñó cuidadosamente para responder preguntas clave planteadas en el análisis. Los datos proporcionados por las bases como `Daniel_database_ocupada.csv` y `202410-sociedades-por-fecha-rut-constitucion_v2.csv` enriquecieron las estadísticas iniciales, permitiendo una exploración más profunda de las correlaciones entre el aumento de barberías y los índices delictuales. Estas representaciones gráficas refuerzan la narrativa y ayudan al lector a comprender visualmente los hallazgos presentados en la WebStory.
