# Proceso de visualizaciones
*Por Cecilia Vidal*


### Proceso
El proceso de selección de datos fue en base a las bases de datos ya creadas.
1. Al tener las bases de datos en csv, se analizó a simple vista las inquietudes que surgían al verla. 


Llegué a la primera cuestión de: ¿Qué comunas han experimentado mayores cambios de criminalidad en los últimos años y cómo varían en comparación a su densidad poblacional?


Esta primera pregunta me llevó a Chat GPT para pedirle ayuda en la realización del código en un cuaderno de Google Collab utilizando Altair. Una vez con el gráfico listo, sentí que no respondía todo lo que quería saber. (Esta visualización está en la carpeta "otros/")


Volví al inicio y llegué a una segunda pregunta, que cumplía con mis expectativas: ¿Existe relación entre la densidad de barberías y el aumento de casos policiales en las comunas?


Repetí los pasos anteriores y recurrí a Chat GPT, quien no me ayudó como esperaba.


Junto a las profesoras logré llegar al gráfico final.


2. El segundo paso, fue hacer el gráfico en el cuaderno de Google Collab, esto, como ya mencioné, con la ayuda de mis profesoras.


Primero se tuvo que limpiar la base de datos ya hecha dado que tenía puntos para marcar unidades de mil, cosa que afectaba los resultados esperados. Se ajustó a columnas de datos eliminando lo anterior mencionado. También se reemplazó las comas de los decimales por puntos en la dimensión Superficie BCN (KM2).


Una vez eso listo, se hizo un gráfico por año que demuestra la relación ya sugerida. Finalmente, esos se juntaron para poder compararlos y realizar un análisis más certero.


3. Momento de exportar todo en los formatos correspondientes.


Para exportar recurrí a Chat GPT quien me explico un código que me ayudaba a conseguir el html, me sirvió, pero solo en un gráfico que decidí borrar. Después logré descargar en PNG, pero yo necesitaba JPG. Con un segundo código pude transformarlo en el mismo cuaderno.


4. Realizar la crónica


Para este paso más creativo, analicé cuáles eran las comunas que más destacan. Esto siempre relacionando el número de barberías con la cantidad de criminalidad. Las elegidas fueron: Santiago, Puente Alto y Maipú.


En base a eso decidí redactar una crónica algo más introspectiva al lector.


5. Pasar las conclusiones a HTML


Cree un archivo html y agregue los códigos pertinentes. No sabía como escribir junto a una imagen, por ende le pregunte Chat GPT el código. 

### Decisiones
El primer cuadro que realice siento que nos ayuda a llegar a ciertas conclusiones de nuestra hipótesis. Es por eso que decidí dejarlo igual en el repositorio y cuaderno para utilizarlo en un futuro cercano. Aun así, para fines de esta entrega, preferí utilizar el segundo gráfico que compara las el número de barberías con el de criminalidad por comuna y año.
### Preguntas
Son muchas las preguntas que surgen al analizar la base de datos inicial, y, del mismo modo, son muchas las que salen del gráfico Altair.


1. ¿Existe una relación entre la densidad de barberías y el número de aumento de casos policiales en algunas comunas?


2. ¿Ha disminuido o aumentado el número de barberías en las zonas con mayor criminalidad?


3. ¿Qué ocurre en la comuna de Santiago? (comuna que el gráfico muestra como la que tiene mayor número de casos policiales manteniendo una densidad relativamente alta de barberías).


4. ¿Por qué Las Condes destaca? ¿Qué ocurre en esa comuna?


5. ¿Qué otros factores influyen en el aumento de criminalidad? ¿Son las barberías realmente las responsables de esto?
