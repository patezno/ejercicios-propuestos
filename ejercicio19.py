# Lee por teclado 5 números enteros positivos, y escribe cuál es el mayor de los números
# introducidos.

def comprobar(num1, num2, num3, num4, num5):
    if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
        print("El numero " + str(num1) + " es el mayor de todos")
    elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
        print("El numero " + str(num2) + " es el mayor de todos")
    elif num3 > num2 and num3 > num1 and num3 > num4 and num3 > num5:
        print("El numero " + str(num3) + " es el mayor de todos")
    elif num4 > num2 and num4 > num3 and num4 > num1 and num4 > num5:
        print("El numero " + str(num4) + " es el mayor de todos")
    elif num5 > num2 and num5 > num3 and num5 > num4 and num5 > num1:
        print("El numero " + str(num5) + " es el mayor de todos")
    else:
        print("Algunos numeros son iguales")


num1 = eval(input("Introduce un número: "))
num2 = eval(input("Introduce otro número: "))
num3 = eval(input("Introduce otro número: "))
num4 = eval(input("Introduce otro número: "))
num5 = eval(input("Introduce otro número: "))

comprobar(num1, num2, num3, num4, num5)
