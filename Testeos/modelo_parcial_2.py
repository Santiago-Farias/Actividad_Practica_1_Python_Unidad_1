"""
Modelo de parcial N°2
Una empresa internacional está realizando un estudio de mercado para decidir cuál
será la nueva plataforma de entretenimiento que se lanzará en el mercado argentino y en la cual invertirán.
Las posibles franquicias son las siguientes: Hulu, Vix+ o CODA.

Para ello, se realizará una encuesta mediante un sistema de voto electrónico, 
con el propósito de conocer cuáles son los gustos de los encuestados (no se sabe cuántos):
Se ingresa de cada encuestado:

Nombre
Edad (no menor a 18)
Tiene suscripción a algún servicio de streaming (sí-no)
Género (Masculino - Femenino - No binario - Otro)
Voto (Hulu, Vix+, CODA)
Se solicita realizar las siguientes búsquedas:

1. Cantidad de encuestados de género Masculino, cuya edad esté entre 18 y 25 o entre 36 y 49 que votaron por Hulu.
2. Nombre, género y edad del encuestado de menor edad que votó por Hulu.
3. Hallar el porcentaje de encuestados mayores de 25 años que tienen suscripción CODA.
4. Determinar el promedio de edad de los encuestados que votaron por Vix+.
5. Contar cuántos encuestados votaron por cada franquicia y determinar cuál tuvo más votos.
"""

usuario_contador = 0

usuario_edad = 0
usuario_tiene_suscripcion = False
usuario_genero = ""
usuario_voto = ""

contador_usuario_masculino_segun_edad_voto_hulu = 0

opcion = "si"

print("¡Bienvenido a nuestra encuesta! Proporcione los datos solicitados a continuación, muchas gracias.")

while True:
    # Solicitar edad del usuario.
    usuario_edad = int(input("Ingrese su edad (no menor a 18 años): "))
    while usuario_edad < 18:
        usuario_edad = int(input("No puede ser menor de 18 años, intente nuevamente: "))

    # Consultar si el usuario cuenta con suscripción.
    usuario_tiene_suscripcion = input("¿Usted cuenta con alguna suscripción a algún servicio de streaming? Responder con 'si' o 'no': ")
    while usuario_tiene_suscripcion.lower() != "si" and usuario_tiene_suscripcion.lower() != "no":
        usuario_tiene_suscripcion = input("Respuesta inválida, responda con 'si' o 'no' por favor: ")

    if usuario_tiene_suscripcion.lower() == "si":
        usuario_tiene_suscripcion = True
    else:
        usuario_tiene_suscripcion = False

    # Solicitar el género del usuario.
    usuario_genero = input("Ingrese su genero (Masculino - Femenino - No binario - Otro): ")
    while usuario_genero.lower() != "masculino" and usuario_genero.lower() != "femenino" and usuario_genero.lower() != "no binario" and usuario_genero.lower() != "otro":
        usuario_genero = input("Respuesta inválda, ingrese una dentro de las opciones (Masculino - Femenino - No binario - Otro): ")

    # Soliciar el voto del usuario.
    usuario_voto = input("¿Cuál de las siguientes tres plataformas de streaming eligiría?\n(Hulu, Vix+, CODA): ")
    while usuario_voto.lower() != "hulu" and usuario_voto.lower() != "vix+" and usuario_voto.lower() != "coda":
        usuario_voto = input("Opción inválida, eliga una de las siguientres tres plataformas de streaming (Hulu, Vix+, CODA): ")

    # Calcular la cantidad de encuestados de género Masculino, cuya edad esté entre 18 y 25 o entre 36 y 49 que votaron por Hulu.
    if usuario_genero.lower() == "masculino":
        if (usuario_edad > 17 and usuario_edad < 26) or (usuario_edad > 35 and usuario_edad < 50):
            if usuario_voto.lower() == "hulu":
                contador_usuario_masculino_segun_edad_voto_hulu += 1

    opcion = input("¿Desea continuar?\n(si/no): ")

    if opcion.lower() == "no":
        break

# Verificación preliminar
print(f"Tiene sub stream? {usuario_tiene_suscripcion}")
print(f"Edad: {usuario_edad}")
print(f"genero: {usuario_genero}")
print(f"voto: {usuario_voto}")
print(f"La cantidad de encuestados de género Masculino, cuya edad esté entre 18 y 25 o entre 36 y 49 que votaron por Hulu: {contador_usuario_masculino_segun_edad_voto_hulu}")

print("""
¡Gracias por participar en nuestra encuesta!
""")