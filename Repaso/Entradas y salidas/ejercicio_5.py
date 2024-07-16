""" 
Ejercicio 5
Se deberá crear un programa que muestre cada operación (suma, resta, multiplicación, y división),
tenemos que obtener los valores (por input) que el usuario nos ingrese (operador_a y operador_b),
transformarlos en números enteros, realizar dicha operación y luego mostrar el resultado de la misma utilizando print. 
Ej: "El resultado de la …… es: 755". 
"""

operador_a = int(input("Ingrese el primer número: "))
operador_b = int(input("Ingrese el segundo número: "))

suma = operador_a + operador_b
resta = operador_a - operador_b
multiplicacion = operador_a * operador_b
division = operador_a / operador_b

print(f"""
El resultado de la suma es: {suma}
El resultado de la resta es: {resta}
El resultado de la multiplicación: {multiplicacion}
El resultado de la división: {division}
 """)