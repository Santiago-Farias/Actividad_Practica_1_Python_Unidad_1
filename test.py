"""
De los jugadores participantes en un torneo de ajedrez, se registra:
- Nombre
- La edad (mayor de 10 años)
- La cantidad de partidas ganadas (no menor a cero) que obtuvieron en el torneo.

Informar:
a. Nombre del jugador con más partidas ganadas.
b. Nombre y edad del jugador con menos partidas ganadas.
c. El promedio de edades de los jugadores.
d. El total de partidas ganadas.
"""

jugadores_cantidad = 3

jugador_mas_ganador_partidas = 0
jugador_mas_ganador_nombre = ""
jugador_mas_ganador_edad = 0

jugador_menos_ganador_partidas = 999999999
jugador_menos_ganador_nombre = ""
jugador_menos_ganador_edad = 0

jugadores_suma_edades = 0
jugadores_promedio_edad = 0.0

total_victorias = 0

# Ingreso de datos.
print("Jugador N°1")
jugador_1_nombre = input("Ingrese el nombre: ")
jugador_1_edad = int(input("Ingrese la edad: "))
while jugador_1_edad < 11:
    print("Debes de ser mayor de 10 años.")
    jugador_1_edad = int(input("Ingrese la edad: "))
jugador_1_partidas_ganadas = int(input("Ingrese la cantidad de partidas ganadas: "))
while jugador_1_partidas_ganadas < 0:
    print("La cantida de partidas ganadas no puede ser menor a 0.")
    jugador_1_partidas_ganadas = int(input("Ingrese la cantidad de partidas ganadas: "))

print("\nJugador N°2")
jugador_2_nombre = input("Ingrese el nombre: ")
jugador_2_edad = int(input("Ingrese la edad: "))
while jugador_2_edad < 11:
    print("Debes de ser mayor de 10 años.")
    jugador_2_edad = int(input("Ingrese la edad: "))
jugador_2_partidas_ganadas = int(input("Ingrese la cantidad de partidas ganadas: "))
while jugador_2_partidas_ganadas < 0:
    print("La cantida de partidas ganadas no puede ser menor a 0.")
    jugador_2_partidas_ganadas = int(input("Ingrese la cantidad de partidas ganadas: "))

print("\nJugador N°3")
jugador_3_nombre = input("Ingrese el nombre: ")
jugador_3_edad = int(input("Ingrese la edad: "))
while jugador_3_edad < 11:
    print("Debes de ser mayor de 10 años.")
    jugador_3_edad = int(input("Ingrese la edad: "))
jugador_3_partidas_ganadas = int(input("Ingrese la cantidad de partidas ganadas: "))
while jugador_3_partidas_ganadas < 0:
    print("La cantida de partidas ganadas no puede ser menor a 0.")
    jugador_3_partidas_ganadas = int(input("Ingrese la cantidad de partidas ganadas: "))

# Calcular promedio de edad de jugadores.
jugadores_suma_edades = jugador_1_edad + jugador_2_edad + jugador_3_edad
jugadores_promedio_edad = round(jugadores_suma_edades / jugadores_cantidad, 2)

# Calcular partidas ganadas en total.
total_victorias = jugador_1_partidas_ganadas + jugador_2_partidas_ganadas + jugador_3_partidas_ganadas

# Calcular jugador más ganador.
if jugador_1_partidas_ganadas > jugador_mas_ganador_partidas:
    jugador_mas_ganador_partidas = jugador_1_partidas_ganadas
    jugador_mas_ganador_nombre = jugador_1_nombre
    jugador_mas_ganador_edad = jugador_1_edad

if jugador_2_partidas_ganadas > jugador_mas_ganador_partidas:
    jugador_mas_ganador_partidas = jugador_2_partidas_ganadas
    jugador_mas_ganador_nombre = jugador_2_nombre
    jugador_mas_ganador_edad = jugador_2_edad

if jugador_3_partidas_ganadas > jugador_mas_ganador_partidas:
    jugador_mas_ganador_partidas = jugador_3_partidas_ganadas
    jugador_mas_ganador_nombre = jugador_3_nombre
    jugador_mas_ganador_edad = jugador_3_edad

# Calcular jugador menos ganador.
if jugador_1_partidas_ganadas < jugador_menos_ganador_partidas:
    jugador_menos_ganador_partidas = jugador_1_partidas_ganadas
    jugador_menos_ganador_nombre = jugador_1_nombre
    jugador_menos_ganador_edad = jugador_1_edad

if jugador_2_partidas_ganadas < jugador_menos_ganador_partidas:
    jugador_menos_ganador_partidas = jugador_2_partidas_ganadas
    jugador_menos_ganador_nombre = jugador_2_nombre
    jugador_menos_ganador_edad = jugador_2_edad

if jugador_3_partidas_ganadas < jugador_menos_ganador_partidas:
    jugador_menos_ganador_partidas = jugador_3_partidas_ganadas
    jugador_menos_ganador_nombre = jugador_3_nombre
    jugador_menos_ganador_edad = jugador_3_edad

print(f""" 
| Jugador mas ganador |
{jugador_mas_ganador_nombre}, {jugador_mas_ganador_edad} años ({jugador_mas_ganador} partidas ganadas)

| Jugador menos ganador |
{jugador_menos_ganador_nombre}, {jugador_menos_ganador_edad} años ({jugador_menos_ganador} partidas ganadas)

| Promedio de edad |
    {jugadores_promedio_edad} años
| Victorias totales |
        {total_victorias}
""")