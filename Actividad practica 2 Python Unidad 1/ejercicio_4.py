""" Ejercicio 4
Cree un programa que pida el nombre, número de comisión, asignatura,
docente y si el usuario estuvo presente, luego que muestre los datos por
consola con las leyendas pertinentes. """

print("En este programa usted ingresará los datos solicitados de un alumno, la materia, el docente de la misma y por último dirá si el alumno estuvo presente o no.")
user_name = input("\nIngrese el nombre del alumno: ")
num_com = int(input("Ingrese el número de comisión del alumno " + user_name + ": "))
asignature = input("Ingrese el nombre de la asignatura: ")
teach = input("Ingrese el nombre del docente de la asignatura " + asignature + ": ")
present = input("¿El alumno " + user_name + " estuvo presente o ausente? ")
print("\nResumen:")
print("En la asignatura " + asignature + " brindada por el profesor " + teach + " el alumno " + user_name + " de la división N°" + str(num_com) + " estuvo " + present + ".")