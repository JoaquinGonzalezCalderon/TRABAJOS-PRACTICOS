from AVL import ARBOLAVL

# 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
# se (MCU), desarrollar un algoritmo que contemple lo siguiente:

# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
# leano que indica si es un héroe o un villano, True y False respectivamente;

# b. listar los villanos ordenados alfabéticamente;

# c. mostrar todos los superhéroes que empiezan con C;

# d. determinar cuántos superhéroes hay el árbol;

# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;

# f. listar los superhéroes ordenados de manera descendente;

# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:

# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.

tree = ARBOLAVL()

#Se insertan los personajes
tree.insert_node("Iron Man", {'is_hero': True})
tree.insert_node("Thor", {'is_hero': True})
tree.insert_node("Hulk", {'is_hero': True})
tree.insert_node("Doctor Strange", {'is_hero': True})
tree.insert_node("Thanos", {'is_hero': False})
tree.insert_node("Loki", {'is_hero': False})
tree.insert_node("Red Skull", {'is_hero': False})
tree.insert_node("Captain America", {'is_hero': True})
tree.insert_node("Scarlet Witch", {'is_hero': False})
tree.insert_node("Black Widow", {'is_hero': True})

# Se muestran todos los villanos x orden alfabetico
print("Villanos ordenados alfabéticamente:")
tree.inorden_villanos()

# c. Mostrar todos los superhéroes que empiezan con "C"
print("\nSuperhéroes que empiezan con 'C':")
tree.inorden_superheros_start_with("C")

# d. determinar cuántos superhéroes hay en el árbol
print(f"\nCantidad de superhéroes: {tree.contar_super_heroes()}")

# e. Buscar y corregir el nombre de Doctor Strange usando búsqueda por proximidad
print("\nModificación del nombre de Doctor Strange:")
node = tree.proximity_search("Doctor Strange")  # Buscamos "Strange"
if node:
    print(f"Nodo encontrado: {node.value}")
    node.value = "Doctor Strange MOD"  # Modificamos el nombre del nodo encontrado
    print("Nombre modificado exitosamente.")
else:
    print("Doctor Strange no encontrado.")


# f. Listar los superhéroes ordenados de manera descendente
print("\nSuperhéroes ordenados de manera descendente:")
tree.postorden()  # Esto hace un recorrido descendente

# separar héroes y villanos en árboles distintos
heroes_tree = ARBOLAVL()
villains_tree = ARBOLAVL()

def separar_heroes_villanos(root, heroes_tree, villains_tree):
    if root is not None:
        if root.other_value.get('is_hero'):
            heroes_tree.insert_node(root.value, root.other_value)
        else:
            villains_tree.insert_node(root.value, root.other_value)
        separar_heroes_villanos(root.left, heroes_tree, villains_tree)
        separar_heroes_villanos(root.right, heroes_tree, villains_tree)

# Separar el árbol original en dos
separar_heroes_villanos(tree.root, heroes_tree, villains_tree)

# determinar cuántos nodos tiene cada árbol
print(f"\nCantidad de nodos en el árbol de héroes: {heroes_tree.contar_super_heroes()}")
print(f"Cantidad de nodos en el árbol de villanos: {villains_tree.contar_super_heroes()}")

# realizar un barrido ordenado alfabéticamente de cada árbol
print("\nBarrido ordenado de héroes:")
heroes_tree.inorden()

print("\nBarrido ordenado de villanos:")
villains_tree.inorden()



print("")
print("--------------------------------------------")
print("")

# 23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:
# a. listado inorden de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
# o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles.

arbol_avl = ARBOLAVL()

print("")
print("--------------------------------------------")
print("")

