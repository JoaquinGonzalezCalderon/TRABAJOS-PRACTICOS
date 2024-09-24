#Ejercicios recursividad

#2. Implementar una función que calcule la suma de todos los números enteros comprendidos
#   entre cero y un número entero positivo dado.

def sumanumeros(numero):
    if numero == 0:
        return 0
    else:
        return numero + sumanumeros(numero-1)
    
print (sumanumeros(5))

#3. Implementar una función para calcular el producto de dos números enteros dados.

def productodenumeros(numero1, numero2):
    if numero1 == 0 or numero2 == 0:
        return  0
    else:
        return numero2 + productodenumeros(numero1-1,numero2)
    
print(productodenumeros(2,10)) 

#4. Implementar una función para calcular la potencia dado dos números enteros, el primero re-
#presenta la base y segundo el exponente.

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base,exponente-1)
    
print(potencia(2,2))

#6. Dada una secuencia de caracteres, obtener dicha secuencia invertida.

def invertido(palabra):
    if len(palabra)== 0:
        return palabra
    else:
        return invertido(palabra[1:]) + palabra[0]
    
print(invertido("pito durito"))

#7. Desarrollar un algoritmo que permita calcular la siguiente serie:

def serie (n):
    if n == 1:
        return 1
    else:
        return 1/n + serie(n-1)
    
print(serie(5))

#Decimal a binario




    