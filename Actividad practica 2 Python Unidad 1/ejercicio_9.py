""" Ejercicio 9
Cree un programa que calcule el promedio de un alumno, ingresando su
nombre apellido, 3 notas, que muestre al final las leyendas pertinentes. """

print("Hola!" + "\nEn este programa calcularemos el promedio de 3 notas de el alumno que usted quiera, vamos!")

fname = input("Ingrese el nombre del alumno: ")
lname = input("Ingrese el apellido del alumno: ")
n1 = float(input("Ingrese la primera nota: "))
n2 = float(input("Ingrese la segunda nota: "))
n3 = float(input("Ingrese la tercera nota: "))

average = (n1+n2+n3)/3

print("El alumno " + fname + " " + lname + " tiene un promedio de: ", average)