# Criaturas y quien las derroto
arbol_avl.insert_node("Ceto", {"derrotado_por": ""})
arbol_avl.insert_node("Tifón", {"derrotado_por": "Zeus"})
arbol_avl.insert_node("Equidna", {"derrotado_por": "Argos Panoptes"})
arbol_avl.insert_node("Dino", {"derrotado_por": ""})
arbol_avl.insert_node("Pefredo", {"derrotado_por": ""})
arbol_avl.insert_node("Enio", {"derrotado_por": ""})
arbol_avl.insert_node("Escila", {"derrotado_por": ""})
arbol_avl.insert_node("Caribdis", {"derrotado_por": ""})
arbol_avl.insert_node("Euriale", {"derrotado_por": ""})
arbol_avl.insert_node("Esteno", {"derrotado_por": ""})
arbol_avl.insert_node("Medusa", {"derrotado_por": "Perseo"})
arbol_avl.insert_node("Ladón", {"derrotado_por": "Heracles"})
arbol_avl.insert_node("Águila del Cáucaso", {"derrotado_por": ""})
arbol_avl.insert_node("Quimera", {"derrotado_por": "Belerofonte"})
arbol_avl.insert_node("Hidra de Lerna", {"derrotado_por": "Heracles"})
arbol_avl.insert_node("León de Nemea", {"derrotado_por": "Heracles"})
arbol_avl.insert_node("Esfinge", {"derrotado_por": ""})
arbol_avl.insert_node("Dragón de la Colúcida", {"derrotado_por": ""})
arbol_avl.insert_node("Cerbero", {"derrotado_por": ""})
arbol_avl.insert_node("Cerda de Cromión", {"derrotado_por": "Teseo"})
arbol_avl.insert_node("Ortros", {"derrotado_por": "Heracles"})
arbol_avl.insert_node("Toro de Creta", {"derrotado_por": "Teseo"})
arbol_avl.insert_node("Jabalí de Calidón", {"derrotado_por": "Atalanta"})
arbol_avl.insert_node("Carcinos", {"derrotado_por": ""})
arbol_avl.insert_node("Gerión", {"derrotado_por": "Heracles"})
arbol_avl.insert_node("Cloto", {"derrotado_por": ""})
arbol_avl.insert_node("Láquesis", {"derrotado_por": ""})
arbol_avl.insert_node("Átropos", {"derrotado_por": ""})
arbol_avl.insert_node("Minotauro de Creta", {"derrotado_por": "Teseo"})
arbol_avl.insert_node("Harpías", {"derrotado_por": ""})
arbol_avl.insert_node("Talos", {"derrotado_por": ""})
arbol_avl.insert_node("Sirenas", {"derrotado_por": ""})
arbol_avl.insert_node("Pitón", {"derrotado_por": "Apolo"})
arbol_avl.insert_node("Cierva de Cerinea", {"derrotado_por": ""})
arbol_avl.insert_node("Basilisco", {"derrotado_por": ""})
arbol_avl.insert_node("Jabalí de Erimanto", {"derrotado_por": ""})

print("")
print("--------------------------------------------")
print("")
# a. Inorden
print("Listado inorden de las criaturas:")
arbol_avl.inorden()

print("")
print("--------------------------------------------")
print("")
# b. Cargar descripciones

def agregar_descripcion(arbol, nombre_criatura, descripcion):
    criatura = arbol.search(nombre_criatura)
    if criatura:
        criatura.other_value["descripcion"] = descripcion
        print(f"Descripción agregada para {nombre_criatura}: {descripcion}")
    else:
        print(f"Criatura {nombre_criatura} no encontrada.")

