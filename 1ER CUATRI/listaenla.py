def search(list_values, criterio, value):
    for index, personaje in enumerate(list_values):
        if personaje[criterio] == value:
            return index
        
def searchlista(list_values, criterio, value):
    for index, personaje in enumerate(list_values):
        if personaje[0][criterio] == value:
            return index

# print(f'Yoda esta en la posicion {search(personajes_star_wars, criterio, buscado)}')

#! eliminar un elemento de la lista
def remove(list_values, criterio, value):
    index = search(list_values, criterio, value)
    if index is not None:
        return list_values.pop(index)

# eliminar = 'R2-D2'
# result_delete = remove(personajes_star_wars, criterio, eliminar)
# print(f'Eliminar {eliminar} resultado: {result_delete}')
#! barrido
def show_list(title, list_values):
    print()
    print(f"{title}")
    for index, elemento in enumerate(list_values):
        print(index, elemento)
    print()

#! criterios de orden
def by_name(item):
    return item['nombre']

def by_namelista(item):
    return item[0]['nombre']


def by_height(item):
    return item['altura']
# lista = [1,2,3,4,523,3,123]

# #tamaño
# print(len(lista))

# #insertar
# lista.insert(2,32)

# #barrido
# for elemento in lista:
#     print(elemento)

# #eliminado
# try:
#     eliminado = lista.remove(elemento)
# except ValueError:
#     print("El elemento a eliminar no esta en la lista")

# if 67 in lista:
#      eliminado = lista.remove(elemento)
# else:
#     print("El elemento a eliminar no esta en la lista")

# #ordenar
# lista.sort()

# lista.sort(reverse=False)

# #busqueda
# try:
#     print('posicion', lista.index())
# except ValueError:
#     print("El elemento que busca no esta en la lista")

# Ejercicio 1 = Diseñar un algoritmo que permita contar la cantidad de nodos de una lista.

# Ejercicio 2 = Diseñar un algoritmo que elimine todas las vocales que se encuentren en una lista de caracteres.

# listacaracteres = ["e", "a", "b", "c", "d", "u", "x"]

# copialista = listacaracteres.copy()

# for elemento in copialista:

#     if elemento in {"a", "e", "i", "o", "u"}:

#         try:
#             listacaracteres.remove(elemento)

#         except ValueError:
#             print("Error")

# print(listacaracteres)

# Ejercicio 3 = Dada una lista de números enteros, implementar un algoritmo para dividir dicha lista en dos,
# una que contenga los números pares y otra para los números impares.

# listanumeros = [2, 5, 6, 3, 4, 6, 4, 2]
# print("Longitud de lista original: ", listanumeros.__len__())
# listapar = []
# listaimpar = []

# copialista = listanumeros.copy()

# for elemento in copialista:
#     if elemento % 2 == 0:
#         listapar.append(elemento)

#     else:
#         listaimpar.append(elemento)

# print("Lista par: ", listapar)
# print("Lista impar: ", listaimpar)

# Ejercicio 4 = Implementar un algoritmo que inserte un nodo en la i-ésima posición de una lista.

# Ejercicio 5 = Dada una lista de números enteros eliminar de estas los números primos.

# 6. Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
# casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesa
# -rias para poder realizar las siguientes actividades:

#Lista con 15 superheroes

