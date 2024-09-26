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
