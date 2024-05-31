import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos desde un archivo CSV
df = pd.read_csv('C:/xampp/mysql/data/bdit.csv')

# Mostrar las primeras filas para inspeccionar el DataFrame
print(df.head())

# Verificar la información básica del DataFrame
print(df.info())

# Describir las estadísticas básicas de las columnas numéricas
print(df.describe())

# Buscar valores nulos
print(df.isnull().sum())

# Opcional: Imputar o eliminar valores nulos
df.fillna(method='ffill', inplace=True)  # Ejemplo de imputación hacia adelante