# Agregar descripciones de todas las criaturas
agregar_descripcion(arbol_avl, "Ceto", "Criatura marina primordial.")
agregar_descripcion(arbol_avl, "Tifón", "El monstruo más terrible de la mitología griega.")
agregar_descripcion(arbol_avl, "Equidna", "Monstruo mitad mujer y mitad serpiente, madre de muchos de los monstruos de la mitología.")
agregar_descripcion(arbol_avl, "Dino", "Una de las Gorgonas, hija de Forcis y Ceto.")
agregar_descripcion(arbol_avl, "Pefredo", "Un monstruo marino que se dice que habitó el mar.")
agregar_descripcion(arbol_avl, "Enio", "Diosa de la guerra, a menudo asociada con la destrucción y el caos.")
agregar_descripcion(arbol_avl, "Escila", "Monstruo marino con cabeza de mujer y cuerpos de perros.")
agregar_descripcion(arbol_avl, "Caribdis", "Criatura marina que representa un remolino mortal.")
agregar_descripcion(arbol_avl, "Euriale", "Una de las Gorgonas, conocida por su belleza.")
agregar_descripcion(arbol_avl, "Esteno", "Una de las Gorgonas, famosa por su mirada petrificante.")
agregar_descripcion(arbol_avl, "Medusa", "La más famosa de las Gorgonas, que podía convertir a los hombres en piedra con su mirada.")
agregar_descripcion(arbol_avl, "Ladón", "Dragón que custodiaba las manzanas doradas del Jardín de las Hespérides.")
agregar_descripcion(arbol_avl, "Águila del Cáucaso", "Un águila gigante que devoraba el hígado de Prometeo.")
agregar_descripcion(arbol_avl, "Quimera", "Monstruo con partes de león, cabra y serpiente.")
agregar_descripcion(arbol_avl, "Hidra de Lerna", "Serpiente de muchas cabezas que se regeneraban si eran cortadas.")
agregar_descripcion(arbol_avl, "León de Nemea", "León invulnerable que fue derrotado por Heracles.")
agregar_descripcion(arbol_avl, "Esfinge", "Criatura con cuerpo de león y cabeza de mujer, que planteaba acertijos.")
agregar_descripcion(arbol_avl, "Dragón de la Colúcida", "Monstruo que custodiaba el Jardín de las Hespérides.")
agregar_descripcion(arbol_avl, "Cerbero", "Perro de tres cabezas que guardaba la entrada al inframundo.")
agregar_descripcion(arbol_avl, "Cerda de Cromión", "Un jabalí feroz que fue derrotado por Teseo.")
agregar_descripcion(arbol_avl, "Ortros", "Perro de dos cabezas que custodiaba el ganado de Gerión.")
agregar_descripcion(arbol_avl, "Toro de Creta", "Un toro monstruoso que fue capturado por Teseo.")
agregar_descripcion(arbol_avl, "Jabalí de Calidón", "Un jabalí que fue cazado por Atalanta y otros héroes.")
agregar_descripcion(arbol_avl, "Carcinos", "Un cangrejo gigante que ayudó a Hera a luchar contra Heracles.")
agregar_descripcion(arbol_avl, "Gerión", "Gigante de tres cuerpos que fue derrotado por Heracles.")
agregar_descripcion(arbol_avl, "Cloto", "Una de las Moiras que controla el hilo de la vida.")
agregar_descripcion(arbol_avl, "Láquesis", "Otra de las Moiras que determina el destino.")
agregar_descripcion(arbol_avl, "Átropos", "La tercera de las Moiras que corta el hilo de la vida.")
agregar_descripcion(arbol_avl, "Minotauro de Creta", "Criatura con cuerpo de hombre y cabeza de toro, que fue derrotada por Teseo.")
agregar_descripcion(arbol_avl, "Harpías", "Criaturas aladas que robaban y atormentaban a los hombres.")
agregar_descripcion(arbol_avl, "Talos", "Un gigante de bronce que custodiaba Creta.")
agregar_descripcion(arbol_avl, "Sirenas", "Criaturas que atraían a los marineros con su canto.")
agregar_descripcion(arbol_avl, "Pitón", "Serpiente gigante que fue derrotada por Apolo.")
agregar_descripcion(arbol_avl, "Cierva de Cerinea", "Cierva sagrada que fue capturada por Heracles.")
agregar_descripcion(arbol_avl, "Basilisco", "Criatura que podía matar con la mirada.")
agregar_descripcion(arbol_avl, "Jabalí de Erimanto", "Jabalí monstruoso que fue capturado por Heracles.")

