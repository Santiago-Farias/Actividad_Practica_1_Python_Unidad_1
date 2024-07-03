""" Ejercicio 8
Cree un programa que permite ingresar el nombre de un producto, el
precio y que calcule el IVA. Tomando el IVA de 21%"""

print("Hola!" + "\nEn este programa calcularemos el IVA de un producto, que emoción!!!!")

product_name = input("Ingrese el nombre del producto: ")
price = float(input("Ingrese el precio del producto $"))
price_without_iva = price/1.21
iva_of_product = price - price_without_iva

print("\nEl IVA del producto " + product_name + " es de: $", iva_of_product, "\nCon un precio sin IVA de $", price_without_iva)
print("El precio del " + product_name + " mas el IVA es: $" + str(price_without_iva + iva_of_product))