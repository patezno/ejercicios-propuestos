# Escribe un programa que visualice los n-primeros múltiplos de 2, siendo n un valor leído por
# teclado

num = eval(input("Introduce un número: "))


def multiplos(num):
    lista = []
    count = 0
    multiplo = 1
    while count < num:
        multiplo = multiplo * 2
        lista.append(multiplo)
        count += 1
    return lista

print("Los " + str(num) + " primeros multiplos de 2 son:")
print(multiplos(num))