print("")
print("--------------------------------------------")
print("")

# c. Mostrar información de Talos
talos = arbol_avl.proximity_search("Talos")
if talos:
    print(f"Criatura: {talos.value}, Derrotado por: {talos.other_value['derrotado_por']}")

print("")
print("--------------------------------------------")
print("")

# d. Tres héroes o dioses que derrotaron más criaturas
heroes = {}
def contar_derrotas(root):
    if root:
        if root.other_value['derrotado_por']:
            heroe = root.other_value['derrotado_por']
            if heroe in heroes:
                heroes[heroe] += 1
            else:
                heroes[heroe] = 1
        contar_derrotas(root.left)
        contar_derrotas(root.right)

contar_derrotas(arbol_avl.root)
top_heroes = sorted(heroes.items(), key=lambda x: x[1], reverse=True)[:3]
print(f"Top 3 héroes/dioses: {top_heroes}")

print("")
print("--------------------------------------------")
print("")

# e. Listado de criaturas derrotadas por Heracles
print("Criaturas derrotadas por Heracles:")
def criaturas_por_heracles(root):
    if root:
        if root.other_value['derrotado_por'] == "Heracles":
            print(root.value)
        criaturas_por_heracles(root.left)
        criaturas_por_heracles(root.right)

criaturas_por_heracles(arbol_avl.root)

print("")
print("--------------------------------------------")
print("")

# f. Listado de criaturas no derrotadas
print("Criaturas no derrotadas:")
def criaturas_no_derrotadas(root):
    if root:
        if root.other_value['derrotado_por'] == "":
            print(root.value)
        criaturas_no_derrotadas(root.left)
        criaturas_no_derrotadas(root.right)

criaturas_no_derrotadas(arbol_avl.root)

print("")
print("--------------------------------------------")
print("")

# g. Modificar campo "capturada" para criaturas atrapadas por Heracles
for criatura in ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]:
    nodo = arbol_avl.search(criatura)
    if nodo:
        nodo.other_value["capturada"] = "Heracles"

print("")
print("--------------------------------------------")
print("")

# h. Buscar por coincidencia
print("Búsqueda por coincidencia (criaturas que comienzan con 'C'):")
coincidencia = arbol_avl.proximity_search("C")
if coincidencia:
    print(coincidencia.value)

print("")
print("--------------------------------------------")
print("")

# j. Eliminar Basilisco y Sirenas
arbol_avl.delete_node("Basilisco")
arbol_avl.delete_node("Sirenas")

print("")
print("--------------------------------------------")
print("")

# k. Modificar Aves del Estínfalo para agregar que Heracles las derrotó
aves = arbol_avl.search("Aves del Estínfalo")
if aves:
    aves.other_value["derrotado_por"] = "Heracles"

print("")
print("--------------------------------------------")
print("")

# l. Modificar nombre de Ladón por Dragón Ladón
ladon = arbol_avl.search("Ladón")
if ladon:
    arbol_avl.delete_node("Ladón")
    arbol_avl.insert_node("Dragón Ladón", {"derrotado_por": "Heracles"})

print("")
print("--------------------------------------------")
print("")

# m. Listado por nivel del árbol
print("Listado por nivel del árbol:")
arbol_avl.by_level()

print("")
print("--------------------------------------------")
print("")

# n. Mostrar criaturas capturadas por Heracles
print("Criaturas capturadas por Heracles:")
def criaturas_capturadas_por_heracles(root):
    if root:
        if root.other_value.get("capturada") == "Heracles":
            print(root.value)
        criaturas_capturadas_por_heracles(root.left)
        criaturas_capturadas_por_heracles(root.right)

criaturas_capturadas_por_heracles(arbol_avl.root)
