""" 
Ejercicio integrador 1

Agencia de viaje:
Para saber el costo de un viaje necesitamos el siguiente algoritmo, sabiendo que el precio por kilo de pasajero es 1000 pesos.
Se ingresan todos los datos por PROMPT los datos a solicitar de dos personas son: nombre, edad y peso
Se pide  armar el siguiente mensaje:
"Hola jose y maria , sus pesos son 80 kilos y 60 kilos respectivamente, sumados da 140 kilos , 
el promedio de edad es 33 y su viaje vale 140000 pesos ".
"""

cantidad_personas = 2

nombre_persona_1 = ""
nombre_persona_2 = ""

edad_persona_1 = 0
edad_persona_2 = 0
suma_de_edades = 0
edad_promedio = 0

peso_persona_1 = 0.0
peso_persona_1 = 0.0
peso_total = 0.0

pasaje_persona_1 = 0.0
pasaje_persona_2 = 0.0
valor_viaje = 0.0

cont = 0

# Ingresar datos y calcular pasaje individual.
while cont < cantidad_personas:
    if cont == 0:
        print(f"Persona N°{cont+1}:")
        nombre_persona_1 = input("Ingrese su nombre: ")
        edad_persona_1 = int(input("Ingrese su edad: "))
        peso_persona_1 = float(input("Ingrese su peso: "))
        pasaje_persona_1 = peso_persona_1 * 1000
    if cont == 1:
        print(f"\nPersona N°{cont+1}:")
        nombre_persona_2 = input("Ingrese su nombre: ")
        edad_persona_2 = int(input("Ingrese su edad: "))
        peso_persona_2 = float(input("Ingrese su peso: "))
        pasaje_persona_2 = peso_persona_2 * 1000
    cont += 1

# Calcular peso total.
peso_total = peso_persona_1 + peso_persona_2

# Calcular valor de viaje.
valor_viaje = pasaje_persona_1 + pasaje_persona_2

# Calcular suma y promedio de edades.
suma_de_edades = edad_persona_1 + edad_persona_2
edad_promedio = suma_de_edades / cantidad_personas
""" 
"Hola jose y maria , sus pesos son 80 kilos y 60 kilos respectivamente, sumados da 140 kilos , 
el promedio de edad es 33 y su viaje vale 140000 pesos ". """

print(f"Hola {nombre_persona_1} y {nombre_persona_2}, sus pesos son {peso_persona_1} kilos y {peso_persona_2} kilos respectivamente, "
      f"sumados da {peso_total} kilos, el promedio de edad es de {edad_promedio} años y su viaje vale ${valor_viaje}")