from pila import Stack
from random import randint

pila = Stack()
pila_aux = Stack()

# -------------------------------------------------

# Ejercicio 1 opcion 1

# for i in range(5):
#     num= randint(1,99):
#     print(num)
#     pila.push(num)

# buscar = int(input("Ingrese el numero que desea buscar"))

# acc=0

# while pila.size() > 0:
#     data = pila.pop()
#     if data == buscar:
#         acc += 1

# print("El numero," ,buscar , "se repitio", acc, "veces" )


# pila.push(randint(1, 99))
# print(pila.size())


# Ejercicio 1 opcion 2

# def concurrencia(numero):
#     print()
#     while pila.size() > 0:
#         if pila.pop() == numero:
#             contador = contador + 1
#         else:
#             return "No hay concurrencias con el numero"


# print(concurrencia(5))

# -------------------------------------------------

# Ejercicio 2

# while pila.size() > 0:
#     if pila.on_top() % 2 == 1: #Chequea si es impar
#         pila.pop()
#     else:
#         pila_aux.push(pila.pop())

#     #VERSION SIMPLIFICADA
#     data = pila.pop()
#     if data % 2 == 0:
#         pila_aux.push(data)

# while pila_aux.size() > 0:
#     pila.push(pila_aux.pop())

# print()
# print(pila.size())

# -------------------------------------------------

# Ejercicio 3

# for i in range(5):
#     num = randint(1, 10)
#     print(num)
#     pila.push(num)

# buscar = int(
#     input("Ingrese el numero que quiera cambiar, si este se encuentra (del 1 al 10): ")
# )
# intercambio = int(input("Ahora ingrese el numero reemplazo: "))

# while pila.size() > 0:
#     data = pila.pop()
#     if data == buscar:
#         pila_aux.push(intercambio)
#     else:
#         pila_aux.push(data)


# while pila_aux.size() > 0:
#     pila.push(pila_aux.pop())

# # Muestra la pila
# print("Contenido de la pila después del reemplazo:")
# while pila.size() > 0:
#     print(pila.pop())

# -------------------------------------------------

# Ejercicio 4

# print("Pila original: ")
# print()
# for i in range(5):
#     num = randint(1, 99)
#     print(num)
#     pila.push(num)

# while pila.size() > 0:
#     pila_aux.push(pila.pop())

# while pila_aux.size() > 0:
#     pila.push(pila_aux.pop())

# print()
# print("Contenido de pila: ")
# print()

# while pila.size() > 0:
#     print(pila.pop())

# -------------------------------------------------

# Ejercicio 5

# palabra = input("Ingrese la palabra: ")
# palabraog = palabra
# for letra in palabra:
#     pila.push(letra)

# palabra2 = ""
# while pila.size() > 0:
#     pila_aux.push(pila.pop())

# while pila_aux.size() > 0:
#     palabra2 += pila_aux.pop()

# if palabra2 == palabraog:
#     print("La palabra es un palindromo")
# else:
#     print("La palabra no es un palindromo")

# -------------------------------------------------

# Ejercicio 6

# palabra = input("Ingrese la palabra: ")

# for letra in palabra:
#     pila.push(letra)

# while pila.size() > 0:
#     print(pila.pop())

# -------------------------------------------------

# Ejercicio 7
