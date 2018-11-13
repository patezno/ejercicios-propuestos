# Escribe un programa que calcule lo que tiene que cobrar un empleado sabiendo
# que se le tiene que aplicar al sueldo una retención del 20%.

sueldo_bruto = eval(input("Introduce el sueldo en bruto: "))

porcentaje = sueldo_bruto * 0.20
sueldo_neto = sueldo_bruto - porcentaje

print("El sueldo neto es " + str(sueldo_neto) + "€")
