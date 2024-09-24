from cola import Queue
from pila import Stack
from random import randint

pila = Stack()
pila_aux = Stack()

cola_1 = Queue()
cola_2 = Queue()

# Ejercicio 1

# for i in range(5):
#     letra = chr(randint(65, 90))
#     cola_1.arrive(letra)

# for i in range(cola_1.size()):
#     print(cola_1.on_front())
#     cola_1.move_to_end()

# print()
# vocales = ["A", "E", "I", "O", "U"]

# for i in range(cola_1.size()):
#     if cola_1.on_front() in vocales:
#         cola_1.atention()
#     else:
#         cola_1.move_to_end()

# for i in range(cola_1.size()):
#     print(cola_1.on_front())
#     cola_1.move_to_end()

# Ejercicio 2

for i in range(5):
    cola_1.arrive(randint(1, 99))

print()
print("Queue original")
for i in range(cola_1.size()):
    print(cola_1.on_front())
    cola_1.move_to_end()

print("Pasaje a pila")
while cola_1.size() > 0:
    pila.push(cola_1.atention)

print("Pasaje a cola nuevamente")
while pila.size() > 0:
    cola_1.arrive(pila.pop())

print()
print("Queue inversa")
for i in range(cola_1.size()):
    print(cola_1.on_front())
    cola_1.move_to_end()
