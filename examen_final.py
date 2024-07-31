"""
Santiago Farias Div. 106
UTN Inversiones, realiza un estudio de mercado para saber cuál será la nueva franquicia que se insertará en el mercado argentino y en la cual invertirán. 
Las posibles franquicias son las siguientes: Apple, Dunkin o Ikea. 
Para ello, se realizará una encuesta mediante un sistema de voto electrónico,
con el propósito de conocer cuáles son los gustos de los encuestados (no se sabe cuántos): Se ingresa de cada encuestado: 
- nombre 
- edad (no menor a 18) 
- está empleado (si-no) 
- género (Masculino - Femenino - Otro) 
- voto (APPLE, DUNKIN, IKEA) 
Se necesita saber: 
1. Cantidad de encuestados desempleados que votaron por DUNKIN o IKEA, cuya edad esté entre 25 y 50 años inclusive. 
2. Nombre y voto del encuestado de género Masculino con menor edad.
3. Porcentaje de votos de cada género. 
4. Promedio de edad de los encuestados de género Femenino que votaron IKEA.
5. Determinar cuál fue el género que tuvo más encuestados.
"""

usuario_nombre = ""
usuario_edad = 0
usuario_estado_empleado = ""
usuario_genero = ""
usuario_voto = ""

contador_usuario_empleado_dunkin_ikea_segun_edad = 0

usuario_joven_masculino_edad = 0
usuario_joven_masculino_nombre = ""
usuario_joven_masculino_voto = ""

contador_genero_masculino = 0
porcentaje_genero_masculino = 0
contador_genero_femenino = 0
porcentaje_genero_femenino = 0
contador_genero_otro = 0
porcentaje_genero_otro = 0
total_generos = 0

contador_genero_femenino_ikea = 0
suma_edades_femenino_ikea = 0
promedio_edad_femenino_ikea = 0.0

genero_con_mas_votos = ""

bandera_usuario_joven_masculino_edad = True

opcion = "si"

while True:

    usuario_nombre = input("Ingrese su nombre: ")

    usuario_edad = int(input("Ingrese su edad (no menor a 18 años): "))
    while usuario_edad < 18:
        usuario_edad = int(input(f"¡Edad inválida! ({usuario_edad}) es menor a 18, intente de nuevo: "))

    usuario_estado_empleado = input("¿Usted se encuentra empleado? Respondo con si o con no: ")
    while usuario_estado_empleado.lower() != "si" and usuario_estado_empleado.lower() != "no":
        usuario_estado_empleado = input("¡Opción inválida! Responda la pregunta con si o con no.\n¿Usted se encuentra empleado?: ")

    usuario_genero = input("Para seleccionar su género, elija una de las siguientes opciones (Masculino - Femenino - Otro): ")
    while usuario_genero.lower() != "masculino" and usuario_genero.lower() != "femenino" and  usuario_genero.lower() != "otro":
        usuario_genero = input("!Opción inválida¡ Ingrese una de las siguientes (Masculino - Femenino - Otro): ")

    usuario_voto = input("Ingrese su voto elijiendo una de las siguientes opciones (APPLE, DUNKIN, IKEA): ")
    while usuario_voto.lower() != "apple" and usuario_voto.lower() != "dunkin" and usuario_voto.lower() != "ikea":
        usuario_voto = input("!Opción inválida¡ Ingrese una de las siguientes (APPLE, DUNKIN, IKEA): ")

    # Calcular la cantidad de encuestados desempleados que votaron por DUNKIN o IKEA, cuya edad esté entre 25 y 50 años inclusive. 
    if usuario_estado_empleado == "no":
        if usuario_voto.lower() == "dunkin" or usuario_voto.lower() == "ikea":
            if usuario_edad > 24 and usuario_edad < 51:
                contador_usuario_empleado_dunkin_ikea_segun_edad += 1

    # Calcular el encuesado Masculino de menor edad y guardar nombre y voto.
    if usuario_genero.lower() == "masculino":
        contador_genero_masculino += 1
        if usuario_edad < usuario_joven_masculino_edad or bandera_usuario_joven_masculino_edad == True:
            usuario_joven_masculino_edad = usuario_edad
            usuario_joven_masculino_nombre = usuario_nombre
            usuario_joven_masculino_voto = usuario_voto
            bandera_usuario_joven_masculino_edad = False
    elif usuario_genero.lower() == "femenino":
        contador_genero_femenino += 1
        if usuario_voto.lower() == "ikea":
            contador_genero_femenino_ikea += 1
            suma_edades_femenino_ikea += usuario_edad
    else:
        contador_genero_otro += 1

    opcion = input("¿Desea seguir? (si/no): ")
    
    if opcion != "si":
        break

# Calcular el total de generos y el porcentaje de cada uno.
total_generos = contador_genero_masculino + contador_genero_femenino + contador_genero_otro

porcentaje_genero_masculino = (contador_genero_masculino / total_generos) * 100
porcentaje_genero_femenino = (contador_genero_femenino / total_generos) * 100
porcentaje_genero_otro = (contador_genero_otro / total_generos) * 100

# Calcular el promedio de edad de los encuestados de género Femenino que votaron IKEA.
if suma_edades_femenino_ikea > 0 and contador_genero_femenino_ikea > 0:
    promedio_edad_femenino_ikea = suma_edades_femenino_ikea / contador_genero_femenino_ikea
else:
    promedio_edad_femenino_ikea = 0

# Calcular el género que tuvo más encuestados.
if contador_genero_masculino > contador_genero_femenino:
    genero_con_mas_votos = "Masculino"
elif contador_genero_femenino > contador_genero_otro:
    genero_con_mas_votos = "Femenino"
else:
    genero_con_mas_votos = "Otro"


# Resultados.
print(f"""
| RESULTADOS |
Cantidad de encuestados desempleados que votaron por DUNKIN o IKEA, cuya edad esté entre 25 y 50 años inclusive: {contador_usuario_empleado_dunkin_ikea_segun_edad}
Nombre y voto del encuestado de género Masculino con menor edad: {usuario_joven_masculino_nombre} de {usuario_joven_masculino_edad} años votó por {usuario_joven_masculino_voto}
Votos totales: {total_generos}
- {round(porcentaje_genero_masculino, 2)}% de Masculinos ({contador_genero_masculino} votos)
- {round(porcentaje_genero_femenino, 2)}% de Femeninos ({contador_genero_femenino} votos)
- {round(porcentaje_genero_otro, 2)}% de Otros generos ({contador_genero_otro} votos)
Promedio de edad de los encuestados de género Femenino que votaron IKEA: {round(promedio_edad_femenino_ikea, 2)}
Género con mas encuestados: {genero_con_mas_votos}
""")