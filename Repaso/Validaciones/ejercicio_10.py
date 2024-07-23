"""
Ejercicio 10
Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos.
"""

clave = "utn2024"
intentos = 3

clave_ingresada = input("Ingrese la clave: ")

while intentos > 0:
    if clave_ingresada != clave:
        print(f"Clave incorrecta ({intentos} intentos restantes)")
        clave_ingresada = input(f"Intente de nuevo: ")
    else:
        print("Clave correcta!")
        break
    intentos -= 1

if intentos == 0:
    print("Haz llegado al límite, no hay mas intentos papá.")