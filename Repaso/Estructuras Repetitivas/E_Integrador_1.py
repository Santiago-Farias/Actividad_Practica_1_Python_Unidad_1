""" 
Ejercicio Integrador 1

1. Permitir que el usuario ingrese todos los números que desee.
Determinar:
a. La suma acumulada de los números negativos.
b. La suma acumulada de los números positivos.
c. La cantidad de números negativos ingresados.
d. El promedio de los números positivos.
f. El porcentaje de números negativos ingresados, respecto del total de ingresos.
"""

acumulador_numeros_negativos = 0
contador_numeros_negativos = 0

acumulador_numeros_positivos = 0
contador_numeros_positivos = 0
promedio_numeros_positivos = 0

cantidad_total_numeros = 0

porcentaje_numeros_negativos = 0

opcion = "si"

while opcion.lower() != "no":
    numero = int(input("Ingrese un número: "))
    opcion = input("¿Desea seguir?\n")
    if numero < 0:
        acumulador_numeros_negativos += numero
        contador_numeros_negativos += 1
    elif numero > 0:
        acumulador_numeros_positivos += numero
        contador_numeros_positivos += 1

promedio_numeros_positivos = acumulador_numeros_positivos / contador_numeros_positivos

cantidad_total_numeros = contador_numeros_positivos + contador_numeros_negativos

porcentaje_numeros_negativos = contador_numeros_negativos / cantidad_total_numeros * 100

print(f""" 
- Suma de números negativos: {acumulador_numeros_negativos}
- Suma de números positivos: {acumulador_numeros_positivos}
- Números negativos ingresados: {contador_numeros_negativos}
- Números positivos promedio: {promedio_numeros_positivos}
- Porcentaje de números negativos: {round(porcentaje_numeros_negativos, 1)}%
""")