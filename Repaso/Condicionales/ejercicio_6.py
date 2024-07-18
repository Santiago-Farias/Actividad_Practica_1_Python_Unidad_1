"""
Ejercicio 6
Pedirle al usuario su edad, determinar si el usuario NO es adolescente. (entre 13 y 17)
"""

user_age = int(input("Ingrese su edad: "))

if not(user_age > 12 and user_age < 18):
    print("Usted no es adolecente.")



""" if user_age < 13 or user_age > 17:
    print("Usted no es adolecente.") """

""" if user_age > 12 and user_age < 18:
    print("Usted es adolecente.")
else:
    print("Usted no es adolecente.") """
