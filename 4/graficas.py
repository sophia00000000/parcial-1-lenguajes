import matplotlib.pyplot as plt
import numpy as np

# Valores de entrada
valores = [50, 100, 150, 200]
c = [0.000005, 0.000005, 0.000012, 0.000008]
py = [1.1444091796875e-05, 1.5974044799804688e-05, 3.838539123535156e-05, 4.124641418457031e-05]

plt.figure(figsize=(8,5))
plt.plot(valores, c, label='C (Compilado)')
plt.plot(valores, py, label='Python (Interpretado)')

# Configuración de la gráfica
plt.xlabel("n")
plt.ylabel("Tiempo (segundos)")
plt.legend()
plt.grid(True)
plt.show()
