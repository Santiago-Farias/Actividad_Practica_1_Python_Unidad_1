bandera = True
num = input("ingrese num: ")
digitos = len(num)
while bandera != False:
    if digitos != 4:
        num = input("Tiene que tener 4 cifras, intente de nuevo: ")
        digitos = len(num)
    else:
        bandera = False
    
    if num[0] == '0':
        bandera = True
        if num[1] == '0':
            bandera = True
            if num[2] == '0':
                bandera = True

    if bandera == True:
        num = input("Sin ceros a la izquierda, intente de nuevo: ")
        digitos = len(num)

# Ejemplo gpt
"""
bandera = True

while bandera:
    num = input("Ingrese número de legajo (debe ser un valor numérico de 4 cifras sin ceros a la izquierda): ")

    # Verificar si el número tiene 4 cifras
    if len(num) != 4 or not num.isdigit():
        print("Debe tener 4 cifras numéricas.")
        continue  # Vuelve al inicio del bucle while

    # Verificar si no tiene ceros a la izquierda
    if num[0] == '0':
        print("No debe tener ceros a la izquierda.")
        continue  # Vuelve al inicio del bucle while

    # Si pasó todas las validaciones
    bandera = False

# Mostrar el número de legajo válido
print("Número de legajo ingresado:", num)
"""