# Escribe un programa que pida por teclado una cantidad de dinero y que a continuación
# muestre la descomposición de dicho importe en el menor número de billetes y monedas de
# 100, 50, 20, 10, 5, 2 y 1 euro. En el caso de que alguna moneda no intervenga en la
# descomposición no se tiene que visualizar nada en la pantalla. Para una cantidad de 2236
# euros la salida que generaría el programa sería:
#     22 billetes de 100 euros
#     1 billete de 20 euros
#     1 billete de 10 euros
#     1 billete de 5 euros
#     1 moneda de 1 euro

money = eval(input("Introduce la cantidad de dinero: "))

# def billetes(cantidad):
#     numero_monedas = [0, 0, 0, 0, 0]
#     tipos_monedas = [100, 20, 10, 5, 1]
#     resto = cantidad
#     posicion_tipo_monedas = 0
#
#     while resto != 0:
#         numero_monedas[posicion_tipo_monedas] = resto / tipos_monedas[posicion_tipo_monedas]
#         resto = resto % tipos_monedas[posicion_tipo_monedas]
#         posicion_tipo_monedas += 1
#     return numero_monedas

print(billetes(money))
