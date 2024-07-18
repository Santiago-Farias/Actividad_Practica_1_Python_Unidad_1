"""
Ejercicio 8
A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá
determinar la posición del jugador en la cancha, considerando los siguientes parámetros:

- Menos de 160 cm: Base
- Entre 160 cm y 179 cm: Escolta
- Entre 180 cm y 199 cm: Alero
- 200 cm o más: Ala-Pívot o Pívot
"""

posicion_jugador = ""

altura_jugador = float(input("Ingrese su altura en centímetros: "))

if altura_jugador < 160.0:
    posicion_jugador = "Base"
elif altura_jugador > 159.0 and altura_jugador < 180.0:
    posicion_jugador = "Escolta"
elif altura_jugador > 179.0 and altura_jugador < 200.0:
    posicion_jugador = "Alero"
else:
    posicion_jugador = "Ala-Pívot"

print(f"Usted puede jugar de {posicion_jugador}. Rompéla toda amigo, ánimo!")