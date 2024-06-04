import pandas as pd
import matplotlib.pyplot as plt

# Ruta del archivo subido
file_path = '/mnt/data/file-OIdyXwDE4NHCW7zYp6IV2xvU'

# Cargar los datos
data = pd.read_csv('C:/xampp/mysql/data/bdit.csv')
import pandas as pd
import matplotlib.pyplot as plt

# Ruta del archivo subido
file_path = '/mnt/data/file-OIdyXwDE4NHCW7zYp6IV2xvU'

# Cargar los datos
data =pd.read_csv('C:/xampp/mysql/data/bdit.csv')

# Convertir la columna de fecha al formato datetime
data['Fecha'] = pd.to_datetime(data['Fecha'])

# Ordenar los datos por fecha
data = data.sort_values('Fecha')

# Gráfica 1: Número de Turistas a lo largo del tiempo
plt.figure(figsize=(10, 5))
plt.plot(data['Fecha'], data['NumeroTurista'], marker='o', color='b')
plt.title('Número de Turistas a lo Largo del Tiempo')
plt.xlabel('Fecha')
plt.ylabel('Número de Turistas')
plt.xticks(rotation=45)  # Rotar las etiquetas del eje x
plt.grid(True)
plt.show()

# Gráfica 2: Gasto Promedio por Turista a lo largo del tiempo
plt.figure(figsize=(10, 5))
plt.plot(data['Fecha'], data['GastoPromediaPorTurista'], marker='o', color='g')
plt.title('Gasto Promedio por Turista a lo Largo del Tiempo')
plt.xlabel('Fecha')
plt.ylabel('Gasto Promedio')
plt.xticks(rotation=45)  # Rotar las etiquetas del eje x
plt.grid(True)
plt.show()

# Gráfica 3: Ingreso de Negocios Locales a lo largo del tiempo
plt.figure(figsize=(10, 5))
plt.plot(data['Fecha'], data['IngrecioNegociolocales'], marker='o', color='r')
plt.title('Ingreso de Negocios Locales a lo Largo del Tiempo')
plt.xlabel('Fecha')
plt.ylabel('Ingreso')
plt.xticks(rotation=45)  # Rotar las etiquetas del eje x
plt.grid(True)
plt.show()

# Gráfica 4: Turistas Internacionales a lo largo del tiempo
plt.figure(figsize=(10, 5))
plt.plot(data['Fecha'], data['TuristaInternacionales'], marker='o', color='c')
plt.title('Turistas Internacionales a lo Largo del Tiempo')
plt.xlabel('Fecha')
plt.ylabel('Número de Turistas Internacionales')
plt.xticks(rotation=45)  # Rotar las etiquetas del eje x
plt.grid(True)
plt.show()

# Gráfica 5: Porcentaje de Tasa de Empleo en Turismo a lo largo del tiempo
plt.figure(figsize=(10, 5))
plt.plot(data['Fecha'], data['PorcentajeTasaEmpleoTurismo'], marker='o', color='m')
plt.title('Porcentaje de Tasa de Empleo en Turismo a lo Largo del Tiempo')
plt.xlabel('Fecha')
plt.ylabel('Porcentaje de Empleo')
plt.xticks(rotation=45)  # Rotar las etiquetas del eje x
plt.grid(True)
plt.show()

# Gráfica 6: Porcentaje de Índice de Desarrollo de Infraestructura a lo largo del tiempo
plt.figure(figsize=(10, 5))
plt.plot(data['Fecha'], data['PorcentajeIndiceDesarrolloInfraestructura'], marker='o', color='y')
plt.title('Porcentaje de Índice de Desarrollo de Infraestructura a lo Largo del Tiempo')
plt.xlabel('Fecha')
plt.ylabel('Porcentaje de Desarrollo')
plt.xticks(rotation=45)  # Rotar las etiquetas del eje x
plt.grid(True)
plt.show()
