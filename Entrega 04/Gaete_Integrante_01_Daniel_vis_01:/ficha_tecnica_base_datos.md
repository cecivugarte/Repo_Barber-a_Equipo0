
# Ficha Técnica de la Base de Datos

## 1. Características de los Datos
La base de datos utilizada contiene información sobre el número de barberías registradas en diversas localidades para los años 2019 y 2022. Específicamente, la base permite identificar tendencias de crecimiento o disminución en cada localidad, lo que la hace adecuada para un análisis comparativo y de evolución temporal.

### Tipo de Datos
- **Estructura**: Archivo delimitado por punto y coma (`;`) en formato CSV.
- **Volumen**: Incluye más de 50 localidades.
- **Frecuencia**: Datos correspondientes a dos años: 2019 y 2022.

---

## 2. Variables Incorporadas

| Variable             | Descripción                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| `Localidad`           | Nombre de la comuna o localidad donde se registraron barberías.            |
| `Barberías 2019`      | Número total de barberías registradas en el año 2019.                      |
| `Barberías 2022`      | Número total de barberías registradas en el año 2022.                      |
| `Cambio (%)`          | Porcentaje de cambio relativo en el número de barberías entre 2019 y 2022. |

---

## 3. Observaciones

### Limpieza de los Datos
- Se detectaron algunas localidades con datos faltantes o inconsistencias que fueron eliminadas para garantizar la calidad del análisis.
- Los valores numéricos fueron convertidos al tipo `int` para asegurar cálculos precisos en el cambio porcentual.

### Potencial de la Base
- **Fortalezas**:
  - Permite analizar tendencias específicas por localidad.
  - Es fácil de procesar gracias a su estructura bien definida.
- **Limitaciones**:
  - No incluye detalles adicionales como población, ingresos o factores socioeconómicos que podrían enriquecer el análisis.
  - Los datos abarcan únicamente dos años, lo que limita la capacidad de observar tendencias a largo plazo.

---

Esta ficha técnica resume las características, variables y observaciones clave sobre la base de datos utilizada, destacando su utilidad para el análisis del sector de barberías.
