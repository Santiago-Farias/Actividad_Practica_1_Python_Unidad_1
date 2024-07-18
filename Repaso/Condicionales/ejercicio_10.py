"""
Ejercicio 10
Ingresar el sueldo, estado civil (casado o soltero) y cantidad de hijos de un empleado. Determinar si el
empleado debe o no pagar el impuesto a las ganancias. El mismo no se pagará si el empleado es
casado con hijos y sus ingresos son menores a $2200000.
"""

empleado_sueldo = float(input("Ingrese su sueldo: "))
empleado_estado_civil = input("Ingrese su estado civil (casado o soltero): ")
empleado_hijos_cantidad = int(input("Ingrese la cantidad de hijos que tiene: "))

if empleado_sueldo < 2200000 and (empleado_estado_civil.lower() == "casado" or empleado_estado_civil.lower() == "soltero" or empleado_hijos_cantidad > 0):
        print("Usted no debe pagar impuesto a las ganancias.")
else:
    print("Usted debe pagar el impuesto a las ganancias.")