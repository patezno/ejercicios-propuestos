# Repite el programa anterior, pero chequeando que el usuario no introduzca números
# negativos. Si se da esta circunstancia hay que visualizar un mensaje de error, forzando al
# usuario a que introduzca números positivos.


def introduccion_numeros(lista):
    lista.append(eval(input("Introduce un número: ")))
    lista.append(eval(input("Introduce otro número: ")))
    lista.append(eval(input("Introduce otro número: ")))
    lista.append(eval(input("Introduce otro número: ")))
    lista.append(eval(input("Introduce otro número: ")))
    return lista


def negativos(lista):
    for n in lista:
        if n < 0:
            print("Has introducido numeros negativos")
            print("Solo se aceptan positivos")
            del lista[:]
            introduccion_numeros(lista)
    return lista


def comprobar(lista):
    numero = max(lista)
    print("El numero " + str(numero) + " es el mayor de todos")

lista = []
introduccion_numeros(lista)
negativos(lista)
comprobar(lista)
