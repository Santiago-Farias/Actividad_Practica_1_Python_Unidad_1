"""
Ejercicio 3
Mostrar la suma de los números desde el 1 hasta el 10.
"""

contador = 0
acumulador = 0

while contador < 10:
    acumulador += contador + 1
    contador += 1

print(f"Suma total: {acumulador}")