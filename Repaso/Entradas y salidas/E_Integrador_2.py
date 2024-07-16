"""
Ejercicio Integrador 2

Empresa de Camiones:
Para el departamento de logística:

A- Es necesario saber la cantidad de camiones que harían falta para transportar los materiales que se utilizarán para la construcción de un edificio.
Para ello, se ingresa la cantidad de toneladas necesarias de materiales a transportar.
El programa deberá informar la cantidad de camiones, sabiendo que cada uno de ellos puede transportar por viaje 3500kg.

B- A partir del ingreso de la cantidad de kilómetros que tiene que recorrer estos camiones para llegar al destino de la obra,
necesitamos que el programa informe cual es el tiempo (en horas) que tardará cada uno de los camiones,
si sabemos que cada camión puede ir a una velocidad máxima y constante de 90 km/h. 
"""

print(""" 
+---------------------+
    -| MOYACORP |-
- Depto. de Logística -
+---------------------+
      
_-¡Camiones con capacidad de 3.5 toneladas!
_-¡Envío inmediato a 90km/h!
 """)

camiones_necesarios = 0
tiempo_transporte = 0

camion_capacidad = 3.5
materiales_cantidad = 0.0

camion_velocidad = 90.0
distancia_a_obra = 0.0

# Ingresar datos.
materiales_cantidad = float(input("Ingrese la cantidad de material en toneladas que necesita transportar: "))
distancia_a_obra = float(input("Ingrese la distancia (en kilómetros) hasta la obra: "))

# Calcular camiones necesarios.
camiones_necesarios = materiales_cantidad//camion_capacidad

if materiales_cantidad % camion_capacidad >= 1:
    camiones_necesarios += 1

# Calcular tiempo de viaje.
tiempo_transporte = distancia_a_obra / camion_velocidad

print(f"\nPara transportar {materiales_cantidad} toneladas de material usted necesita {camiones_necesarios} camiones (3.5 toneladas cada uno).")
print(f"Tiempo estimado para la llegada de los camiones: {tiempo_transporte} horas")