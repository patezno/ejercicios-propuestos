# Escribe un programa que pida por teclado un número y que a continuación
# muestre el mensaje el número leído es positivo o bien el número leído
# es negativo dependiendo de que el número introducido por teclado
# sea positivo o negativo. Consideramos al número 0 positivo.

num = eval(input("Introduzca un número: "))

if num >= 0:
    print("El número " + str(num) + " es positivo")
else:
    print("El número " + str(num) + " es negativo")
