""" 
Ejercicio 8
Tenemos que obtener los valores (por input) que el usuario nos ingrese (sueldo e incremento), 
transformarlos en números enteros y mostrar el importe de sueldo actualizado con el incremento porcentual utilizando print.
"""

usuario_sueldo = int(input("Ingrese su sueldo actual: "))
porcentaje_deseado = int(input("Ingrese su incremento porcentual deseado: "))

porcentaje = usuario_sueldo * porcentaje_deseado / 100

usuario_sueldo_incrementado = usuario_sueldo + porcentaje

print(f"Su sueldo incrementado en {porcentaje_deseado}% es de: ${usuario_sueldo_incrementado}")