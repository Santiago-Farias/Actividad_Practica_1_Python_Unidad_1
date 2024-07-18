"""
Ejercicio 6
Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma
de los números ingresados y el promedio de los mismos.
"""
suma_numeros = 0
promedios_numeros = 0
opcion = 0
contador_ciclos = 0

while opcion != 1:
    numeros = int(input("Ingrese un número: "))
    opcion = int(input("¿Desea seguir ingresando números? (0 seguir, 1 detener)\n"))
    suma_numeros += numeros
    contador_ciclos += 1

promedios_numeros = suma_numeros / contador_ciclos

print(f"\nSuma de números: {suma_numeros}\nPromedio: {promedios_numeros}")