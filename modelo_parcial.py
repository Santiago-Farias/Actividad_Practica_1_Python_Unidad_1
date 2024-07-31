# Entregado y auto corregido.

"""
Modelo de parcial:

Una concesionaria nos pide un programa que nos permita cargar los datos de sus ventas:
las ventas son indeterminadas.

nombre del cliente:
edad(debe ser mayor)
marca del vehiculo (renault,fiat,bmw)
cantidad de puertas (2,4)
apellido del vendedor (Zapata,Quiroz,Simino)

se necesita saber:

A-Cantidad de vehiculos de 2 puertas que sean de la marca renault
B-nombre del cliente mas joven
C-porcentaje cada marca de auto sobre el total
D-promedio de edades de los clientes que compraron 4 puertas
E-nombre del cliente mas viejo que compro fiat
F-total de autos vendidos de la marca BMW
G-Apellido del vendedor que menos vendio

NOTA: RECUERDEN QUE PARA RENDIR EL EXAMEN DEBEN TENER 100% DE ASISTENCIAS
"""

vehiculos_renault_vendidos_contador = 0
vehiculos_renault_vendidos_porcentaje = 0

vehiculos_fiat_vendidos_contador = 0
vehiculos_fiat_vendidos_porcentaje = 0

vehiculos_bmw_vendidos_contador = 0
vehiculos_bmw_vendidos_porcentaje = 0

vehiculos_vendidos_total = 0

vehiculos_dos_puertas_renault = 0

cliente_mas_joven_edad = 0
cliente_mas_joven_nombre = ""

cliente_mas_viejo_fiat_edad = 0
cliente_mas_viejo_fiat_nombre = ""

cliente_edad_cuatro_puertas_acumulador = 0
cliente_edad_cuatro_puertas_contador = 0
cliente_edad_cuatro_puertas_promedio = 0.0

vendedor_zapata_ventas = 0
vendedor_quiroz_ventas = 0
vendedor_simino_ventas = 0

minimo_vendedor_ventas = 0
apellido_minimo_vendedor = ""

opcion = ""
bandera_joven = True
bandera_viejo_fiat = True
bandera_maximo_vendedor = True

print("""
| AUTOCITY |
""")

while True:
    nombre_cliente = input("Ingrese el nombre del cliente: ")

    edad_cliente = int(input("Ingrese la edad del cliente (debe ser mayor): "))
    while edad_cliente < 18:
        edad_cliente = int(input(f"Edad inválida ({edad_cliente} años) debe ser mayor de edad, intente de nuevo: "))

    marca_vehiculo = input("Ingrese la marca del vehiculo (Renault, Fiat, BMW): ")
    while marca_vehiculo.lower() != "renault" and marca_vehiculo.lower() != "fiat" and marca_vehiculo.lower() != "bmw":
        marca_vehiculo = input("Marca inválida, ingrese una de las indicadas (Renault, Fiat, BMW): ")

    puertas_cantidad = int(input("Ingrese la cantidad de puertas del vehiculo (2 o 4): "))
    while puertas_cantidad != 2 and puertas_cantidad != 4:
        puertas_cantidad = int(input("Cantidad de puertas inválida, ingrese una de las indicadas (2 o 4): "))

    vendedor_appelido = input("Ingrese el nombre del vendedor. Vendedores: Zapata, Quiroz, Simino: ")
    while vendedor_appelido.lower() != "zapata" and vendedor_appelido.lower() != "quiroz" and vendedor_appelido.lower() != "simino":
        vendedor_appelido = input("Nombre inálido, ingrese uno de los indicados (Zapata, Quiroz, Simino): ")

    # Contar vehiculos vendidos según marca.
    if marca_vehiculo.lower() == "renault":
        vehiculos_renault_vendidos_contador += 1
    # Contar los vehiculos Renault de 2 puertas.
        if puertas_cantidad == 2:
            vehiculos_dos_puertas_renault += 1
    elif marca_vehiculo.lower() == "fiat":
        vehiculos_fiat_vendidos_contador += 1
        # Calcular el cliente mas viejo que compró fiat.
        if edad_cliente > cliente_mas_viejo_fiat_edad or bandera_viejo_fiat == True:   
            cliente_mas_viejo_fiat_edad = edad_cliente
            cliente_mas_viejo_fiat_nombre = nombre_cliente
            bandera_viejo_fiat = False
    else:
        vehiculos_bmw_vendidos_contador += 1

    # Calcular el cliente mas joven.
    if edad_cliente < cliente_mas_joven_edad or bandera_joven == True:
        cliente_mas_joven_edad = edad_cliente
        cliente_mas_joven_nombre = nombre_cliente
        bandera_joven = False

    # Acumular edades y contar los clientes que compren con 4 puertas.
    if puertas_cantidad == 4:
        cliente_edad_cuatro_puertas_acumulador += edad_cliente
        cliente_edad_cuatro_puertas_contador += 1

    # Calcular ventas de vendedores.
    if vendedor_appelido.lower() == "zapata":
        vendedor_zapata_ventas += 1
    elif vendedor_appelido.lower() == "quiroz":
        vendedor_quiroz_ventas += 1
    else:
        vendedor_simino_ventas += 1

    # Consultar al usuario si desea salir.
    opcion = input("¿Desea continuar? (si/no): ")
    while opcion.lower() != "si" and opcion.lower() != "no":
        opcion = input("Opcion inválida, ingrese una de las indicadas (si/no): ")
    if opcion == "no":
        break

