"""
Ejercicio 9
Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Tendrá intentos
indeterminados.
Cuando validamos preguntamos por el error.
"""

clave = "utn2024"

clave_ingresada = input("Ingrese la clave: ")

while clave_ingresada != clave:
    clave_ingresada = input("Intente de nuevo: ")

print("Contraseña correcta.")