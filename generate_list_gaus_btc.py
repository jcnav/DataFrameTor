import numpy as np

# Parámetros de la distribución
media = 250000  # Media de la distribución
desviacion_estandar = 100000  # Desviación estándar de la distribución
cantidad_numeros = 100  # Cantidad de números aleatorios a generar

# Genera la lista de números aleatorios
numeros_aleatorios = np.random.normal(media, desviacion_estandar, cantidad_numeros)

# Asegura que los números estén dentro del rango [500, 500000]
numeros_aleatorios = np.clip(numeros_aleatorios, 500, 500000)

# Convierte los números a enteros
numeros_aleatorios = numeros_aleatorios.astype(int)

# Imprime la lista de números aleatorios
print(numeros_aleatorios)

for i in numeros_aleatorios:
    print(i)