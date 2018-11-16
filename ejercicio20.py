# Repite el programa anterior, pero chequeando que el usuario no introduzca números
# negativos. Si se da esta circunstancia hay que visualizar un mensaje de error, forzando al
# usuario a que introduzca números positivos.
from ejercicio19 import comprobar

def negativos(num1, num2, num3, num4, num5):
    while num1 < 0 or num2 < 0 or num3 < 0 or num4 < 0 or num5 < 0:
        print("Has introducido numeros negativos")
        print("Solo se aceptan positivos")

        num1 = eval(input("Introduce un número: "))
        num2 = eval(input("Introduce otro número: "))
        num3 = eval(input("Introduce otro número: "))
        num4 = eval(input("Introduce otro número: "))
        num5 = eval(input("Introduce otro número: "))

    return num1, num2, num3, num4, num5

num1 = eval(input("Introduce un número: "))
num2 = eval(input("Introduce otro número: "))
num3 = eval(input("Introduce otro número: "))
num4 = eval(input("Introduce otro número: "))
num5 = eval(input("Introduce otro número: "))

negativos(num1, num2, num3, num4, num5)
comprobar(num1, num2, num3, num4, num5)
