import time

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n* factorial(n - 1)

valores = [50, 100, 150, 200]
tiempos = []

for valor in valores:
    inicio = time.time()
    resultado = factorial(valor)
    fin = time.time()
    tiempos.append(fin - inicio)

print(tiempos)
