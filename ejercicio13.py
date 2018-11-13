# Diseña un programa que calcule el importe final de una venta considerando
# que sobre el valor bruto se hace un descuento según la siguiente tabla:
#     a. Valores <=20 implican un descuento del 0%
#     b. Valores >20 y <=100 implican un descuento del 5%
#     c. Valores >100 implican un descuento 10%


valor = eval(input("Introduce el valor bruto: "))

if valor <= 20:
    print("El importe final es " + str(valor))
elif valor > 20 and valor <= 100:
    descuento = valor * 0.05
    importe_final = valor - descuento
    print("El importe final es " + str(importe_final))
elif valor > 100:
    descuento = valor * 0.10
    importe_final = valor - descuento
    print("El importe final es " + str(importe_final))
