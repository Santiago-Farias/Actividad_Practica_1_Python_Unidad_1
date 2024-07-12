""" Ejercicio 3
Crear un programa que solicite al usuario que ingrese un número.
Se deberá validar que se encuentre entre 0 y 9 inclusive. En caso no
coincidir con el rango, volverlo a solicitar hasta que la condición se cumpla. """

num1 = int(input("Ingrese un número entero: "))

while num1 > 9 or num1 < 0:
    num1 = int(input("Inténtelo de nuevo: "))

print("\nValor ingresado:", num1)
print("Usted a ingresado correctamente un valor comprendido entre 0 y 9.\nFelicidades!")