""" 
Ejercicio integrador 1

Ferrete Lámparas
En una ferretería se quiere implementar un sistema que permita a los usuarios saber cuánto deberán
pagar por la compra de lámparas de bajo consumo. Se tiene en cuenta que todas las lámparas cuestan
$800.
A partir de la cantidad y marca de las lámparas compradas (solo se puede comprar una marca por vez)
se aplicará el siguiente descuento:
- Si compra 6 o más lámparas bajo consumo tiene un descuento del 50%.
- Si compra 5 lámparas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si
es de otra marca el descuento es del 30%.
- Si compra 4 lámparas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un
descuento del 25 % y si es de otra marca el descuento es del 20%.
- Si compra 3 lámparas bajo consumo marca "ArgentinaLuz" el descuento es del 15%, si es
“FelipeLamparas” se hace un descuento del 10 % y si es "PatitoFeo" un 5%.
Por otro lado, si el importe final con descuento suma más de $4000 se obtiene un descuento adicional
de 5%.
Mostrar por pantalla:
Marca, cantidad de lámparas, total a pagar sin descuento, el descuento obtenido si corresponde, el
descuento adicional (si corresponde) y el total a pagar con descuento.
"""

lampara_precio = 800.0
lamparas_compradas = 0
marca_lampara_ingresada = ""
marca_lampara_1 = "ArgentinaLuz"
marca_lampara_2 = "FelipeLamparas"
marca_lampara_3 = "PatitoFeo"

porcentaje_descuento = 0

precio_total_lamparas = 0.0
importe_preliminar = 0.0
importe_final = 0.0

# Ingresar cantidad de lamparas a comprar.
lamparas_compradas = int(input("Ingrese la cantidad de lámparas de bajo consumo desea comprar: "))
marca_lampara_ingresada = input("Ingrese la marca de lamparas que desea comprar: ")

# Calcular precio sin descuento.
precio_total_lamparas = lamparas_compradas * lampara_precio

# Calcular el primer descuento.
if lamparas_compradas > 5:
    porcentaje_descuento = 50
elif lamparas_compradas == 5:
    if marca_lampara_ingresada == marca_lampara_1:
        porcentaje_descuento = 40
    else:
        porcentaje_descuento = 30
elif lamparas_compradas == 4:
    if marca_lampara_ingresada == marca_lampara_1 or marca_lampara_ingresada == marca_lampara_2:
        porcentaje_descuento = 25
    else:
        porcentaje_descuento = 20
elif lamparas_compradas == 3:
    if marca_lampara_ingresada == marca_lampara_1:
        porcentaje_descuento = 15
    elif marca_lampara_ingresada == marca_lampara_2:
        porcentaje_descuento = 10
    elif marca_lampara_ingresada == marca_lampara_3:
        porcentaje_descuento = 5
else:
    porcentaje_descuento = 0

importe_preliminar = precio_total_lamparas * porcentaje_descuento / 100
importe_final = precio_total_lamparas - importe_preliminar

# Calcular el segundo descuento si corresponde.
if importe_final > 4000.0:
    porcentaje_descuento = 5
else:
    porcentaje_descuento = 0

descuento_adicional = importe_final * porcentaje_descuento / 100
importe_final += - descuento_adicional

print(f""" 
+-----------------+
    | FACTURA |
Lamparas: {lamparas_compradas}
Marca: {marca_lampara_ingresada}
Importe sin descuentos: ${precio_total_lamparas}
Importe final: ${importe_final}
- Vuelva pronto :) -
+-----------------+
""")

""" 
Solución con cuentas dentro de los if's.
# Calcular descuento del 50%.
if lamparas_compradas >= 6:
    importe_preliminar = precio_total_lamparas * descuento_50 / 100
    importe_final = precio_total_lamparas - importe_preliminar

# Calcular descuento del 40% y del 30%.
if lamparas_compradas == 5 and marca_lampara_ingresada == marca_lampara_1:
    importe_preliminar = precio_total_lamparas * descuento_40 / 100
    importe_final = precio_total_lamparas - importe_preliminar
else:
    importe_preliminar = precio_total_lamparas * descuento_30 / 100
    importe_final = precio_total_lamparas - importe_preliminar

# Calcular descuento del 25% y del 20%.
if lamparas_compradas == 4 and (marca_lampara_ingresada == marca_lampara_1 or marca_lampara_ingresada == marca_lampara_2):
    importe_preliminar = precio_total_lamparas * descuento_25 / 100
    importe_final = precio_total_lamparas - importe_preliminar
else:
    importe_preliminar = precio_total_lamparas * descuento_20 / 100
    importe_final = precio_total_lamparas - importe_preliminar

# Calcular descuento del 15%, 10% y del 5%.
if lamparas_compradas == 3 and marca_lampara_ingresada == marca_lampara_1:
    importe_preliminar = precio_total_lamparas * descuento_15 / 100
    importe_final = precio_total_lamparas - importe_preliminar
elif marca_lampara_ingresada == marca_lampara_2:
    importe_preliminar = precio_total_lamparas * descuento_10 / 100
    importe_final = precio_total_lamparas - importe_preliminar
elif marca_lampara_ingresada == marca_lampara_3:
    importe_preliminar = precio_total_lamparas * descuento_5 / 100
    importe_final = precio_total_lamparas - importe_preliminar
else:
    importe_preliminar = precio_total_lamparas
    importe_final = precio_total_lamparas
    """
