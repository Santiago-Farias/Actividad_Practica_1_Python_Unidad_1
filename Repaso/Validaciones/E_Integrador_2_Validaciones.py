# Entregado.
"""
Ejercicio integradoar N°2 Validaciones
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

jugadores = 0

jugador_nombre = ""
jugador_edad = 0
jugadores_edad_suma = 0
jugadores_edad_promedio = 0
jugador_ganadas = 0

jugador_mas_ganador_nombre = ""
jugador_mas_ganador_partidas = 0

jugador_menos_ganador_nombre = ""
jugador_menos_ganador_partidas = 0
jugador_menos_ganador_edad = 0

total_partidas_ganadas = 0

bandera = True

opcion = ""

print(""" 
| Torneo de Ajedrez 'Marcelo Conocelo' |
--- A continuación registe los datos de los jugadores.
""")

# Solicitar ingreso de datos hasta que el usuario desée.
while True:
    jugador_nombre = input("Ingrese el nombre del jugador actual: ")

    jugador_edad = int(input("Ingrese la edad del jugador actual (mayor de 10 años): "))
    while jugador_edad < 11:
        jugador_edad = int(input("Tiene que ser mayor a 10 años, intente de nuevo: "))

    jugador_ganadas = int(input("Ingrese las partidas ganadas por el jugadaor actual (no menor a 0): "))
    while jugador_ganadas < 0:
        jugador_ganadas = int(input(f"Número inválido ({jugador_ganadas}) es menor a 0, intente de nuevo: "))
    
    # Sumar edades de jugadores.
    jugadores_edad_suma += + jugador_edad

    # Calcular datos del jugador mas ganador.
    if jugador_ganadas > jugador_mas_ganador_partidas or bandera == True:
        jugador_mas_ganador_partidas = jugador_ganadas
        jugador_mas_ganador_nombre = jugador_nombre

    # Calcular datos del jugador menos ganador.
    if jugador_ganadas < jugador_menos_ganador_partidas or bandera == True:
        jugador_menos_ganador_partidas = jugador_ganadas
        jugador_menos_ganador_nombre = jugador_nombre
        jugador_menos_ganador_edad = jugador_edad
        bandera = False

    # Acumular suma de partidas ganadas.
    total_partidas_ganadas += jugador_ganadas

    # Solicitar al usuario si desea seguir ingresando datos.
    opcion = input("Desea seguir (si/no)")
    if opcion.lower() == "no":
        break

# Calcular promedio de edades.
jugadores_edad_promedio = jugadores_edad_suma / jugadores

# Mostrar estadísticas por pantalla.
print(f""" 
| Y LOS RESULTADOS SON... |

Jugador mas ganador: {jugador_mas_ganador_nombre}
Nombre y edad del jugador menos ganador, respectivamente: {jugador_menos_ganador_nombre}, {jugador_menos_ganador_edad}
Edad promedio: {jugadores_edad_promedio:.2f}
Partidas ganadas en total: {total_partidas_ganadas}
""")