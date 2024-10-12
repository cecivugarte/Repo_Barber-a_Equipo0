
# Ficha Técnica del Dataset

## 1. Características de los datos:
- **Tamaño del dataset**: 16 filas y 27 columnas.
- **Tipos de datos**:
  - **Numéricos**: Variables como, "Número de empresas", "Renta neta informada" están especificados con números enteros.
  - **Categóricos**: Variables como "Comuna del domicilio", "Actividad económica", "Subrubro económico", "Rubro económico" son de tipo texto (objeto).
  
- **Fuente y calidad de los datos**: No hay valores faltantes en el conjunto de datos.

## 2. Alcance metodológico:
- **Metodología de recopilación**: Los datos corresponden a cifras oficiales acerca de las empresas registradas en el país.
- **Posibles enfoques de análisis**:
  - **Análisis descriptivo**: Para resumir las características generales de las empresas, ventas, y composición de los trabajadores (género, número, y rentas).
  - **Regresiones o correlaciones**: Para estudiar las relaciones entre ventas, número de empleados, y otras variables económicas.
  - **Segmentación**: Se podrían realizar análisis de clúster para agrupar empresas según características comunes.

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
- **Contexto**: La base de datos nos entrega información para que podamos ver las tendencias que ha tenido este rubro en un margen de años definido.
- **Variable de interés principal**: Número de empresas, ventas anuales y número de empleados.

## 5. Observaciones sobre la base de datos:
- **Valores faltantes**: No se observan valores faltantes.
- **Posibles errores**: Las columnas relacionadas con ventas y rentas están en texto, pero deberían ser numéricas para facilitar el análisis.
- **Limitaciones**: Una de las posibles problemáticas que presenta esta base de datos , se relaciona con nuestro estudio y es que, es posible que no todas las barberías/peluquerías de la comuna, se encuentren en el registro.
