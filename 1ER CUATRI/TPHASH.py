# lista de pokemones con sus: número, nombre, tipo y nivel.
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

# Funciones hash

def hash_tipo(pokemon):
    # Devuelve el tipo de un pokémon como clave hash.
    return pokemon['tipo']

def hash_numero(pokemon):
    # Devuelve el último dígito del número del pokémon como clave hash.
    return str(pokemon['numero'])[-1]

def hash_nivel(pokemon):
    # Devuelve el nivel del pokémon como clave hash.
    return pokemon['nivel']

tabla_tipo = {}
tabla_numero = {}
tabla_nivel = {}


def agregar_pokemon(pokemon):
    for tipo in pokemon['tipo']:
        if tipo not in tabla_tipo:  # si no esta, lo añade con una lista vacía.
            tabla_tipo[tipo] = []
        tabla_tipo[tipo].append(pokemon) 

    # Se añade el pokémon a la tabla hash basada en el último dígito de su número.
    clave_numero = hash_numero(pokemon)
    if clave_numero not in tabla_numero:
        tabla_numero[clave_numero] = []
    tabla_numero[clave_numero].append(pokemon)

    # Añade el pokémon a la tabla hash por su nivel.
    clave_nivel = hash_nivel(pokemon)
    if clave_nivel not in tabla_nivel:
        tabla_nivel[clave_nivel] = []
    tabla_nivel[clave_nivel].append(pokemon)

# e - Mostrar todos los Pokémons cuyos números terminan en 3, 7 y 9.

def mostrarpokemonesnumero():
    for numero in tabla_numero:
        # verifica si el num = 3, 7 o 9.
        if numero == '3' or numero == '7' or numero == '9':
            pokemones = tabla_numero[numero]  
            print(f"Pokémones que terminan en {numero}:")
            for pokemon in pokemones:  
                print(pokemon)
            print()  # linea en blanco

# f - Mostrar todos los Pokémons cuyos niveles son múltiplos de 2, 5 y 10.

def mostrarpokemonesnivel():
    print("Pokémones con niveles múltiplos de 2, 5 y 10:")
    print("")
    for nivel in tabla_nivel: 
        # verifica si el nivel es múltiplo de 2, 5 y 10.
        if nivel % 2 == 0 and nivel % 5 == 0 and nivel % 10 == 0:
            pokemones = tabla_nivel[nivel]  
            for pokemon in pokemones:  
                print(pokemon)
            print()  

# g - Mostrar todos los Pokémons de los siguientes tipos: Acero, Fuego, Eléctrico, Hielo.

def mostrarpokemonestipo(tiposinteres):
    
    for tipo in tiposinteres:
        if tipo in tabla_tipo:  
            pokemones = tabla_tipo[tipo]  
            if pokemones:
                print(f'Pokémons de tipo: {tipo}:')
                for pokemon in pokemones:  
                    print(pokemon)
                print()  
            else:
                print(f"No se encontraron Pokémones del tipo {tipo}")


for pokemon in pokemons:
    agregar_pokemon(pokemon)

# impresion de resultados
print("")
print("---------------------------------------------------")
mostrarpokemonesnumero()  # pokémones con números que terminan en 3, 7 y 9.
print("")
print("---------------------------------------------------")
mostrarpokemonesnivel()  # pokémones con niveles múltiplos de 2, 5 y 10.
print("")
print("---------------------------------------------------")
lista = ['Acero', 'Fuego', 'Electrico', 'Hielo']  # Lista de tipos de interés.
mostrarpokemonestipo(lista)  # pokémones de los tipos especificados.
