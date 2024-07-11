""" Ejercicio
Crear un programa que se ingrese la edad del usuario en número y pueda
calcular si es adolescente (edad entre 13 y 17 años). """

user_age = int(input("Ingrese su edad: "))

if user_age > 13 and user_age < 17:
    print("Usted es un adolecente.")
else:
    print("Usted no es un adolecente, salga de aquí por favor.")