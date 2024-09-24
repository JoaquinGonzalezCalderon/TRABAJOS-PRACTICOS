from cola import Queue
from heap import HeapMin
from heap import HeapMax



# COLA



# 11. Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta
# de origen. 
# Desarrollar las funciones necesarias para resolver las siguientes actividades:

colapj = Queue()

colapj.arrive({"nombre": "Luke Skywalker", "planeta": "Tatooine"})
colapj.arrive({"nombre": "Leia Organa", "planeta": "Alderaan"})
colapj.arrive({"nombre": "Han Solo", "planeta": "Corellia"})
colapj.arrive({"nombre": "Yoda", "planeta": "Dagobah"})
colapj.arrive({"nombre": "Darth Vader", "planeta": "Tatooine"})
colapj.arrive({"nombre": "Jar Jar Binks", "planeta": "Naboo"})
colapj.arrive({"nombre": "Chewbacca", "planeta": "Kashyyyk"})

def imprimir_cola(cola):
    if cola.size() > 0:
        for i in range(cola.size()):
            personaje = cola.on_front()
            print(f"Nombre: {personaje['nombre']}, Planeta: {personaje['planeta']}")
            cola.move_to_end()

print("")
print("")
# a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
print("Punto A")
def mostrarplanetas(cola):
    planetas = {"Alderaan", "Endor", "Tatooine"}
    for i in range(cola.size()):
        personaje = cola.on_front()
        if personaje['planeta'] in planetas:
            print(f"{personaje['nombre']} de {personaje['planeta']}")
        cola.move_to_end()

print("Personajes de Alderaan, Endor, y Tatooine:")
mostrarplanetas(colapj)

print("")
print("")
# b. indicar el plantea natal de Luke Skywalker y Han Solo
print("Punto B")
def planetanatal(cola):
    for i in range(cola.size()):
        personaje = cola.on_front()
        if personaje['nombre'] == 'Luke Skywalker' or personaje['nombre'] == 'Han Solo':
            print(f"{personaje['nombre']} es de {personaje['planeta']}")
        cola.move_to_end()

print("Planeta Natal de los siguientes personajes: ")
planetanatal(colapj)

print("")
print("")
# c. insertar un nuevo personaje antes del maestro Yoda
print("Punto C")
def insertarpj(cola,nuevopj):
    for i in range(cola.size()):
        personaje = cola.on_front()
        if personaje['nombre'] == 'Yoda':
            cola.arrive(nuevopj)
        cola.move_to_end()

insertarpj(colapj, {"nombre": "Sebulba", "planeta": "Malastare"})
imprimir_cola(colapj)


print("")
print("")
# d. eliminar el personaje ubicado después de Jar Jar Binks
print("Punto D")
def eliminarjarjar(cola):
    for i in range(cola.size()):
        personaje = cola.on_front()
        if personaje['nombre'] == 'Jar Jar Binks':
            cola.atention()
        cola.move_to_end()

eliminarjarjar(colapj)
imprimir_cola(colapj) 

print("")
print("------------------------------------------------------------------------------------------")
print("")

# 22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se cono-
# ce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino F) 
# –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro-
# manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

colamcu = Queue()

colamcu.arrive({'nombre': 'Tony Stark', 'superheroe': 'Iron Man', 'genero': 'M'})
colamcu.arrive({'nombre': 'Steve Rogers', 'superheroe': 'Capitán América', 'genero': 'M'})
colamcu.arrive({'nombre': 'Natasha Romanoff', 'superheroe': 'Black Widow', 'genero': 'F'})
colamcu.arrive({'nombre': 'Bruce Banner', 'superheroe': 'Hulk', 'genero': 'M'})
colamcu.arrive({'nombre': 'Carol Danvers', 'superheroe': 'Captain Marvel', 'genero': 'F'})
colamcu.arrive({'nombre': 'Peter Parker', 'superheroe': 'Spider-Man', 'genero': 'M'})
colamcu.arrive({'nombre': 'Scott Lang', 'superheroe': 'Ant-Man', 'genero': 'M'})


# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
print("Punto A")
def capitanamarvel(cola):
    for i in range(cola.size()):
        personaje = cola.on_front()
        if personaje['superheroe'] == 'Captain Marvel':
            print(f"El nombre de Capitana Marvel es {personaje['nombre']}") 
        cola.move_to_end()

capitanamarvel(colamcu)

print("")
print("")
# b. mostrar los nombre de los superhéroes femeninos;
print("Punto B")
def femeninos(cola):
    for i in range(cola.size()):
        personaje = cola.on_front()
        if personaje['genero'] == 'F':
            print(personaje['superheroe'])
        cola.move_to_end()

femeninos(colamcu)

print("")
print("")
# c. mostrar los nombres de los personajes masculinos;
print("Punto C")
def masculinos(cola):
    for i in range(cola.size()):
        personaje = cola.on_front()
        if personaje['genero'] == 'M':
            print(personaje['nombre'])
        cola.move_to_end()

masculinos(colamcu)

print("")
print("")
# d. determinar el nombre del superhéroe del personaje Scott Lang;
print("Punto D")
def scott(cola):
    for i in range(cola.size()):
        personaje = cola.on_front()
        if personaje['nombre'] == 'Scott Lang':
            print(f"El superhéroe de Scott Lang es {personaje['superheroe']}")
        cola.move_to_end()

scott(colamcu)

print("")
print("")  

# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;
print("Punto E")
def letraS(cola):
    for i in range(cola.size()):
        personaje = cola.on_front()
        if personaje['nombre'][0].upper() == 'S':
            print(personaje)
        cola.move_to_end()

letraS(colamcu)


print("")
print("")
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.
print("Punto F")

def carol(cola):
    for i in range(cola.size()):
        personaje = cola.on_front()
        if personaje['nombre'] == 'Carol Danvers':
            print(f"El nombre de superhéroe de Carol Danvers es {personaje['superheroe']}")
        cola.move_to_end()

carol(colamcu)


# HEAP



print("")
print("")


# 5. El gran almirante Thrawn es el estratega del imperio galáctico para combatir contra los re-
# beldes, el mismo normalmente se encuentra desbordado de pedidos de sugerencia de cómo
# actuar por los distintos generales, para lo cual nos solicita desarrollar un algoritmo que le per-
# mita atender los pedidos de ayuda de acuerdo a la prioridad de los mismo en base a los siguien-
# te requerimientos:

# a. se deben contemplar tres niveles de prioridad para la cola;

# b. cada pedido de sugerencia cuenta con la siguiente información: nombre del general solici-
# tante, planeta en el que se encuentra o el más próximo y descripción del pedido;

# c. aquellos pedidos que provengan del “Gran Inquisidor”, el planeta de Lothal o la descrip-
# ción mencione a “Hera Syndulla” tendrán la mayor prioridad;

# d. si el pedido es del “Agente Kallus” o la descripción menciona “Destructor Estelar” o vehí-
# culos “AT-AT” tendrán prioridad media;

# e. el resto de los pedidos serán de prioridad baja;

# f. realizar la atención de la cola almacenando los pedidos de mayor prioridad en una pila
# llamada “bitácora” para revisión y seguimiento;

# g. luego de cada atención se podrá agregar un pedido a la cola.


def determinar_prioridad(nombre, planeta, descripcion):
    # Prioridad Alta
    if nombre == "Gran Inquisidor" or planeta == "Lothal" or "Hera Syndulla" in descripcion:
        return 1
    # Prioridad Media
    elif nombre == "Agente Kallus" or "Destructor Estelar" in descripcion or "AT-AT" in descripcion:
        return 2
    # Prioridad Baja
    else:
        return 3

#Cola de prioridad
heap = HeapMin()
bitacora = []  # Pila para almacenar los pedidos de prioridad alta

# Función para agregar un pedido a la cola de prioridad
def agregar_pedido(nombre, planeta, descripcion):
    prioridad = determinar_prioridad(nombre, planeta, descripcion)
    # Usamos el método "arrive" para agregar el pedido con la prioridad al heap
    heap.arrive([nombre, planeta, descripcion], prioridad)
    print(f"Pedido agregado: {[nombre, planeta, descripcion]} con prioridad {prioridad}")

