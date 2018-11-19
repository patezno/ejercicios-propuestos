# Lee por teclado 5 números enteros positivos, y escribe cuál es el mayor de los números
# introducidos.

def comprobar(lista):
    numero = max(lista)
    print("El numero " + str(numero) + " es el mayor de todos")

def introduccion_numeros(lista):
    lista.append(eval(input("Introduce un número: ")))
    lista.append(eval(input("Introduce otro número: ")))
    lista.append(eval(input("Introduce otro número: ")))
    lista.append(eval(input("Introduce otro número: ")))
    lista.append(eval(input("Introduce otro número: ")))
    return lista

lista = []
introduccion_numeros(lista)
comprobar(lista)
