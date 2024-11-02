# Lista de pokémones con sus atributos básicos: número, nombre, tipo y nivel.
pokemons = [
    {'numero': 1, 'nombre': 'Bulbasaur', 'tipo': ['Planta', 'Veneno'], 'nivel': 5},
    {'numero': 4, 'nombre': 'Charmander', 'tipo': ['Fuego'], 'nivel': 10},
    {'numero': 7, 'nombre': 'Squirtle', 'tipo': ['Agua'], 'nivel': 15},
    {'numero': 25, 'nombre': 'Pikachu', 'tipo': ['Electrico'], 'nivel': 20},
    {'numero': 37, 'nombre': 'Vulpix', 'tipo': ['Fuego'], 'nivel': 25},
    {'numero': 143, 'nombre': 'Snorlax', 'tipo': ['Normal'], 'nivel': 30},
    {'numero': 199, 'nombre': 'Slowking', 'tipo': ['Agua', 'Psiquico'], 'nivel': 35},
    {'numero': 1009, 'nombre': 'Mew', 'tipo': ['Psiquico'], 'nivel': 100}
]

# Funciones hash para generar claves en las tablas hash

def hash_tipo(pokemon):
    # Devuelve el tipo de un pokémon como clave hash.
    return pokemon['tipo']

def hash_numero(pokemon):
    # Devuelve el último dígito del número del pokémon como clave hash.
    return str(pokemon['numero'])[-1]

def hash_nivel(pokemon):
    # Devuelve el nivel del pokémon como clave hash.
    return pokemon['nivel']

# Tablas hash para almacenar pokémones según diferentes criterios.
tabla_tipo = {}
tabla_numero = {}
tabla_nivel = {}

# Función para agregar un pokémon a las tablas hash correspondientes.
def agregar_pokemon(pokemon):
    # Añade el pokémon a la tabla hash basada en su tipo.
    for tipo in pokemon['tipo']:
        if tipo not in tabla_tipo:  # Si el tipo no está en la tabla, lo añade con una lista vacía.
            tabla_tipo[tipo] = []
        tabla_tipo[tipo].append(pokemon)  # Agrega el pokémon a la lista correspondiente.

    # Añade el pokémon a la tabla hash basada en el último dígito de su número.
    clave_numero = hash_numero(pokemon)
    if clave_numero not in tabla_numero:
        tabla_numero[clave_numero] = []
    tabla_numero[clave_numero].append(pokemon)

    # Añade el pokémon a la tabla hash basada en su nivel.
    clave_nivel = hash_nivel(pokemon)
    if clave_nivel not in tabla_nivel:
        tabla_nivel[clave_nivel] = []
    tabla_nivel[clave_nivel].append(pokemon)

# e - Mostrar todos los Pokémons cuyos números terminan en 3, 7 y 9.

def mostrarpokemonesnumero():
    # Recorre cada número en la tabla de números.
    for numero in tabla_numero:
        # Verifica si el número termina en 3, 7 o 9.
        if numero == '3' or numero == '7' or numero == '9':
            pokemones = tabla_numero[numero]  # Obtiene la lista de pokémones para ese número.
            print(f"Pokémones que terminan en {numero}:")
            for pokemon in pokemones:  # Imprime cada pokémon cuyo número coincide.
                print(pokemon)
            print()  # Imprime una línea en blanco para separar bloques de resultados.

# f - Mostrar todos los Pokémons cuyos niveles son múltiplos de 2, 5 y 10.

def mostrarpokemonesnivel():
    print("Pokémones con niveles múltiplos de 2, 5 y 10:")
    print("")
    for nivel in tabla_nivel:  # Recorre cada nivel en la tabla hash de niveles.
        # Verifica si el nivel es múltiplo de 2, 5 y 10.
        if nivel % 2 == 0 and nivel % 5 == 0 and nivel % 10 == 0:
            pokemones = tabla_nivel[nivel]  # Obtiene la lista de pokémones para ese nivel.
            for pokemon in pokemones:  # Imprime cada pokémon cuyo nivel cumple la condición.
                print(pokemon)
            print()  # Imprime una línea en blanco para separar bloques de resultados.

# g - Mostrar todos los Pokémons de los siguientes tipos: Acero, Fuego, Eléctrico, Hielo.

def mostrarpokemonestipo(tiposinteres):
    # Recorre cada tipo de interés en la lista proporcionada.
    for tipo in tiposinteres:
        if tipo in tabla_tipo:  # Verifica si el tipo está en la tabla hash de tipos.
            pokemones = tabla_tipo[tipo]  # Obtiene la lista de pokémones para ese tipo.
            if pokemones:
                print(f'Pokémons de tipo: {tipo}:')
                for pokemon in pokemones:  # Imprime cada pokémon de ese tipo.
                    print(pokemon)
                print()  # Imprime una línea en blanco para separar bloques de resultados.
            else:
                print(f"No se encontraron Pokémones del tipo {tipo}")

# Agrega todos los pokémones de la lista principal a las tablas hash.
for pokemon in pokemons:
    agregar_pokemon(pokemon)

# Llama a las funciones para mostrar resultados específicos.
print("")
print("---------------------------------------------------")
mostrarpokemonesnumero()  # Muestra pokémones con números que terminan en 3, 7 y 9.
print("")
print("---------------------------------------------------")
mostrarpokemonesnivel()  # Muestra pokémones con niveles múltiplos de 2, 5 y 10.
print("")
print("---------------------------------------------------")
lista = ['Acero', 'Fuego', 'Electrico', 'Hielo']  # Lista de tipos de interés.
mostrarpokemonestipo(lista)  # Muestra pokémones de los tipos especificados.
