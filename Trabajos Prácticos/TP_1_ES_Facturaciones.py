""" 
Enunciado:
Para el departamento de facturación:
A. Ingresar tres precios de productos y mostrar la suma de los mismos.
B. Ingresar tres precios de productos y mostrar el promedio de los mismos.
C. ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%).

Una vez finalizado el TP, Comparte el código en los foros 👇 
"""
prod1 = float(input("Ingrese el precio del producto N°1: $"))
prod2 = float(input("Ingrese el precio del producto N°2: $"))
prod3 = float(input("Ingrese el precio del producto N°3: $"))

prods_value = prod1 + prod2 + prod3
prods_value_average = prods_value / 3
prods_value_iva = prods_value * 1.21


print("\n+++++++RESUMEN+++++++")
print("\nValor total: $" + str(prods_value))
print("Promedio de precio: " + str(prods_value_average))
print("Valor total mas IVA del 21%: " + str(prods_value_iva))