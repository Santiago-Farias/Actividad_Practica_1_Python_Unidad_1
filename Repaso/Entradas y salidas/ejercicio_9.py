""" 
Ejercicio 9
Tenemos que crear un programa que deberá obtener el importe que ingrese el usuario por consola(input),
transformar en número y mostrar el importe actualizado con un descuento del 20% utilizando print.
"""

importe = float(input("Ingrese su importe: "))

descuento = 20

porcentaje = importe * descuento / 100

importe_final = importe - porcentaje

print(f"Su importe con un descuento del {descuento}% es de: {importe_final}")