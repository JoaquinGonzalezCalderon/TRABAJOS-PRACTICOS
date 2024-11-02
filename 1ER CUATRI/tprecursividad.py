# Desarrollar una función que permita convertir un número romano en un número decimal.


def numeroromanos(numero):
    
    numeros = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    # Verificación de patrones inválidos de repetición en el número romano ingresado.
    if (
        "IIII" in numero       
        or "VV" in numero      
        or "XXXX" in numero    
        or "LL" in numero      
        or "CCCC" in numero    
        or "DD" in numero      
        or "MMMM" in numero    
        or "IIX" in numero     
    ):
        raise ValueError("Numero romano invalido: revisar repeticiones invalidas / Ingresos invalidos")

    # Caso base: si el número es una cadena vacía, se devuelve 0 (termina la recursión).
    if len(numero) == 0:
        return 0

    # Caso base: si el número tiene un solo símbolo, se devuelve su valor correspondiente.
    elif len(numero) == 1:
        return numeros[numero[0]]

    # Caso recursivo: si el valor del primer símbolo es menor que el segundo, se resta el primero al segundo.
    elif numeros[numero[0]] < numeros[numero[1]]:
        # Realiza la resta y continúa la recursión con el número a partir del tercer símbolo.
        return numeros[numero[1]] - numeros[numero[0]] + numeroromanos(numero[2:])

    # Caso recursivo: si el valor del primer símbolo es mayor o igual al segundo, se suma el valor del primer símbolo.
    else:
        # Realiza la suma y continúa la recursión con el número a partir del segundo símbolo.
        return numeros[numero[0]] + numeroromanos(numero[1:])

print("PUNTO 1 RECURSIVIDAD")
print(numeroromanos("X"))  
print("")


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
    # Caso base: si la mochila está vacía y no se encontró el sable, se indica que no se encontró el objeto.
    if not mochila:
        return f"No encontraste {objeto} en la mochila, un error que te costo la vida..."

    # Caso base: si el primer objeto en la mochila es el sable de luz, se devuelve el mensaje con el contador actual.
    elif mochila[0] == "sable de luz":
        return f"¡Obtuviste un sable laser! Contador: {contador}"

    # Caso recursivo: si el primer objeto no es el sable de luz, continúa la búsqueda en el resto de la mochila.
    else:
        return usarlafuerza(objeto, mochila[1:], contador + 1)

# Ejemplo 
mochiladeluke = [
    "holocron sith",
    "blaster",
    "sable de luz",
    "casco mandaloriano",
    "casco stormtrooper",
]

print("PUNTO 2 RECURSIVIDAD")
print(usarlafuerza("sable de luz", mochiladeluke))  
print("")