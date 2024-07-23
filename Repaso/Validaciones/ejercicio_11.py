"""
Ejercicio 11
Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.
"""

# Con While, preguntando por el error.
nota = int(input("Ingrese la nota: "))

while nota < 1 or nota > 10:
    nota = int(input("Rango incorrecto, intente de nuevo: "))

print(f"Nota comprendida entre 1 y 10 correcta ({nota})")

# Con Do-While (While_True)
""" while True:
    nota = int(input("Ingrese la nota: "))
    
    if nota > 0 and nota < 11:
        break
    print("\nRango incorrecto.")

print(f"Nota comprendida entre 1 y 10 correcta ({nota})") """