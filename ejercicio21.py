# Escribe un programa que solicite por teclado 5 números positivos, forzando al usuario a que
# únicamente introduzca valores positivos. A continuación el programa tiene que escribe cuál
# es el valor más pequeño y cuál es el mayor valor de los introducidos por el usuario.
from ejercicio19 import comprobar
from ejercicio20 import negativos

def comprobar_menor(num1, num2, num3, num4, num5):
    if num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5:
        print("El numero " + str(num1) + " es el menor de todos")
    elif num2 < num1 and num2 < num3 and num2 < num4 and num2 < num5:
        print("El numero " + str(num2) + " es el menor de todos")
    elif num3 < num2 and num3 < num1 and num3 < num4 and num3 < num5:
        print("El numero " + str(num3) + " es el menor de todos")
    elif num4 < num2 and num4 < num3 and num4 < num1 and num4 < num5:
        print("El numero " + str(num4) + " es el menor de todos")
    elif num5 < num2 and num5 < num3 and num5 < num4 and num5 < num1:
        print("El numero " + str(num5) + " es el menor de todos")
    else:
        print("Algunos numeros son iguales")


num1 = eval(input("Introduce un número: "))
num2 = eval(input("Introduce otro número: "))
num3 = eval(input("Introduce otro número: "))
num4 = eval(input("Introduce otro número: "))
num5 = eval(input("Introduce otro número: "))

negativos(num1, num2, num3, num4, num5)
comprobar(num1, num2, num3, num4, num5)
comprobar_menor(num1, num2, num3, num4, num5)
