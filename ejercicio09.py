# Escribe un programa que nos pida por teclado dos números enteros
# y que a continuación muestre en pantalla la suma de los dos números solamente
# si son los dos positivos. Si no se cumple que los dos números sean positivos
# se visualizará un mensaje indicándolo. La salida ha de tener
# el siguiente formato: “La suma de los dos números es: XXX” o “No se calcula la
# suma porque alguno de los números o los dos no son positivos”.

num1 = eval(input("Introduce el primer número: "))
num2 = eval(input("Introduce el segundo número: "))

if num1 and num2 >= 0:
    suma = num1 + num2
    print("La suma de los dos números es: " + str(suma))
else:
    print("No se calcula la suma porque alguno de los números o los dos no son positivo")
