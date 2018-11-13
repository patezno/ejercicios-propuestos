# Escribe un programa que pida por teclado dos números y que muestre en pantalla
# uno de los dos mensajes siguientes en función de los números leídos:
# a) el primer número (valor) es mayor que el segundo (valor)
# (introduciendo el valor de los números en el mensaje);
# b) el primer número (valor) es menor que el segundo (valor; c) los dos números
# son iguales (valor).

num1 = eval(input("Introduce el primer número: "))
num2 = eval(input("Introduce el segundo número: "))

if num1 > num2:
    print("El primer número " + str(num1) + " es mayor que el segundo número " + str(num2))
elif num2 > num1:
    print("El primer número " + str(num1) + " es menor que el segundo número " + str(num2))
elif num1 == num2:
    print("Los dos números " + str(num1) + " y " + str(num2) + " son iguales")
