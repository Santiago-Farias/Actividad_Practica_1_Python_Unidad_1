""" Ejercicio 5
Crear un programa que al ingresar un número puede calcular si es mayor,
niño/a(menor de 10) o pre-adolescente (edad entre 10 y 13 años)
adolescente (edad entre 13 y 17 años) de edad. """

user_age = int(input("Ingrese su edad: "))

if user_age > 18:
    print("Usted es mayor de edad.")
elif user_age > 13 and user_age < 17:
    print("Usted es adolecente")
elif user_age > 10 and user_age < 13:
    print("Usted es pre-adolecente")
elif user_age < 10:
    print("Usted es un niño.")
else:
    print("Usted es un androide")