# Contar total de vehiculos vendidos.
vehiculos_vendidos_total = vehiculos_renault_vendidos_contador + vehiculos_fiat_vendidos_contador + vehiculos_bmw_vendidos_contador

# Calcular porcentajes de vehiculos vendidos según su marca entre el total vendido.
vehiculos_renault_vendidos_porcentaje = (vehiculos_renault_vendidos_contador / vehiculos_vendidos_total) * 100
vehiculos_fiat_vendidos_porcentaje = (vehiculos_fiat_vendidos_contador / vehiculos_vendidos_total) * 100
vehiculos_bmw_vendidos_porcentaje = (vehiculos_bmw_vendidos_contador / vehiculos_vendidos_total) * 100

# Calcular el vendedor con menos ventas.
# También se puede hacer comparando entre los contadores, no es un mínimo.
if vendedor_zapata_ventas < minimo_vendedor_ventas or bandera_maximo_vendedor == True:
    minimo_vendedor_ventas = vendedor_zapata_ventas
    apellido_minimo_vendedor = "Zapata"
if vendedor_quiroz_ventas < minimo_vendedor_ventas or bandera_maximo_vendedor == True:
    minimo_vendedor_ventas = vendedor_quiroz_ventas
    apellido_minimo_vendedor = "Quiroz"
if vendedor_simino_ventas < minimo_vendedor_ventas or bandera_maximo_vendedor == True:
    minimo_vendedor_ventas = vendedor_simino_ventas
    apellido_minimo_vendedor = "Simino"
    bandera_maximo_vendedor = False

# Calcular promedio de edad de los clientes que compraron 4 puertas.
if cliente_edad_cuatro_puertas_contador > 0:
    cliente_edad_cuatro_puertas_promedio = cliente_edad_cuatro_puertas_acumulador / cliente_edad_cuatro_puertas_contador
else:
    cliente_edad_cuatro_puertas_promedio = "¡No se compraron vehiculos con 4 puertas!"

# Mostrar estadísticas.
print(f""" 
| AUTOCITY |

- Estadísitcas -
Vehiculos vendidos en total: {vehiculos_vendidos_total}
Porcentajes de ventas:
Renalut: {round(vehiculos_renault_vendidos_porcentaje, 2)}% ({vehiculos_renault_vendidos_contador} ventas)
Fiat: {round(vehiculos_fiat_vendidos_porcentaje, 2)}% ({vehiculos_fiat_vendidos_contador} ventas)
BMW: {round(vehiculos_bmw_vendidos_porcentaje, 2)}% ({vehiculos_bmw_vendidos_contador} ventas)
Vehiculos marca Renault de 2 puertas vendidos: {vehiculos_dos_puertas_renault}
Vehiculos BMW vendidos en total: {vehiculos_bmw_vendidos_contador}
El cliente mas joven es: {cliente_mas_joven_nombre} con {cliente_mas_joven_edad} años
El cliente mas mayor que compró un vehiculo marca Fiat es: {cliente_mas_viejo_fiat_nombre} con {cliente_mas_viejo_fiat_edad} años
Promedio de edad de los clientes que comraron un vehiculo de 4 puertas: {cliente_edad_cuatro_puertas_promedio}
El vendedor con menos ventas es: {apellido_minimo_vendedor} con {minimo_vendedor_ventas} ventas realizadas
""")