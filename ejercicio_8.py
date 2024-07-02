""" Ejercicio 8
Escribe un programa que muestre por consola el resultado de la siguiente
operación (10+3) * (6+6), ¿qué sucede si realizas la misma operación pero sin
los paréntesis? """

print(10+3*6+6)

# Con los parentecis puestos se toma comom prioridar resovler los mismos, por lo que primero hace las respectivas sumas, luego en base a los resultados se sigue con la multiplicación.
# En cambio cuando se quitan los parentesis, se toma como prioridad resolver la multiplicación que es el de mayor jerarquía, 
# por lo que 3*6=18, luego se suman los numeros y da de resultado 34.