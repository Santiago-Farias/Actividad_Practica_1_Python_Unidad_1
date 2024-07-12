""" Ejercicio 4
Crear un programa que solicite al usuario que ingrese una letra. Se deberá
validar que la letra sea ‘U’, ‘T’ o ‘N’ (en mayusculas).
En caso no coincidir con ninguna de las letras, volver a solicitarla hasta que
la condición se cumpla. """

""" Extra personal:
Cuando el usuario ingrese una de las letras válidas, se mostrará en pantalla los espacios faltantes y la letra acertada.
Cuando complete toda la palabra el programa termina."""

letter = input("Ingrese una letra: ")
l1 = "_" # Variable letra 1.
l2 = "_" # Variable letra 2.
l3 = "_" # Variable letra 3.
word = "" # Variable que guardará las letras válidas.

while word != "UTN":
    letter = input("Ingrese una nueva letra: ")

    if letter == "U":
        l1 = letter
        word = l1 + l2 + l3
        print(word)

    if letter == "T":
        l2 = letter
        word = l1 + l2 + l3
        print(word)

    if letter == "N":
        l3 = letter
        word = l1 + l2 + l3
        print(word)