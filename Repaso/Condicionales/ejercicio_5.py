"""
Ejercicio 5
Pedirle al usuario su edad, determinar si el usuario es adolescente. (entre 13 y 17)
"""

user_age = int(input("Ingrese su edad: "))

""" if user_age > 12 and user_age < 18:
    print("Usted es adolecente.") """

if user_age > 12:
    if user_age < 18:
        print("Usted es adolecente.")