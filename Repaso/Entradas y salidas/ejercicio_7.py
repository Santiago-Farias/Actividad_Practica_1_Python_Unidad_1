""" 
Ejercicio 7
Tenemos que obtener el sueldo (por input) que el usuario nos ingrese , 
transformarlo en número entero y mostrar el importe de sueldo actualizado con el incremento del 15% utilizando print.
"""

usuario_sueldo = int(input("Ingrese su sueldo: "))

porcentaje = usuario_sueldo * 0.15

usuario_sueldo_actualizado = usuario_sueldo + porcentaje

print(f"Su sueldo incrementado en 15% es de ${usuario_sueldo_actualizado}")