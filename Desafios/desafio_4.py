""" Desafio 4 - Adivina el número secreto
1- Pedirá al usuario que ingrese un número entero.
2- Utilizará un bucle while.
3- Comprobará si el número ingresado por el usuario es el mismo que el número escogido por el mago. 
Si el número elegido por el usuario es diferente al número secreto del mago, 
el usuario debería ver el mensaje "¡Ja, ja! ¡Estás atrapado en mi bucle!" 
y se le solicitará que ingrese un número nuevamente. 
Si el número ingresado por el usuario coincide con el número escogido por el mago, 
el número debe imprimirse en la pantalla, y el mago debe decir las siguientes palabras: 
"¡Bien hecho, Junior! Eres libre ahora."
 """

secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, Junior!|
| Introduce un número entero |
| y adivina qué número he |
| elegido para ti. |
|¿Cuál es el número secreto? |
+================================+
""")

num = int(input("Ingrese un número entero: "))

if num != secret_number:
    print("¡Ja, ja, ja, ja, ja, ja, ja, ja, ja, ja, ja, ja! \n¡Estás atrapado en mi bucle!")


while num != secret_number:
    num = int(input("Ingrese un nuevo núemro entero: "))

print(""" 

+===== EL NÚMERO SECRETO ES: =====+
+=====          777          =====+

¡Bien hecho, Junior! Eres libre ahora.     
 """)