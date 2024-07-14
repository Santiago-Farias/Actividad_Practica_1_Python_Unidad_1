nota = int(input("Ingrese la nota: "))

while nota < 0 or nota > 10:
    nota = int(input("Ingrese nuevamente la nota: "))

print("Nota ingresada exitosamente, fue un:", nota)