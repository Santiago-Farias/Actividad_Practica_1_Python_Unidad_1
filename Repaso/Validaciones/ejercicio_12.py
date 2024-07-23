"""
Ejercicio 12
Solicitarle al usuario el ingreso de un color primario. Validar que el mismo sea Rojo, Verde o Azul.
"""

color_ingreso = input("Ingrese el nombre de un color primario (Rojo, Verde o Azul): ")

while color_ingreso.lower() != "rojo" and  color_ingreso.lower() != "verde" and color_ingreso.lower() != "azul":
    color_ingreso = input("Opción incorrecta, intente de nuevo: ")

print(f"Opción correcta, color elegido {color_ingreso}")


""" while True:
    color_ingreso = input("Ingrese el nombre de un color primario: ")

    if color_ingreso.lower() == "rojo" or color_ingreso.lower() == "verde" or color_ingreso.lower() == "azul":
        print(f"Opción correcta, color elegido {color_ingreso}")
        break """