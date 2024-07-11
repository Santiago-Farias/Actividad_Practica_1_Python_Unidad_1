""" Ejercicio 3
Crear un programa que a partir del ingreso de la altura de un
basquetbolista determinar si es pivot o no. Para serlo el mismo deberá
medir más de 1.80 metros. """

print("Bienvenido basquetbolista!")
height = float(input("En el siguiente programa determinaremos si usted puede jugar de pivot o no \n\nIngrese su altura: "))

if height > 1.80:
    print("Usted es un pivot")
else:
    print("Usted no es pivot, vaya a su casa.")