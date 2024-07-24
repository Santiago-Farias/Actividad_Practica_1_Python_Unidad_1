# ENTREGADO
"""
Ejercicio Integrador N°1 Completo
Permitir que el usuario ingrese todos los números que desee. Los mismos deben estar
comprendidos entre -10000 y 10000, y deben ser distintos de 0. Determinar:
a. La suma acumulada de los números negativos.
b. La suma acumulada de los números positivos.
c. La cantidad de números negativos ingresados.
d. El promedio de los números positivos.
e. El número positivo más grande.
f. El porcentaje de números negativos ingresados, respecto del total de ingresos.
"""

numero = 0
numeros_cantidad_total = 0

negativos_suma = 0
negativos_contador = 0
negativos_porcentaje = 0

positivos_suma = 0
positivos_contador = 0
positivos_promedio = 0.0

positivo_maximo = 0
valor_minimo = 0

opcion = ""

bandera = True

while True:

    numero = int(input("Ingrese un número (entre -10000 y 10000): "))

    # Validar el ingreso del número.
    while numero < -10000 or numero > 10000 or numero == 0:
        numero = int(input("Número inválido.\nIngrese nuevamente un número (entre -10000 y 10000): "))

    # Calcular la suma acumulada y la cantidad ingresada.
    if numero < 0:
        negativos_suma += numero
        negativos_contador += 1
    if numero > 0:
        positivos_suma += numero
        positivos_contador += 1
        if numero > positivo_maximo:
            positivo_maximo = numero


    # Consultar la continuidad del programa.
    opcion = input("Desea seguir (si/no)")
    if opcion.lower() == "no":
        break

# Calcular promedio números positivos.
positivos_promedio = positivos_suma / positivos_contador

# Calcular procentaje de negativos ingresados.
numeros_cantidad_total = positivos_contador + negativos_contador
negativos_porcentaje = (negativos_contador / numeros_cantidad_total) * 100

# Mostrar por pantalla resultados.
print(f""" 
Suma acumulada de números positivos: {positivos_suma}
El positivo mas grande es: {positivo_maximo}
Promedio de los números positivos: {round(positivos_promedio, 2)}
-
Suma acumulada de números negativos: {negativos_suma}
Cantiad de negativos ingresados: {negativos_contador}
Porcentaje de números negativos ingresados: {round(negativos_porcentaje, 2)}
""")