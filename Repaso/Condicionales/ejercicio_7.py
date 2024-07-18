"""
Ejercicio 7
Pedirle al usuario su edad, determinar si es mayor (18 años o más), niño/a (menor de 10), pre-
adolescente (edad entre 10 y 12 años inclusive) o adolescente (edad entre 13 y 17 años).
Condiciones excluyentes ya que si no se cumple una si o si se tiene que cumplir una de las otras.
"""

user_age = int(input("Ingrese su edad: "))

if user_age > 17:
    print("Usted es mayor de edad.")
elif user_age > 9 and user_age < 13:
    print("Usted es pre-adolecente.")
elif user_age > 12 and user_age < 18:
    print("Usted es adolecente.")
else:
    print("Usted es un niño.")