"""
Ejercicio integrador N°2
Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar
la carga y validación de datos para luego mostrarlos por pantalla.
Los datos requeridos son:
Apellido
Edad, entre 18 y 90 años inclusive.
Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.
"""

print(""" 
Bienvenido a nuestro sistema de censos!
A continucación tendrá que ingresar los datos solicitados, siguiendo las indicaciones.
""")

usuario_apellido = input("Ingrese su apellido: ")

usuario_edad = int(input("Ingrese su edad (entre 18 y 90 años inclusive): "))

while usuario_edad < 18 or usuario_edad > 90:
    print("¡Edad inválida!")
    usuario_edad = int(input("Siga las reglas, intente de nuevo: "))

usuario_estado_civil = input("Ingrese su estado civil (“Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”): ")

while usuario_estado_civil.lower() != "soltero" and usuario_estado_civil.lower() != "casado" and usuario_estado_civil.lower() != "divorciado" and usuario_estado_civil.lower() != "viudo":
    print("¡Estado inválido!")
    usuario_estado_civil = input("Siga las reglas, intente de nuevo: ")

usuario_nro_legajo = int(input("Ingrese el número de legajo (4 cifras, sin ceros a la izquierda: "))

while usuario_nro_legajo > 9999:
    print("Número inválido")
    usuario_nro_legajo = int(input("Siga las reglas, intente de nuevo: "))