# Función para atender el pedido de mayor prioridad
def atender_pedido():
    if len(heap.elements) > 0:
        # "atention" para atender el pedido con mayor prioridad
        pedido_atendido = heap.atention()  # Devuelve una tupla con (prioridad, pedido)
        # Si es de prioridad alta, se guarda en la bitácora
        if pedido_atendido[0] == 1:
            bitacora.append(pedido_atendido[1])
        print(f"Pedido atendido: {pedido_atendido[1]}")
    else:
        print("No hay más pedidos en la cola.")

# Ejemplo 

agregar_pedido("Gran Inquisidor", "Lothal", "Necesitamos más naves")
agregar_pedido("Agente Kallus", "Coruscant", "Requiere refuerzos AT-AT")
agregar_pedido("General Zod", "Tatooine", "Hera Syndulla ha caido")
agregar_pedido("General Veers", "Lothal", "El escuadrón AT-AT está en posición")

#Se atiende pedido a pedido

atender_pedido() 
atender_pedido()  
atender_pedido()  
atender_pedido()  


print(f"Bitácora de pedidos prioritarios: {bitacora}")

print("")
print("----------------------------------------")
print("")
# 3. El general Hux es la persona encargada de administrar todas las operaciones de la base Starki-
# ller, para lo cual nos solicita desarrollar un algoritmo que permita controlar las actividades que se realizan, contemplando lo siguiente:

# a. debe contemplar distintas prioridades para el control de operaciones de acuerdo al siguien-
# te criterio: pedidos de líder supremo Snoke y de Kylo Ren nivel tres, de capitán Phasma
# nivel dos y el resto de las operaciones nivel a cargo de los generales de la base de nivel uno;

# b. de cada actividad se conoce quien es el encargado, una descripción, la hora y opcional-
# mente la cantidad de Stormtroopers requeridos;

# c. utilizar una cola de prioridad para administrar las distintas operaciones, debe cargar al
# menos ocho: dos de nivel tres, cuatro de nivel dos y cuatro de nivel uno;

# e. realizar la atención de las operaciones de la cola;

# d. opcionalmente se podrán agregar operaciones luego de atender una;

# f. luego de atender la quinta operación, agregar una operación solicitada por capitán Phasma
# para revisión de intrusos en el hangar B7 que requiere 25 Stormstroopers;

# g. luego de atender la sexta operación, agregar una operación solicitada por el líder supremo
# Snoke para destruir el planeta Takodana.


def definirprioridad(encargado,descripcion,hora,cantidadstorm):
    if encargado == "Snoke" or encargado == "Kylo Ren":
        return 3
    elif encargado == "Phasma":
        return 2
    else:
        return 1

heap3 = HeapMax()

def agregarop(encargado,descripcion,hora,cantidadstorm):
    prioridad = definirprioridad(encargado,descripcion,hora,cantidadstorm)
    heap3.arrive([encargado, descripcion,hora,cantidadstorm], prioridad)
    print(f"Pedido agregado: {[encargado, descripcion, hora,cantidadstorm]} con prioridad {prioridad}")

def atenderop():
    if len(heap3.elements) > 0:
        opatentida = heap3.atention()
        print(f"Operación atendida: {opatentida}")
        mostrarcola()  # Mostrar el estado de la cola después de atender
    else:
        print("No hay operaciones para atender.")

def mostrarcola():
    print("Estado actual de la cola de prioridad:")
    for elemento in heap3.elements:
        print(f"Prioridad {elemento[0]} - {elemento[1]}")



agregarop("Snoke", "Reunion de Canciller", "10:00", 2)
agregarop("Phasma", "Entrenamiento StormTrooper", "12:00", 304)
agregarop("Kylo Ren", "Revision de operaciones nivel 3", "14:00", 0)
agregarop("General Veers", "Revision de operaciones nivel 2", "16:00", 0)
agregarop("General Zod", "Revision de operaciones nivel 1", "18:00", 0)

atenderop()
atenderop()
atenderop()
atenderop()
atenderop()

agregarop("Phasma","Revision de intrusos en Hangar B7","09:00",25)

atenderop()

agregarop("Snoke", "Destruir planeta Takodana","04:00",0)

atenderop()