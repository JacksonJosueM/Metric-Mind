import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos desde un archivo CSV
df = pd.read_csv('C:/xampp/mysql/data/bdit.csv')

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Asumiendo que 'Fecha' es una columna de tipo datetime, convertimos a tipo datetime si no lo es
df['Fecha'] = pd.to_datetime(df['Fecha'])

# Reducción de fechas con muestreo
sampled_df = df.resample('M', on='Fecha').mean()  # Cambia 'M' a otra frecuencia si deseas otro tipo de muestreo

# Ajusta el tamaño de la figura
plt.figure(figsize=(12, 8))

# Grafica la línea con estilo distintivo
sns.lineplot(x=sampled_df.index, y='NumeroTurista', data=sampled_df, linewidth=2.5, marker='o', markersize=8)

# Agrega etiquetas y título
plt.title('Número de Turistas a lo Largo del Tiempo')
plt.xlabel('Fecha')
plt.ylabel('Número de Turistas')

# Formatea las fechas en el eje x si es necesario
# plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m-%d'))

# Agrega grid
plt.grid(True)

# Muestra la gráfica
plt.xticks(rotation=45)  # Rota las etiquetas de fecha para mayor legibilidad
plt.tight_layout()  # Ajusta el diseño para evitar recortes
plt.show()
