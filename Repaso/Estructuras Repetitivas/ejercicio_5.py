"""
Ejercicio 5
Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio.
Mostrar por pantalla.
"""

contador = 0
numeros = 0
suma_numeros = 0
promedio_numeros = 0

while contador < 5:
    numeros = int(input(f"Ingrese el número N° {contador+1}: "))
    suma_numeros += numeros
    contador += 1

promedio_numeros = suma_numeros / contador

print(f"\nSuma de números: {suma_numeros} \nPromedio de números: {promedio_numeros}")