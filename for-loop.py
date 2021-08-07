#!/usr/bin/env python3

#creamos nuestra lista.
numeros = [1, 2, 3, 4, 5, 6, 7]
nombres = ["Sam", "Mary", "Camila", "Sofia", "Andrea"]

#creamos el bucle for.
if __name__=="__main__":
    for numbers in numeros:
        print("Numero: {}".format(numbers))

    for name in nombres:
        print("Nombre: {}".format(name))