# superheroes = [
#     {
#         "nombre": "Spider-Man",
#         "año_aparicion": 1962,
#         "casa_comic": "Marvel",
#         "biografia": "Peter Parker, un joven que obtiene habilidades arácnidas después de ser mordido por una araña radiactiva."
#     },
#     {
#         "nombre": "Batman",
#         "año_aparicion": 1939,
#         "casa_comic": "DC",
#         "biografia": "Bruce Wayne, un millonario que combate el crimen en Gotham City usando su intelecto y habilidades físicas."
#     },
#     {
#         "nombre": "Mujer Maravilla",
#         "año_aparicion": 1941,
#         "casa_comic": "DC",
#         "biografia": "Diana, princesa de las Amazonas, que lucha por la justicia, el amor y la igualdad en el mundo."
#     },
#     {
#         "nombre": "Iron Man",
#         "año_aparicion": 1963,
#         "casa_comic": "Marvel",
#         "biografia": "Tony Stark, un genio inventor y empresario que crea una armadura avanzada para convertirse en el superhéroe Iron Man."
#     },
#     {
#         "nombre": "Linterna Verde",
#         "año_aparicion": 1940,
#         "casa_comic": "DC",
#         "biografia": "Hal Jordan, un piloto que se convierte en miembro de la Green Lantern Corps, una fuerza policial intergaláctica."
#     },
#     {
#         "nombre": "Wolverine",
#         "año_aparicion": 1974,
#         "casa_comic": "Marvel",
#         "biografia": "Logan, un mutante con habilidades regenerativas y garras de adamantium."
#     },
#     {
#         "nombre": "Doctor Strange",
#         "año_aparicion": 1963,
#         "casa_comic": "Marvel",
#         "biografia": "Stephen Strange, un neurocirujano que se convierte en el Hechicero Supremo para proteger la Tierra contra amenazas místicas."
#     },
#     {
#         "nombre": "Capitana Marvel",
#         "año_aparicion": 1968,
#         "casa_comic": "Marvel",
#         "biografia": "Carol Danvers, una ex-piloto de la Fuerza Aérea que obtiene superpoderes y se convierte en una de las heroínas más poderosas del universo."
#     },
#     {
#         "nombre": "Flash",
#         "año_aparicion": 1940,
#         "casa_comic": "DC",
#         "biografia": "Barry Allen, un científico forense que obtiene la capacidad de moverse a supervelocidad después de un accidente en su laboratorio."
#     },
#     {
#         "nombre": "Star-Lord",
#         "año_aparicion": 1976,
#         "casa_comic": "Marvel",
#         "biografia": "Peter Quill, un aventurero intergaláctico y líder de los Guardianes de la Galaxia."
#     },
#     {
#         "nombre": "Superman",
#         "año_aparicion": 1938,
#         "casa_comic": "DC",
#         "biografia": "Clark Kent, un extraterrestre del planeta Krypton que posee poderes sobrehumanos en la Tierra."
#     },
#     {
#         "nombre": "Aquaman",
#         "año_aparicion": 1941,
#         "casa_comic": "DC",
#         "biografia": "Arthur Curry, el rey de la Atlántida que tiene la capacidad de comunicarse con la vida marina y posee una fuerza sobrehumana."
#     },
#     {
#         "nombre": "Thor",
#         "año_aparicion": 1962,
#         "casa_comic": "Marvel",
#         "biografia": "El dios del trueno, originario de Asgard, que protege tanto su hogar como la Tierra con su poderoso martillo Mjolnir."
#     },
#     {
#         "nombre": "Viuda Negra",
#         "año_aparicion": 1964,
#         "casa_comic": "Marvel",
#         "biografia": "Natasha Romanoff, una espía y asesina altamente entrenada que se convierte en una agente de S.H.I.E.L.D. y miembro de los Vengadores."
#     },
#     {
#         "nombre": "Flecha Verde",
#         "año_aparicion": 1941,
#         "casa_comic": "DC",
#         "biografia": "Oliver Queen, un millonario que combate el crimen como un arquero experto con un arco y una variedad de flechas especiales."
#     }
# ]

# #Funciones de busqueda, eliminacion y mostrar lista
# print("")
# print("----------------------------------")
# print("")
# def buscar(list_values, criterio, value):
#     for index, personaje in enumerate(list_values):
#         if personaje[criterio] == value:
    
#             return index
#     return None

# def eliminar(list_values, criterio, value):
#     index = buscar(list_values, criterio, value)
#     if index is not None:
#         return list_values.pop(index)
#     return None

# def mostrarlista(title, list_values):
#     print()
#     print(f"{title}")
#     for index, elemento in enumerate(list_values):
#         print(index, elemento)
#     print()

# # a. eliminar el nodo que contiene la información de Linterna Verde;
# print("")
# print("----------------------------------")
# print("")
# eliminado = "Linterna Verde"
# criterio = "nombre"
# result_delete = eliminar(superheroes, criterio, eliminado)

# # Mostrar el resultado de la eliminación
# print(f'Eliminar {eliminar} resultado: {result_delete}')

# # show_list("Lista despues de sacar a Linterna Verde", superheroes)

# # b. mostrar el año de aparición de Wolverine;
# print("")
# print("----------------------------------")
# print("")
# def encontraraño(list_values, criterio, value):
#     index = buscar(list_values, criterio, value)
#     if index is not None:
#         return list_values[index]["año_aparicion"]
#     return None

# value= 'Wolverine'
# añoaparicion = None
# busquedawolverine = encontraraño(superheroes,'nombre',value)

# if busquedawolverine is not None:
#     print(f'El año de aparición de {value} es {busquedawolverine}.')
# else:
#     print(f'{value} no se encuentra en la lista.')

# # c. cambiar la casa de Dr. Strange a Marvel;
# print("")
# print("----------------------------------")
# print("")

# def cambiarcasa (list_values, criterio, value,nuevacasa):
#     index = buscar(list_values, criterio, value)
#     if index is not None:
#         list_values[index]["casa_comic"] = nuevacasa

# cambiarcasa(superheroes,'nombre','Doctor Strange','DC')

# mostrarlista("Lista de Superhéroes después de cambiar la casa de Dr. Strange", superheroes)


# # d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;

# def puntod(list_values,criterio,value):
#     index = buscar(list_values, criterio, value)
#     if index is not None:
#         return list_values[index]["nombre"] and list_values[index]["biografia"]
    

    

# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;

# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;

# g. mostrar toda la información de Flash y Star-Lord;

# h. listar los superhéroes que comienzan con la letra B, M y S;

# i. determinar cuántos superhéroes hay de cada casa de comic.