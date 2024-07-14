""" Enunciado:
De los 3 Jugadores de un Reality Show, se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibió en la etapa de votos
Informar:
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan mediante input() """

print(
"""
+================================+
| ¡Bienvenido al programa de TV!|
| Reality Show |
| Don Pepito |
+================================+
""")
players = 3

player_name_1 = ""
player_name_2 = ""
player_name_3 = ""

player_age_1 = 0
player_age_2 = 0
player_age_3 = 0

player_votes_1 = 0
player_votes_2 = 0
player_votes_3 = 0

most_voted_player = 0
most_voted_player_name = ""
most_voted_player_age = 0

least_voted_player = 99999999
least_voted_player_name = ""
least_voted_player_age = 0

amount_players_age = 0
avg_players_age = 0.0
total_votes = 0

cont = 0

# Ingresar datos de cada jugador.
while cont < players:
    if cont == 0:
        print("Jugador N°" + str(cont+1))
        player_name_1 = input("Ingrese el nombre: ")
        player_age_1 = int(input("Ingrese la edad: "))
        while player_age_1 < 25:
            player_age_1 = int(input("Tienes que ser mayor de 25 años.\nIntente de nuevo: "))
        player_votes_1 = int(input("Ingrese la cantidad de votos: "))
        while player_votes_1 <= 0:
            player_votes_1 = int(input("Cantidad de votos válidos de 1 en adelante.\nIntente de nuevo: "))
    if cont == 1:
        print("\nJugador N°" + str(cont+1))
        player_name_2 = input("Ingrese el nombre: ")
        player_age_2 = int(input("Ingrese la edad: "))
        while player_age_2 < 25:
            player_age_2 = int(input("Tienes que ser mayor de 25 años.\nIntente de nuevo: "))
        player_votes_2 = int(input("Ingrese la cantidad de votos: "))
        while player_votes_2 <= 0:
            player_votes_2 = int(input("Cantidad de votos válidos de 1 en adelante.\nIntente de nuevo: "))
    if cont == 2:
        print("\nJugador N°" + str(cont+1))
        player_name_3 = input("Ingrese el nombre: ")
        player_age_3 = int(input("Ingrese la edad: "))
        while player_age_3 < 25:
            player_age_3 = int(input("Tienes que ser mayor de 25 años.\nIntente de nuevo: "))
        player_votes_3 = int(input("Ingrese la cantidad de votos: "))
        while player_votes_3 <= 0:
            player_votes_3 = int(input("Cantidad de votos válidos de 1 en adelante.\nIntente de nuevo: "))
    cont += 1

cont = 0 # Reinicio del contador

# Calcular jugador mas y menos votado.
while cont < players:
    if cont == 0:
        if player_votes_1 > most_voted_player:
            most_voted_player = player_votes_1
            most_voted_player_name = player_name_1
            most_voted_player_age = player_age_1
        if player_votes_1 < least_voted_player:
            least_voted_player = player_votes_1
            least_voted_player_age = player_age_1
            least_voted_player_name = player_name_1
    if cont == 1:
        if player_votes_2 > most_voted_player:
            most_voted_player = player_votes_2
            most_voted_player_name = player_name_2
            most_voted_player_age = player_age_2
        if player_votes_2 < least_voted_player:
            least_voted_player = player_votes_2
            least_voted_player_age = player_age_2
            least_voted_player_name = player_name_2
    if cont == 2:
        if player_votes_3 > most_voted_player:
            most_voted_player = player_votes_3
            most_voted_player_name = player_name_3
            most_voted_player_age = player_age_3
        if player_votes_3 < least_voted_player:
            least_voted_player = player_votes_3
            least_voted_player_age = player_age_3
            least_voted_player_name = player_name_3
    cont += 1

# Calcular promedio de edad de los jugadores.
amount_players_age = player_age_1 + player_age_2 + player_age_3
avg_players_age = amount_players_age / players

#Calcular votos totales.
total_votes = player_votes_1 + player_votes_2 + player_votes_3

print(
"""
+================================+
| ¡FELICIDADES!|"""
"\n| " + most_voted_player_name + ", " + str(most_voted_player_age) + " años '" + str(most_voted_player) + " votos' |"
"""
| Ganador del |
| Reality Show |
| Don Pepito |
+================================+

+================================+
| Jugador menos votado |"""
"\n| " + least_voted_player_name + ", " + str(least_voted_player_age) + " años '" + str(least_voted_player) + " votos' |"
"""
| Promedio de edad de los jugadores |"""
"\n| " + str(avg_players_age) + " años |"
"""
| Participación |"""
"\n| " + str(total_votes) + " votos totales |"
"""
+================================+
""")