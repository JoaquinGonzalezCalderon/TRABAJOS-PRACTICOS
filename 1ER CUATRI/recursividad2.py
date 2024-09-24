
#4

#2 elevado a 3 = 2 * 2 * 2 = n elevado a m = n * (n + m-1)

from cmath import log


def potencia(base,exponente):
    if exponente == 0:
        return 1
    
    else:
        return base * potencia(base,exponente-1) 
    
print("El resultado es: ")
print(potencia(45,3))

#6

def invertido(palabra):
        if len(palabra) == 0:
            return palabra    
        else:
            return palabra[-1] + invertido(palabra[:-1])
        
print(invertido("hola"))

#7

def serie(n):
    if n == 0:
        return n

    else:
        return 1/n + serie(n-1)
    
print(serie(2))    
    
# 8

def binario(numero):
    if numero == 1 :
        return str(1)
    
    else:
        return binario(numero//2) + str(numero%2)
    
print(binario(6))


#10

def digitos(numero):
    if numero < 10:
        return 1
    
    else:
        return 1 + digitos(numero//10)
         
print(digitos(2421))

# 14

def digitossuma(numero):
    if numero < 10:
        return numero
    
    else:
        return numero%10 + digitossuma(numero//10)  
         
print(digitossuma(124))

#17

vector = ['enrique', 'pedrito', 'agustin','ostia tio']

def vectorinverso(vector):
    if len(vector) == 1:
        print (vector[0])
    
    else:
        print (vector[-1])
        vectorinverso(vector[:-1])
        
vectorinverso(vector)

#22. El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
#otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
#objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
#ayuda de la fuerza” realizar las siguientes actividades:

#a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
#queden más objetos en la mochila;

#b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
#car para encontrarlo;

#c. Utilizar un vector para representar la mochila.

mochila = ['casco mandaloriano', 'cristal kyber', 'holocron sith', 'sable jedi']

