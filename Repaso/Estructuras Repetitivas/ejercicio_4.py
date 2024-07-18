"""
Ejercicio 4
Mostrar la suma de los números pares desde el 1 hasta el 10.
"""

contador = 0
acumulador_pares = 0

while contador < 10:
    if (contador+1) % 2 == 0:
        acumulador_pares += contador+1
    contador += 1

print(f"Suma de números pares: {acumulador_pares}")