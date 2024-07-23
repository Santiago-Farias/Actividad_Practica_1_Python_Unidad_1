clave_correcta = "clave123"  # Clave correcta que debe ingresar el usuario
intentos = 3  # Número de intentos permitidos

while intentos > 0:
    clave_ingresada = input("Ingrese la clave: ")
    
    if clave_ingresada == clave_correcta:
        print("¡Clave correcta! Acceso concedido.")
        break  # Sale del bucle si la clave es correcta
    else:
        intentos -= 1
        print(f"Clave incorrecta. Intentos restantes: {intentos}")

if intentos == 0:
    print("¡Número de intentos agotados! Acceso denegado.")
