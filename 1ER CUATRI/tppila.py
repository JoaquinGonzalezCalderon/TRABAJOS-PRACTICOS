from pila import Stack
from random import randint


# 16. Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire
# strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que
# permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en am-
# bos episodios.


def ejercicio16(pila1, pila2):
    interseccion = []  # lista para poner los personajes de ambos episodios
    pilatemporal = []  

    # transfiere todos los personajes de pila1 (episodio V) a una pila temporal.
    while pila1:
        pilatemporal.append(pila1.pop())

    # compara lo de la pila 1 con la pila 2 (distintos episodios)
    while pilatemporal:
        elemento = pilatemporal.pop()  
        if elemento in pila2:  # Si el elemento está en pila2, es parte de la intersección.
            interseccion.append(elemento)  

    return interseccion  

# Crea las pilas con los personajes de cada episodio.
pilaepV = ["Luke Skywalker", "Princess Leia", "Han Solo", "Darth Vader"]
pilaepVII = ["Rey", "Finn", "Kylo Ren", "Poe Dameron", "Han Solo"]

resultadointerseccion = ejercicio16(pilaepV, pilaepVII)
print("Intersección de pilas:", resultadointerseccion)

print("")
print("-----------------------------------------------------------------")
print("")

# 24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
# su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
# necesarias para resolver las siguientes actividades:

# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posi-
# ción uno la cima de la pila;

# b. determinar los personajes que participaron en más de 5 películas de la saga, además indi-
# car la cantidad de películas en la que aparece;

# c. determinar en cuantas películas participo la Viuda Negra (Black Widow)

# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

pilamarvel = Stack()  

# personajes con la cantidad de apariciones
pilamarvel = [
    ("Groot", 6),
    ("Doctor Strange", 6),
    ("Capitan America", 11),
    ("Black Widow", 9),
    ("Black Panther", 4),
    ("Rocket Raccoon", 6),
]

# a. Determinar la posición de Groot y Rocket Raccoon 
print("")
print("GROOT Y ROCKET RACCOON")
print("")

contador = 0  

for personaje, apariciones in pilamarvel:
    contador = contador + 1  

    if personaje == "Groot":  
        print("Posición de Groot: ", contador)

    if personaje == "Rocket Raccoon":  
        print("Posición de Rocket: ", contador)

# b. Determinar los personajes con más de 5 apariciones.
print("")
print("MAS DE 5 PELICULAS")
print("")

for personaje, apariciones in pilamarvel:
    if apariciones > 5:  # comprueba si tiene mas de 5 apariciones
        print("El personaje: " + personaje + " aparece en:  ")
        print(apariciones)

# c. Determinar en cuántas películas participó Black Widow.
print("")
print("BLACKWIDOW")
print("")

for personaje, apariciones in pilamarvel:
    if personaje == "Black Widow":  # Verifica si el personaje es Black Widow.
        print("Black Widow aparecio en: ")
        print(apariciones)

# d. Mostrar todos los personajes cuyos nombres comienzan con C, D y G.
print("")
print("PERSONAJES CON C, D Y G")
print("")

for personaje, apariciones in pilamarvel:
    if personaje.startswith("C"):
        print(personaje)
    if personaje.startswith("D"):
        print(personaje)
    if personaje.startswith("G"):
        print(personaje)
