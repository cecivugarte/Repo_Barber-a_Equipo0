# README: Proceso de Creación de "Barberías y Criminalidad: Entre Navajas y Sombras"

---

## Identificación del Tema y Construcción de la Hipótesis

### Decisión inicial
El objetivo era abordar un tema urbano que combinara datos duros con una narrativa interesante. Detectamos un fenómeno llamativo: el aumento de barberías en comunas con altos índices de criminalidad. Esto derivó en la hipótesis de que podría existir una correlación entre ambos fenómenos, con barberías funcionando potencialmente como fachadas para actividades ilícitas.

### Preguntas planteadas
1. ¿Qué comunas muestran este patrón?  
2. ¿Qué evidencia concreta respalda esta hipótesis?  
3. ¿Cómo estructurar la narrativa y los datos para contar esta historia de forma comprensible y atractiva?

---

## Recolección de Datos

### Fuentes consultadas
- CEAD (Centro de Estudios y Análisis del Delito) para estadísticas de criminalidad.  
- SII (Servicio de Impuestos Internos) para datos sobre barberías registradas.  
- Reportajes y noticias relacionados con el cierre de barberías implicadas en actividades ilícitas.

### Desafíos
Los datos estaban en formatos variados, por lo que fue necesario unificar y limpiar la información. Las estadísticas de criminalidad estaban organizadas por año y comuna, mientras que los registros de barberías eran acumulativos.

### Soluciones
- Convertimos los datos en archivos CSV para facilitar su manejo.
- Enfocamos el análisis en comunas representativas como Santiago, Puente Alto y Providencia.

---

## Diseño de la Narrativa

### Enfoque
Construir una historia que combinara datos y narrativa de forma equilibrada, logrando captar la atención del lector sin perder rigor analítico.

### Estructura narrativa
1. **Introducción:** Presentación del fenómeno y planteamiento de la hipótesis.  
2. **Un problema en aumento:** Análisis de los datos de criminalidad.  
3. **Todos necesitan un corte:** Contexto sobre el auge de barberías.  
4. **Entre navajas y sombras:** Exploración de la posible relación entre ambos fenómenos.  

### Estilo
Usamos un lenguaje accesible, reforzado por preguntas retóricas en los títulos para invitar a la reflexión.

---

## Creación de Visualizaciones

### Herramientas
Utilizamos `Plotly` para generar gráficos interactivos que enriquecieran la experiencia del lector. Esto permitió identificar tendencias de manera visual y accesible.

### Visualizaciones diseñadas
1. **Casos Policiales por Comuna (2019-2024):**  
   Muestra cómo la criminalidad ha evolucionado en Santiago, Puente Alto y Providencia.
2. **Número de Barberías (2019-2022):**  
   Expone el crecimiento desproporcionado de barberías en ciertas comunas.
3. **Gráficos combinados (Santiago, Puente Alto, Providencia):**  
   Comparan el aumento de barberías y casos policiales en las comunas seleccionadas.

### Desafíos técnicos
- Ajustar los colores y el tamaño de los gráficos para mejorar la legibilidad.
- Manejar datos faltantes, interpolando valores donde era necesario.

### Decisión clave
Cada visualización debía responder una pregunta específica y estar alineada con el flujo narrativo.

---

## Diseño Web

### Objetivo
Crear una página intuitiva y visualmente atractiva que guiara al lector a través de la historia.

### Elementos destacados
- **Menú lateral:** Permitió la navegación directa entre secciones.  
- **Encabezado llamativo:** Incluyó un subtítulo intrigante: *"Entre Navajas y Sombras"*.  
- **Diseño minimalista:** Usamos tipografías modernas y fondos neutros para centrar la atención en el contenido.  
- **Integración de gráficos:** Los gráficos fueron incrustados como iframes para mantener su interactividad.

### Desafíos
Lograr un equilibrio entre texto y visualizaciones para evitar una sobrecarga de información en las secciones.

---

## Revisión y Ajustes Finales

### Tareas realizadas
- Revisión del contenido textual para garantizar coherencia y claridad.  
- Refinamiento de las leyendas y etiquetas de los gráficos para mejorar su comprensión.  
- Inclusión de un gráfico adicional para Providencia, dada su relevancia como caso atípico.

# Responsabilidad en la WebStory del Encargo 06

| Elemento   | Daniel Gaete                         | Cecilia Vidal                        | Vicente Lueiza                   |
|------------|--------------------------------------|--------------------------------------|-----------------------------------|
| Redacción de Código | Trabajó en el desarrollo y ajuste del código para las visualizaciones. | Participó en la creación y depuración del código. | Apoyo menor en validación técnica. |
| Creación de Visualizaciones | Trabajó en la generación y ajuste de gráficos interactivos. | Colaboró en la creación de gráficos y análisis de datos. | Validación de datos utilizados. |
| Diseño | Desarrolló el diseño general de la WebStory. | Apoyo en la presentación visual de gráficos. | Apoyo estético menor. |
| Redacción de Contenido | Colaboración menor en la estructura narrativa. | Apoyo en revisiones de texto. | Principal encargado de la redacción y narrativa textual. |

Cada integrante aportó desde su experiencia en las diferentes etapas del desarrollo, asegurando que el resultado final reflejara un trabajo colaborativo y bien estructurado.




## Reflexión Final

Este proyecto fue un desafío que combinó análisis de datos con storytelling visual. Aprendimos que:  
1. Los datos son más efectivos cuando se contextualizan dentro de una narrativa clara.  
2. Las visualizaciones interactivas mejoran la comprensión y el impacto de la historia.  
3. Un diseño limpio y bien estructurado es crucial para guiar al lector a través de temas complejos.  

El resultado final es una webstory que no solo informa, sino que invita a reflexionar sobre las dinámicas sociales y económicas detrás de un fenómeno urbano aparentemente trivial.

