"""
Ejercicio 4
A partir del ingreso de la altura de un basquetbolista determinar si es pivot o no. Para serlo el mismo
deberá medir más de 1.80 metros.
"""

player_height = float(input("Ingrese su altura: "))

if player_height > 1.80:
    print("Usted puede jugar de pivot.")
else:
    print("Usted no puede jugar de pivot.")