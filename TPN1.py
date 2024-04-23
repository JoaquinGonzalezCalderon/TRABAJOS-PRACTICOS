# Desarrollar una función que permita convertir un número romano en un número decimal.


def numeroromanos(numero):

    numeros = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    if (
        "IIII" in numero
        or "VV" in numero
        or "XXXX" in numero
        or "LL" in numero
        or "CCCC" in numero
        or "DD" in numero
        or "MMMM" in numero
    ):
        raise ValueError("Numero romano invalido: revisar repeticiones invalidas")

    if len(numero) == 0:
        return 0

    elif len(numero) == 1:
        return numeros[numero[0]]

    elif numeros[numero[0]] < numeros[numero[1]]:
        return numeros[numero[1]] - numeros[numero[0]] + numeroromanos(numero[2:])

    else:
        return numeros[numero[0]] + numeroromanos(numero[1:])


print(numeroromanos("I"))

# El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
# objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
# ayuda de la fuerza” realizar las siguientes actividades:

# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
# queden más objetos en la mochila;

# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
# car para encontrarlo;

# c. Utilizar un vector para representar la mochila.

from typing import List


def usarlafuerza(objeto: str, mochila: List[str], contador=0) -> str:

    if not mochila:
        return (
            f"No encontraste {objeto} en la mochila, un error que te costo la vida..."
        )

    elif mochila[0] == "sable de luz":
        return f"¡Obtuviste un sable laser! Contador: {contador}"

    else:
        return usarlafuerza(objeto, mochila[1:], contador + 1)


mochiladeluke = [
    "holocron sith",
    "blaster",
    "sable de luz",
    "casco mandaloriano",
    "casco stormtrooper",
]

print(usarlafuerza("sable de luz", mochiladeluke))
