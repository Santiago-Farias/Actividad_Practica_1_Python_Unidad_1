""" Ejercicio 2
Crear un programa que solicite al usuario que ingrese una contraseña
mediante prompt.
Comprobar que la contraseña ingresada sea ‘utn750’. En caso de no
coincidir, volver a solicitarla hasta que coincidan. """

password = input("Ingrese la contraseña: ")

while password != "utn750":
    password = input("Intente de nuevo: ")

print("Acceso concedido.")