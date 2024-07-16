""" 
Ejercicio 10
Tenemos que crear un programa que deberán obtener el importe y el descuento que ingrese el usuario por consola,
transformarlos en números y mostrar el importe actualizado con el descuento utilizando print.
"""

importe = float(input("Ingrese su importe: "))
porcentaje = int(input("Ingrese el descuento porcentual: "))

descuento = importe * porcentaje / 100

importe_con_descuento = importe - descuento

print(f"Su importe reducido en un {porcentaje}% es de: {importe_con_descuento}")