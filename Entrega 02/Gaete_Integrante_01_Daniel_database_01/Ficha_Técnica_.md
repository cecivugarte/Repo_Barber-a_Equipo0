
# Ficha Técnica del Dataset

## 1. Características de los datos:
- **Tamaño del dataset**: 16 filas y 27 columnas.
- **Tipos de datos**:
  - **Numéricos**: Variables como "Número de empresas", "Número de trabajadores", "Renta neta informada" están representadas principalmente por números enteros.
  - **Categóricos**: Variables como "Comuna del domicilio", "Actividad económica", "Subrubro económico", "Rubro económico" son de tipo texto (objeto).
  - Algunas variables, como las ventas anuales y rentas netas, están en formato de texto, pero contienen valores numéricos en unidades financieras (UF).
- **Fuente y calidad de los datos**: No hay valores faltantes en el conjunto de datos, pero hay posibles errores en el formato de las columnas financieras (valores numéricos con comas).

## 2. Alcance metodológico:
- **Metodología de recopilación**: los datos provienen de registros administrativos relacionados con actividades económicas, empresas y trabajadores en Chile.
- **Posibles enfoques de análisis**:
  - **Análisis descriptivo**: Para resumir las características generales de las empresas, ventas, y composición de los trabajadores (género, número, y rentas).
  - **Regresiones o correlaciones**: Para estudiar las relaciones entre ventas, número de empleados, y otras variables económicas con fenomenos como la ola migratoria y el aumento de actividades relacionadas con el lavado de activos.
 

## 3. Variables incorporadas:
Algunas variables clave incluyen:
- **Año Comercial (Numérico)**: Año de referencia.
- **Comuna del domicilio (Categórico)**: Localización de la empresa.
- **Número de empresas (Numérico)**: Cantidad de empresas en cada localidad.
- **Ventas anuales en UF (Texto)**: Ventas totales.
- **Número de trabajadores (Numérico)**: Trabajadores registrados.
- **Renta neta informada en UF (Texto)**: Ingresos netos.
- **Número de trabajadores por género (Numérico)**: Clasificación por género de los trabajadores.
- Existen múltiples columnas relacionadas con trabajadores ponderados y por género.

## 4. Descripción del propósito de la base de datos:
- **Contexto**: El dataset parece estar orientado al análisis de empresas asociadas a servicios de peluquería y barbería en una región específica (Puente Alto), con información detallada sobre su actividad económica, ventas y composición de empleados por género.
- **Variable de interés principal**: Ventas anuales, numero de empleados, renta neta, etc. Para visualizar el crecimiento de la barbería como negocio en los ultimos años.

## 5. Observaciones sobre la base de datos:
- **Valores faltantes**: No se observan valores faltantes.
- **Posibles errores**: Las columnas relacionadas con ventas y rentas están en texto, pero deberían ser numéricas para facilitar el análisis.
- **Limitaciones**: La muestra es pequeña (solo 16 registros), lo que limita el alcance de análisis estadísticos robustos, considerando que debe haber un mayor número de barberías pero no estan registradas
