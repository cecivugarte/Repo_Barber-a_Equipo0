# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Csmkmf4G9GiW5KfrvI-lWLzgw2GS2-u_
"""

# Importa las bibliotecas necesarias
import pandas as pd

# Carga el archivo CSV con el delimitador correcto y la codificación adecuada
file_path = '/content/BARBERIAS ESTACION CENTRAL LIMPIO.csv'
df = pd.read_csv(file_path, delimiter=';', encoding='ISO-8859-1')

# Visualiza las primeras filas del DataFrame
df.head()